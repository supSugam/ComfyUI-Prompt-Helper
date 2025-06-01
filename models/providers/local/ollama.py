from tqdm import tqdm
from ollama import Client, ListResponse
from utils import image_to_base64
from models.base import PromptModelBase
from defaults import DEFAULT_OLLAMA_API_HOST, DEFAULT_OLLAMA_TIMEOUT

class OllamaUtil:
    def __init__(self, client: Client):
        self.client = client

    def get_models(self):
        response: ListResponse = self.client.list()
        return [model.model for model in response.models]

    def pull_model(self, model: str):
        current_digest, bars = '', {}
        for progress in self.client.pull(model, stream=True):
            digest = progress.get('digest', '')
            if digest != current_digest and current_digest in bars:
                bars[current_digest].close()

            if not digest:
                print(progress.get('status'))
                continue

            if digest not in bars and (total := progress.get('total')):
                bars[digest] = tqdm(total=total, desc=f'pulling {digest[7:19]}', unit='B', unit_scale=True)

            if completed := progress.get('completed'):
                bars[digest].update(completed - bars[digest].n)

            current_digest = digest

class OllamaModel(PromptModelBase):
    def __init__(self, model_name: str, keep_model_alive: bool = False):
        self.client = Client(DEFAULT_OLLAMA_API_HOST, timeout=DEFAULT_OLLAMA_TIMEOUT)
        self.model_name = model_name
        self.keep_model_alive = 1 if keep_model_alive else None
        self.util = OllamaUtil(self.client)

    def image_to_prompt(self, image, system_instruction, user_instruction, max_tokens, **kwargs):
        
        models = self.util.get_models()
        
        model = self.model_name.strip()
        
        if model not in models:
            print(f"Downloading model: {model}")
            self.util.pull_model(model)
            
        print('System Context: "{}"'.format(system_instruction))
        print('Prompt: "{}"'.format(user_instruction))

        full_response = ""
                
        print('Generating Response')
        full_response =  self.client.generate(model=model, system=system_instruction, prompt=user_instruction, keep_alive=self.keep_model_alive, stream=False, images=[image], options={
                'num_predict': max_tokens,
        })
        result = full_response['response']
        return (result, )
    

    def refine_prompt(self, prompt, instructions=None, **kwargs):
        instruction_text = instructions or ""
        combined = f"{instruction_text}\n\n{prompt}"
        response = self.client.generate(model=self.model_name, prompt=combined)
        return response.get("response", "").strip()



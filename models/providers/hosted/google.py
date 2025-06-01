from models.base import PromptModelBase
from google import genai
from defaults import DEFAULT_SYSTEM_INSTRUCTIONS_IMG2PROMPT, DEFAULT_USER_INSTRUCTIONS_IMG2PROMPT

class Gemini2FlashModel(PromptModelBase):
    def image_to_prompt(self, image, system_instruction=DEFAULT_SYSTEM_INSTRUCTIONS_IMG2PROMPT,
                        user_instruction=DEFAULT_USER_INSTRUCTIONS_IMG2PROMPT, **kwargs):
        client = genai.Client(api_key="YOUR_API_KEY")
        my_file = client.files.upload(file=image)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[my_file, user_instruction],
        )
        return response.text

class Gemini25FlashPreviewModel(PromptModelBase):
    def image_to_prompt(self, image, system_instruction=DEFAULT_SYSTEM_INSTRUCTIONS_IMG2PROMPT,
                        user_instruction=DEFAULT_USER_INSTRUCTIONS_IMG2PROMPT, **kwargs):
        client = genai.Client(api_key="YOUR_API_KEY")
        my_file = client.files.upload(file=image)
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview",
            contents=[my_file, user_instruction],
        )
        return response.text

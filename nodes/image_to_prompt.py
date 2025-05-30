from ..models import MODELS_WITH_IMAGE_SUPPORT
from ..defaults import DEFAULT_SYSTEM_PROMPT_IMG2PROMPT, DEFAULT_INSTRUCTIONS_IMG2PROMPT

class ImageToPrompt:

    @classmethod
    def INPUT_TYPES(cls):

        # Base UI inputs
        inputs = {
            "required": {
            "image": ("IMAGE",),
            "model": (MODELS_WITH_IMAGE_SUPPORT,),
            "system_prompt": (
                "STRING", {
                "default": DEFAULT_SYSTEM_PROMPT_IMG2PROMPT,
                "multiline": True,
                "title": "System Prompt"
                }
            ),
            "instructions": (
                "STRING", {
                "default": DEFAULT_INSTRUCTIONS_IMG2PROMPT,
                "multiline": True,
                "title": "Instructions"
                }
            )
            },
            "optional": {}
        }

        return inputs

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate"
    CATEGORY = "Prompt Helper"

    def generate(self, image, model, system_prompt, instructions, **kwargs):
        # Handle API key override
        api_key_override = kwargs.get(f"{model.split('/')[0].upper()} API Key", "").strip()
        system_prompt = system_prompt.strip() or DEFAULT_SYSTEM_PROMPT_IMG2PROMPT
        instructions = instructions.strip() or DEFAULT_INSTRUCTIONS_IMG2PROMPT
        # TODO: use api_key_override if provided
        return ("Prompt generation not implemented yet.",)

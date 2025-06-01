from models.registry import MODELS_WITH_IMAGE_SUPPORT, MODELS
from ..defaults import (
    DEFAULT_SYSTEM_INSTRUCTIONS_IMG2PROMPT,
    DEFAULT_USER_INSTRUCTIONS_IMG2PROMPT,
)
from ..utils import image_to_temp_file


class ImageToPrompt:

    @classmethod
    def INPUT_TYPES(cls):

        # Base UI inputs
        inputs = {
            "required": {
                "image": ("IMAGE",),
                "model": (MODELS_WITH_IMAGE_SUPPORT,),
                "system_prompt": (
                    "STRING",
                    {
                        "default": DEFAULT_SYSTEM_INSTRUCTIONS_IMG2PROMPT,
                        "multiline": True,
                        "title": "System Prompt",
                    },
                ),
                "instructions": (
                    "STRING",
                    {
                        "default": DEFAULT_USER_INSTRUCTIONS_IMG2PROMPT,
                        "multiline": True,
                        "title": "Instructions",
                    },
                ),
            },
            "optional": {
                "keep_model_alive": (
                    "BOOLEAN",
                    {"default": False, "title": "Keep Model Alive"},
                ),
            },
        }

        return inputs

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate"
    CATEGORY = "Prompt Helper"

    def generate(self, image, model, system_prompt, instructions, keep_model_alive=False, **kwargs):

        # Check if the model is registered
        if model not in MODELS:
            raise ValueError(f"Model {model} is not registered.")

        final_image = image_to_temp_file(image)

        # Get the model instance from the registry
        model_cls = MODELS[model]["model_class"]
        model_instance = model_cls(**kwargs)
        # Call the image_to_prompt method with the provided parameters
        response = model_instance.image_to_prompt(
            image=final_image,
            system_instruction=system_prompt,
            user_instruction=instructions,
            **kwargs,
        )
        # Return the response as a tuple
        return (response,)

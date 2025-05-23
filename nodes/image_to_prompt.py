from models import MODEL_REGISTRY

class ImageToPrompt:

    @classmethod
    def INPUT_TYPES(cls):
        model_choices = list(MODEL_REGISTRY.keys())
        default_model = "openai/gpt-4-vision-preview"

        # Placeholder: user picks the model before execution
        selected_model_key = default_model  # This will always be the UI default at load time
        model_meta = MODEL_REGISTRY[selected_model_key]
        provider = selected_model_key.split("/")[0]

        # Base UI inputs
        inputs = {
            "required": {
                "image": ("IMAGE",),
                "model": (
                    "STRING", {
                        "default": default_model,
                        "choices": model_choices
                    }
                ),
                "system_prompt": (
                    "STRING", {
                        "default": "You are a helpful image captioner.",
                        "multiline": True
                    }
                ),
                "instructions": (
                    "STRING", {
                        "default": "Describe the image vividly and use descriptive language.",
                        "multiline": True
                    }
                )
            },
            "optional": {}
        }

        # If this is a remote model, add API key input
        if not model_meta["is_local"]:
            inputs["optional"][f"{provider.upper()} API Key"] = ("STRING", {
                "default": "",
                "multiline": False
            })

        return inputs

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate"
    CATEGORY = "Prompt Helper"

    def generate(self, image, model, system_prompt, instructions, **kwargs):
        # Handle API key override
        api_key_override = kwargs.get(f"{model.split('/')[0].upper()} API Key", "").strip()
        # TODO: use api_key_override if provided
        return ("Prompt generation not implemented yet.",)

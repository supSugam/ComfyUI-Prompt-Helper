class ImageToPrompt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "instructions": ("STRING", {"multiline": True}),
                # model selection can come later
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate"
    CATEGORY = "Prompt Helper"

    def generate(self, image, instructions):
        """
        Generate a prompt from an image and instructions.
        """

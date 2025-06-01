"""Top-level package for prompt_helper."""

from .nodes.image_to_prompt import ImageToPrompt

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
]

__author__ = """Sugam"""
__email__ = "sugamsubedi234@gmail.com"
__version__ = "0.0.1"

NODE_CLASS_MAPPINGS = {
    "ImageToPrompt": ImageToPrompt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageToPrompt": "Image → Prompt",
}

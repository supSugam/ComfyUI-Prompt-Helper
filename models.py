from typing import Literal, TypedDict

class ModelConfig(TypedDict):
    provider: str
    is_local: bool
    title: str
    allow_images: bool

ModelKey = Literal[
    "openai/gpt-4-vision-preview",
    "openai/gpt-4o",
    "fancyfeast/joy-caption-pre-alpha",
    "salesforce/blip-2"
]

MODELS: dict[ModelKey, ModelConfig] = {
    "openai/gpt-4-vision-preview": {
        "provider": "openai",
        "is_local": False,
        "title": "GPT-4 Vision (OpenAI)",
        "allow_images": True
    },
    "openai/gpt-4o": {
        "provider": "openai",
        "is_local": False,
        "title": "GPT-4o (OpenAI)",
        "allow_images": True
    },
    "fancyfeast/joy-caption-pre-alpha": {
        "provider": "fancyfeast",
        "is_local": True,
        "title": "JoyCaption Pre-Alpha",
        "allow_images": True
    },
    "salesforce/blip-2": {
        "provider": "salesforce",
        "is_local": True,
        "title": "BLIP-2",
        "allow_images": True
    },
}


class PromptModelBase:
    """
    Abstract base class for prompt models (API or local).
    """
    def __init__(self, config=None):
        self.config = config or {}

    def image_to_prompt(self, image, instructions=None):
        """
        Convert image to prompt using optional instructions.
        """
        raise NotImplementedError

    def refine_prompt(self, prompt, instructions=None):
        """
        Refine a prompt using instructions.
        """
        raise NotImplementedError

MODEL_REGISTRY: dict[ModelKey, type[PromptModelBase]] = {}
def register_model(name: ModelKey):
    def decorator(cls):
        MODEL_REGISTRY[name] = cls
        return cls
    return decorator

@register_model("openai/gpt-4o")
class OpenAIGPT4oModel(PromptModelBase):
    def image_to_prompt(self, image, instructions=None):
        # Implementation for OpenAI GPT-4o
        pass

    def refine_prompt(self, prompt, instructions=None):
        # Implementation for refining prompt
        pass

ALL_MODELS = list(MODELS.keys())
MODELS_WITH_IMAGE_SUPPORT = [key for key, config in MODELS.items() if config["allow_images"]]

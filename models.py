from typing import TypedDict
from .defaults import (
    DEFAULT_SYSTEM_INSTRUCTIONS_IMG2PROMPT,
    DEFAULT_USER_INSTRUCTIONS_IMG2PROMPT,
    ModelKey,
)

class ModelConfig(TypedDict):
    provider: str
    is_local: bool
    title: str
    allow_images: bool


MODELS: dict[ModelKey, ModelConfig] = {
    "openai/gpt-4-vision-preview": {
        "provider": "openai",
        "is_local": False,
        "title": "GPT-4 Vision (OpenAI)",
        "allow_images": True,
    },
    "openai/gpt-4o": {
        "provider": "openai",
        "is_local": False,
        "title": "GPT-4o (OpenAI)",
        "allow_images": True,
    },
    "fancyfeast/joy-caption-pre-alpha": {
        "provider": "fancyfeast",
        "is_local": True,
        "title": "JoyCaption Pre-Alpha",
        "allow_images": True,
    },
    "salesforce/blip-2": {
        "provider": "salesforce",
        "is_local": True,
        "title": "BLIP-2",
        "allow_images": True,
    },
    "google/gemini-2.5-flash-preview": {
        "provider": "google",
        "is_local": False,
        "title": "Gemini 2.0 Flash Preview",
        "allow_images": True,
    },
    "google/gemini-2.0-flash": {
        "provider": "google",
        "is_local": False,
        "title": "Gemini 2.0 Flash",
        "allow_images": True,
    },
}


class PromptModelBase:
    """
    Abstract base class for prompt models (API or local).
    """

    def __init__(self, config=None):
        self.config = config or {}

    def image_to_prompt(
        self,
        image,
        system_instruction,
        user_instruction,
        **kwargs
    ):
        """
        Convert image to prompt using optional instructions.
        """
        raise NotImplementedError

    def refine_prompt(self, prompt, instructions=None, **kwargs):
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


@register_model("google/gemini-2.0-flash")
class Gemini2FlashModel(PromptModelBase):
    def image_to_prompt(self, image, system_instruction=DEFAULT_SYSTEM_INSTRUCTIONS_IMG2PROMPT,
                        user_instruction=DEFAULT_USER_INSTRUCTIONS_IMG2PROMPT, **kwargs):
        """
        Convert an image to a prompt using Gemini 2.0 Flash.
        """

        from google import genai

        client = genai.Client(api_key="AIzaSyAOmBlMfZVDrTXwbIaxivHzyeMQlVHvytI")

        my_file = client.files.upload(file=image)

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[my_file, user_instruction],
        )

        return response.text

@register_model("google/gemini-2.5-flash-preview")
class Gemini25FlashPreviewModel(PromptModelBase):
    def image_to_prompt(self, image, system_instruction=DEFAULT_SYSTEM_INSTRUCTIONS_IMG2PROMPT,
                        user_instruction=DEFAULT_USER_INSTRUCTIONS_IMG2PROMPT, **kwargs):
        """
        Convert an image to a prompt using Gemini 2.5 Flash Preview.
        """

        from google import genai

        client = genai.Client(api_key="AIzaSyAOmBlMfZVDrTXwbIaxivHzyeMQlVHvytI")

        my_file = client.files.upload(file=image)

        response = client.models.generate_content(
            model="gemini-2.5-flash-preview",
            contents=[my_file, user_instruction],
        )

        return response.text

ALL_MODELS = list(MODELS.keys())
MODELS_WITH_IMAGE_SUPPORT = [
    key for key, config in MODELS.items() if config["allow_images"]
]

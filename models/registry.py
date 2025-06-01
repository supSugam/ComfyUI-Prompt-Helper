from typing import TypedDict
# from .providers.hosted.openai import GPT4VisionModel
from .providers.hosted.google import Gemini2FlashModel, Gemini25FlashPreviewModel
from .providers.local.nlpconnect import NlpconnectVitGpt2Caption
# from .providers.local.fancyfeast import JoyCaptionModel
# from .providers.local.salesforce import Blip2Model
from .base import PromptModelBase

# ModelTypeEnum

import enum

class ModelLocationEnum(enum.Enum):
    LOCAL = "local"
    HOSTED = "hosted"

class ModelBackendEnum(enum.Enum):
    TRANSFORMERS = "transformers"
    OLLAMA = "ollama"
    API = "api"

class ModelConfig(TypedDict):
    provider: str
    location: ModelLocationEnum
    backend: ModelBackendEnum
    title: str
    allow_images: bool
    model_class: type

MODELS: dict[str, ModelConfig] = {
    # "openai/gpt-4-vision-preview": {
    #     "provider": "openai",
    #     "location": ModelLocationEnum.HOSTED,
    #     "backend": ModelBackendEnum.API,
    #     "title": "GPT-4 Vision (OpenAI)",
    #     "allow_images": True,
    #     "model_class": GPT4VisionModel,
    # },
    # "openai/gpt-4o": {
    #     "provider": "openai",
    #     "location": ModelLocationEnum.HOSTED,
    #     "backend": ModelBackendEnum.API,
    #     "title": "GPT-4o (OpenAI)",
    #     "allow_images": True,
    #     "model_class": GPT4VisionModel,
    # },
    "google/gemini-2.0-flash": {
        "provider": "google",
        "location": ModelLocationEnum.HOSTED,
        "backend": ModelBackendEnum.API,
        "title": "Gemini 2.0 Flash",
        "allow_images": True,
        "model_class": Gemini2FlashModel,

    },
    "google/gemini-2.5-flash-preview": {
        "provider": "google",
        "location": ModelLocationEnum.HOSTED,
        "backend": ModelBackendEnum.API,
        "title": "Gemini 2.5 Flash Preview",
        "allow_images": True,
        "model_class": Gemini25FlashPreviewModel,
    },
        "nlpconnect/vit-gpt2": {
        "provider": "nlpconnect",
        "location": ModelLocationEnum.LOCAL,
        "backend": ModelBackendEnum.TRANSFORMERS,
        "title": "ViT-GPT2 (Image Captioning)",
        "allow_images": True,
        "model_class": NlpconnectVitGpt2Caption,
    },
    # "fancyfeast/joy-caption-pre-alpha": {
    #     "provider": "fancyfeast",
    #     "location": ModelLocationEnum.LOCAL,
    #     "backend": ModelBackendEnum.TRANSFORMERS,
    #     "title": "JoyCaption Pre-Alpha",
    #     "allow_images": True,
    #     "model_class": JoyCaptionModel,
    #     "max_tokens": None,
    # },
    # "salesforce/blip-2": {
    #     "provider": "salesforce",
    #     "location": ModelLocationEnum.LOCAL,
    #     "backend": ModelBackendEnum.TRANSFORMERS,
    #     "title": "BLIP-2",
    #     "allow_images": True,
    #     "model_class": Blip2Model,
    #     "max_tokens": None,
    # },
}

ALL_MODELS = list(MODELS.keys())
MODELS_WITH_IMAGE_SUPPORT = [
    key for key, cfg in MODELS.items() if cfg["allow_images"]
]

def get_model_instance(model_key: str) -> PromptModelBase:
    config = MODELS.get(model_key)
    if not config:
        raise ValueError(f"Model '{model_key}' is not registered.")

    model_class = config.get("model_class")
    if model_class is None:
        raise ValueError(f"Model '{model_key}' is not implemented.")
    kwargs = {}
    if "max_tokens" in config:
        kwargs["max_tokens"] = config["max_tokens"]
    return model_class(**kwargs)

ALL_MODELS = list(MODELS.keys())
MODELS_WITH_IMAGE_SUPPORT = [k for k, v in MODELS.items() if v.get("allow_images")]

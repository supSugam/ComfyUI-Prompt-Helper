from typing import Literal


DEFAULT_SYSTEM_INSTRUCTIONS_IMG2PROMPT = "You are a helpful image captioner."
DEFAULT_USER_INSTRUCTIONS_IMG2PROMPT = "Describe the image vividly and use descriptive language."


ModelKey = Literal[
    "openai/gpt-4-vision-preview",
    "openai/gpt-4o",
    "fancyfeast/joy-caption-pre-alpha",
    "salesforce/blip-2",
    "google/gemini-2.5-flash-preview",
    "google/gemini-2.0-flash",
]

DEFAULT_MODEL_IMG2PROMPT: ModelKey = "openai/gpt-4o"

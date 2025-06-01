from typing import Literal


DEFAULT_SYSTEM_INSTRUCTIONS_IMG2PROMPT = "You are a helpful image captioner."
DEFAULT_SYSTEM_INSTRUCTIONS_PROMPT2PROMPT = "You are a helpful prompt refiner."

DEFAULT_USER_INSTRUCTIONS_IMG2PROMPT = "Describe the image vividly and use descriptive language."
DEFAULT_USER_INSTRUCTIONS_PROMPT2PROMPT = "Refine the prompt to be more descriptive and vivid."


DEFAULT_MAX_TOKENS_IMG2PROMPT = 1000
DEFAULT_MAX_TOKENS_PROMPT2PROMPT = 1000


DEFAULT_OLLAMA_API_HOST = "http://localhost:11434"
DEFAULT_OLLAMA_TIMEOUT = 300

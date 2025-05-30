from .models import ModelKey


DEFAULT_SYSTEM_PROMPT_IMG2PROMPT = "You are a helpful image captioner."
DEFAULT_INSTRUCTIONS_IMG2PROMPT = "Describe the image vividly and use descriptive language."


# Get type hint , possible?
DEFAULT_MODEL_IMG2PROMPT: ModelKey = "openai/gpt-4o"

class PromptModelBase:
    """
    Abstract base class for prompt models (API or local).
    """

    def image_to_prompt(self, image, system_instruction, user_instruction, max_tokens, **kwargs):
        """
        Convert image to prompt using optional instructions.
        """
        raise NotImplementedError

    def refine_prompt(self, prompt, instructions=None, **kwargs):
        """
        Refine a prompt using instructions.
        """
        if instructions:
            return f"{instructions.strip()}\n{prompt.strip()}"
        return prompt

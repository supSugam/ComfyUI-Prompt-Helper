from models.base import PromptModelBase
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch

class NlpconnectVitGpt2Caption(PromptModelBase):
    def __init__(self):
        self.model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        self.processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        self.tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = self.model.to(self.device)
        self.gen_kwargs = {"max_length": 16, "num_beams": 4}

    def image_to_prompt(self, image, system_instruction=None, user_instruction=None, **kwargs):
        if image.mode != "RGB":
            image = image.convert(mode="RGB")

        pixel_values = self.processor(images=image, return_tensors="pt").pixel_values.to(self.device)
        output_ids = self.model.generate(pixel_values, **self.gen_kwargs)
        caption = self.tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()
        return caption

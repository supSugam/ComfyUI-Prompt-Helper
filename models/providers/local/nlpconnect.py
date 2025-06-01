from ....models.base import PromptModelBase
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image

class NlpconnectVitGpt2Caption(PromptModelBase):
    def __init__(self):
        self.model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        self.processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        self.tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = self.model.to(self.device)
        self.gen_kwargs = {"max_length": 16, "do_sample": False}

    def image_to_prompt(self, image, system_instruction=None, user_instruction=None, max_tokens=100, **kwargs):

        if isinstance(image, str):
            image = Image.open(image)

        if image.mode != "RGB":
            image = image.convert(mode="RGB")

        pixel_values = self.processor(images=[image], return_tensors="pt").pixel_values
        pixel_values = pixel_values.to(self.device)
        output_ids = self.model.generate(pixel_values, **self.gen_kwargs)
        caption = self.tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0]
        return caption
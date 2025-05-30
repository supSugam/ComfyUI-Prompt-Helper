import tempfile
import torch
from PIL import Image
import io

def tensor_to_image(tensor):
    tensor = tensor.cpu()
    image_np = tensor.squeeze().mul(255).clamp(0, 255).byte().numpy()
    return Image.fromarray(image_np, mode='RGB')


def image_to_temp_file(tensor_img: torch.Tensor, suffix=".png"):
    img = tensor_to_image(tensor_img)
    temp = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
    img.save(temp, format="PNG")
    temp.flush()
    temp.close()
    return temp.name

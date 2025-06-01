import tempfile
import torch
from PIL import Image
from io import BytesIO
import base64


def tensor_to_image(tensor):
    tensor = tensor.cpu()
    image_np = tensor.squeeze().mul(255).clamp(0, 255).byte().numpy()
    return Image.fromarray(image_np, mode='RGB')

def image_to_bytes(image: Image.Image):
    with BytesIO() as output:
        image.save(output, format="PNG")
        image_bytes = output.getvalue()
    return image_bytes

def image_to_base64(image: Image.Image):
    with BytesIO() as output:
        image.save(output, format="PNG")
        image_bytes = output.getvalue()
        image_base64 = base64.b64encode(image_bytes)
    return image_base64



def image_to_temp_file(tensor_img: torch.Tensor, suffix=".png"):
    img = tensor_to_image(tensor_img)
    temp = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
    img.save(temp, format="PNG")
    temp.flush()
    temp.close()
    return temp.name

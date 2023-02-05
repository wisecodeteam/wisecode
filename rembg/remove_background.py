import rembg
from PIL import Image
input_path = "image_before.jpg"
output_path = "image_after.png"
input_image = Image.open(input_path)
output_image = rembg.remove(input_image)
output_image.save(output_path)
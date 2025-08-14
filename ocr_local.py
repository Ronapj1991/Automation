from pathlib import Path
import pytesseract as tess
from PIL import Image

img_path = input("Please paste the path of the image: ")
img_path = img_path.strip("\"").strip()

image = Image.open(Path(fr"{img_path}"))

text = tess.image_to_string(image)

print(text)

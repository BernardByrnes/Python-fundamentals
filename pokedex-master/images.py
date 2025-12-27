try:
    from PIL import Image, ImageFilter
except ModuleNotFoundError:
    print("Pillow is not installed. Install it with: python -m pip install pillow")
    raise

from pathlib import Path
import sys

img_path = Path(__file__).parent / 'Pokedex' / 'pikachu.jpg'

if not img_path.exists():
    print(f"File not found: {img_path}")
    sys.exit(1)

try:
    img = Image.open(img_path)
except Exception as e:
    print(f"Failed to open image {img_path}: {e}")
    sys.exit(1)

print(img)
# print("format:", img.format, "size:", img.size, "mode:", img.mode)

filtered_img = img.convert("L")
filtered_img.save("grey.png","png")
filtered_img.show()
filtered_img.rotate(90)
filtered_img.resize((300,300))
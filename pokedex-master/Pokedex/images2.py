from PIL import Image, ImageFilter

img = Image.open("./pikachu.jpg")
filtered_img = img.convert("L")
filtered_img.save("grey3.png","png")
filtered_img.show()
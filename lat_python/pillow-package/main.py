from PIL import Image as img

pic = img.open("index.jpeg")

print(pic.format)
print(pic.size)
print(pic.mode)

pic.show()

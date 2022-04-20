from PIL import Image
import math

img_name = "basic-square.png"

inputImage = Image.open(img_name)
img = inputImage
width, height = inputImage.size
output = Image.new(mode="RGB", size=(width * 3, height * 3))

r = min(width.bit_length(), height.bit_length()) - 1

for i in range(r):
    for j in range(width, inputImage.width - width, width):
        output.paste(img, (j, height))
        output.paste(img, (j, inputImage.height - (height * 2)))

    for j in range(height, inputImage.height - height, height):
        output.paste(img, (width, j))
        output.paste(img, (inputImage.width - (width * 2), j))

    width //= 2
    height //= 2

    img.resize((width, height))

output.save("output-" + img_name)

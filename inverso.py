from PIL import Image
import os

def openimage(filename):
    return Image.open(os.path.join('input', filename))

def negative(img: Image)->Image:
    negated = Image.new(img.mode, img.size)
    w, h = negated.size
    for i in range(h):
        for j in range(w):
            if img.mode == 'RGB':
                r, g, b = img.getpixel((i, j))
                negated.putpixel((i, j), (255-r, 255-g, 255-b))
            elif img.mode == "RGBA":
                r, g, b, a = img.getpixel((i, j))
                negated.putpixel((i, j), (255-r, 255-g, 255-b, a))
            else:
                pass
    return negated

img = openimage("imagem.png")
negative(img).show()
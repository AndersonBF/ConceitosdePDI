from PIL import Image, ImageDraw, ImageFont
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

def write_text(img, text, color, textfont, fontsize, position)->Image:
   meme = img.copy()

   textfont = ImageFont.truetype(textfont, fontsize)
   
   draw = ImageDraw.Draw(meme)
   draw.text(position, text, color, font=textfont)
   return meme


img = openimage("imagem.png")
neg = negative(img)
write_text(neg, "não gostamos de python", (255, 255, 255), "arial.ttf", 40, (10, 10)).show()
negative(img).show()
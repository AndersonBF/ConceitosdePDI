from PIL import Image
from inputoutput import in_file, out_file
import os

def grayscale(colored):
    w,h = colored.size
    img = Image.new("RGB", (w,h), (0,0,0))

    for x in range(w):
        for y in range(h):
            pxl = colored.getpixel((x,y))
            #media cordenadas rgb
            lum = (pxl[0] + pxl[1] + pxl[2]) // 3
            img.putpixel((x,y), (lum, lum, lum))
    return img

def media_grayscale(colored):
    w,h = colored.size
    img = Image.new("RGB", (w,h))

    for x in range(w):
        for y in range(h):
            pxl = colored.getpixel((x,y))
            #media cordenadas rgb
            lum = int(0.3*pxl[0] + 0.59*pxl[1] + 0.11*pxl[2]) // 3
            img.putpixel((x,y), (lum, lum, lum))
    return img


if __name__ == "__main__":
    img = Image.open(in_file("imagem.png"))
    print(img.getpixel((0,0)))
    print(img.getpixel((0,1)))
    print(img.getpixel((0,2)))


    fruta = Image.open(in_file("imagem.png"))
    pb_fruta = media_grayscale(fruta)
    pb_fruta.save(out_file("imagem2.png"))

    tomate = Image.open(in_file("tomate.png"))
    pb_fruta2 = media_grayscale(tomate)
    pb_fruta2b = grayscale(tomate)
    pb_fruta2b.save(out_file("tomate2.png"))
    pb_fruta2.save(out_file("tomate.png"))

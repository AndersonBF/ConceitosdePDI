from PIL import Image, ImageFilter
import numpy as np
from inputoutput import in_file, out_file
import os

def show_horizontal(*images):
    arrays = [np.array(im) for im in images]
    im = Image.fromarray(np.hstack(arrays))
    im.show()

img = Image.open(in_file("imagem.png"))
img2 = img.filter(ImageFilter.BLUR)
#filtro de passa alta
filtered = img.filter(ImageFilter.CONTOUR)
#filtered.show()
#img.show()
show_horizontal(img, filtered, img2)

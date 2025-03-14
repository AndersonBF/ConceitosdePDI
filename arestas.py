from PIL import Image, ImageFilter
from math import sqrt
import os
from inputoutput import show_vertical, show_horizontal

INPUT_DIR = os.path.join('input')
OUTPUT_DIR = os.path.join('output')

def show_edges(filename, direction='x', offset=0):
    original = Image.open(os.path.join(INPUT_DIR, filename)).convert('L')
    
    XSOBEL = ImageFilter.Kernel(
        (3, 3),
        [-1, 0, 1,
         -2, 0, 2,
         -1, 0, 1],
        scale=1,
        offset=offset
    )
    
    YSOBEL = ImageFilter.Kernel(
        (3, 3),
        [-1, -2, -1,
          0,  0,  0,
          1,  2,  1],
        scale=1,
        offset=offset
    )
    
    if direction == 'x':
        filtered = original.filter(XSOBEL)
    elif direction == 'y':
        filtered = original.filter(YSOBEL)
    else:
        vsobel = original.filter(XSOBEL)
        hsobel = original.filter(YSOBEL)
        w, h = original.size
        filtered = Image.new('L', (w, h))
        for i in range(w):
            for j in range(h):
                value = sqrt(
                    vsobel.getpixel((i, j))**2 + hsobel.getpixel((i, j))**2
                )
                value = int(min(value, 255))
                filtered.putpixel((i, j), value)
    
    show_horizontal(original, filtered)
    filtered.save(
        os.path.join(OUTPUT_DIR, 
                     '{}_{}sobel_{}.png'.format(filename[:filename.index('.')] , direction, offset)
                  )
    )

if __name__ == "__main__":
    show_edges('imagem.png', 'a', 0)
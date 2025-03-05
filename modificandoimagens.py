from PIL import Image # type: ignore
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)
#image = Image.open(in_path("imagem.png"))
#image = Image.new("RGB", (700,700), (255,255, 0))

def triangle(size):
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    image = Image.new("RGB", (size, size), WHITE)

    for x in range(size):
        for y in range(size):
            if x < y:
                image.putpixel((x,y), BLACK)
    return image
#print(image.getpixel((0,0)))

if __name__ == "__main__":
    t = triangle(700)
    t.show()
    t.save("output/triangle.png")
    print("Imagem salva com sucesso!")

print("Fim do programa")
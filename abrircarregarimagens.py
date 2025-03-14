import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImage(image):
    
    obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)
    plt.imshow(obj_img)
    plt.show()

def main():
    obj_img = cv2.imread("input/imagem.png")
    print(obj_img.shape)
    showImage(obj_img)

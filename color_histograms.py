# Importação de bibliotecas
import cv2  
import numpy as np
from matplotlib import pyplot as plt
import argparse

# Argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="Path to the image")
args = vars(ap.parse_args())

# Carregando imagem
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
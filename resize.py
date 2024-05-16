# PÁGINA 26

# Importação de bibliotecas
import numpy as np
import argparse
import cv2
import imutils

# Argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# Redimensionando imagem
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation= cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)
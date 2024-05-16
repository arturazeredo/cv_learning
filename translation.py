# coding: utf-8

# Importação de bibliotecas
import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt
#import opencv_jupyter_ui as jcv2
import imutils # biblioteca para redimensionar imagem

# Argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="Path to the image")
args = vars(ap.parse_args())

# Carregando imagem
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Matriz de translação
M = np.float32([[1, 0, 25], [0, 1, 50]])
# Aplicando a transformação
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)
# Matriz de rotação
M = np.float32([[1, 0, -50], [0, 1, -90]])
# Aplicando a transformação
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

# Redimensionando imagem
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)
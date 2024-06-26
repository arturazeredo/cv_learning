# Importando bibliotecas

import numpy as np
import argparse
import cv2
import imutils

# Argumentos    
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
# Carregando imagem
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# Definindo centro da imagem, ponto onde a imagem será rotacionada
(h,w) = image.shape[:2]
center = (w//2, h//2)

# Matriz de rotação
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated by 45 Degrees", rotated)
# Matriz de rotação
M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = imutils.rotate(image, -90)
cv2.imshow("Rotated by -90 Degrees", rotated)
cv2.waitKey(0)

rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)
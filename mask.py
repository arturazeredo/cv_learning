# Importação de bibliotecas
import argparse
import cv2
import numpy as np
# Argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Carregando imagem
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Máscara
mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1]//2, image.shape[0]//2) # centro da imagem
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1) #  criando um retângulo
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked applied to image", masked)
cv2.waitKey(0)

# Máscara circular
mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.circle(mask, (cX, cY), 100, 255, -1) # criando um circulo com raio 100 e concreto
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Applied to image", masked)
cv2.waitKey(0)



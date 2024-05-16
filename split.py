# Importando bibliotecas
import numpy as np
import argparse
import cv2
# Argumentos
ap= argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Carregando imagem
image = cv2.imread("image-test.jpg") 
(B, G, R)= cv2.split(image) # Dividindo imagem em canais
# Imagem Splitada
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()


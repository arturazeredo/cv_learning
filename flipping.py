# Importação de bibliotecas
import argparse
import cv2

# Argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
# Carregando imagem
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# Flipping imagem
flipped = cv2.flip(image, 1) # 1 = horizontal, 0 = vertical, -1 = both
cv2.imshow("Flipped Horizontally", flipped)

flipped = cv2.flip(image, 0) # 1 = horizontal, 0 = vertical, -1 = both
cv2.imshow("Flipped Vertically", flipped)

flipped = cv2.flip(image, -1) # 1 = horizontal, 0 = vertical, -1 = both
cv2.imshow("Flipped Horizontally and Vertically", flipped)

cv2.waitKey(0)


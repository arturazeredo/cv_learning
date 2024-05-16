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
# Corte
cropped = image[30:120, 240:335] # y1:y2, x1:x2
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
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

# Máscara
mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1]//2, image.shape[0]//2) # centro da imagem
cv2.rectangle(mask, (cx - 75, cy - 75), (cx + 75, cy + 75), 255, -1) #  criando um retângulo
cv2.imshow("Mask", mask)
# Máscara aplicada
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked applied to image", masked)
cv2.waitKey(0')

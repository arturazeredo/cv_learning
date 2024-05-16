from __future__ import print_function
import numpy as np
import argparse 
import cv2

# Argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# Aviso de que o valor está entre 0 e 255
print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))
# Aviso de arrendondamento
print("Wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
print("Wrap around: {}".format(np.uint8([50]) - np.uint8([100])))
# Adicionando Pixels
M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)
# Subtraindo Pixels
M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)
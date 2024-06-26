# Importação de bibliotecas
import numpy as np
import cv2
# Retângulo
rectangle = np.zeros((300, 300), dtype = "uint8")
cv2.rectangle(rectangle, (25,25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)
# Operações binárias
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseAnd)   
cv2.waitKey(0) 

bitwiseOr = cv2.bitwise_not(rectangle, circle)
cv2.imshow("NOT", bitwiseAnd)
cv2.waitKey(0)
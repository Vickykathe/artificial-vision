# -*- coding: utf-8 -*-
"""

Created on Tue Nov  3 10:50:01 2020
@author: Katherine Vela
"""

import cv2 #OpenCV
import numpy as np
import matplotlib.pyplot as plt

# :::::: OUR IMAGES ::::::

img2 = cv2.imread('images/A.jpg')
img1 = cv2.imread('images/B.jpg')


# 1.Visualizar las imágenes de entrada en Escala de Grises.
U = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
D = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# 3.Obtener el Umbral de cada imagen 
umbralA,_ = cv2.threshold(U,0,255,cv2.THRESH_OTSU)
umbralB,_ = cv2.threshold(D,0,255,cv2.THRESH_OTSU)

#2.Visualizar las imágenes de entrada en formato Binario.
mascaraA = np.uint8((U<umbralA)+255)
mascaraB = np.uint8((D<umbralB)+255)


#5.Obtenga el argumento mínimo de cada imagen
minimoA = np.min(img1)
minimoB = np.min(img2)
# Obtener el valor mínimo de cada imagen1.
pxX = np.size(img1, axis=1) #W
pxY = np.size(img1, axis=0) #H
pxXY = np.size(img1, axis=None)
# Obtener el valor mínimo de cada imagen2.
pxX = np.size(img1, axis=1) #W
pxY = np.size(img1, axis=0) #H
pxXY = np.size(img1, axis=None)
#================================================
#6.Obtenga el argumento maxímo de cada imagen
maximoA = np.max(img1)
maximoB = np.max(img2)
#Obtener el valor (px) máximo de cada imagen 1.
pxX = np.size(img1, axis=0) #W
pxY = np.size(img1, axis=1) #H

#. Obtener la suma (px) resultante en cada imagen.
pxXY = np.size(img1, axis=None)
#Obtener el valor (px) máximo de cada imagen 2.
pxX = np.size(img2, axis=0) #W
pxY = np.size(img2, axis=1) #H
#. Obtener la suma (px) resultante en cada imagen.
pxXY = np.size(img2, axis=None)
#======================================================

#Obtener la suma  resultante en cada imagen.
sumaA = np.sum(img1)
sumaB = np.sum(img2)
#7.Obtener el promedio de cada imagen
promA = np.mean(img1)
promB = np.mean(img2)
#8.Obtenga la varianza de cada imagen.
varA = np.var(img1)
varB = np.var(img2)
#9.Obtenga la Desviación Estándar de cada imagen.
desA = np.sqrt(varA)
desB = np.sqrt(varB)

#10.Obtenga el histograma de cada imagen en Escala de Grises
dataA = U.flatten()
plt.hist(dataA, bins = 100)
dataB = D.flatten()
plt.hist(dataB, bins = 100)

#11.Obtenga el histograma de cada imagen discriminado por cada componente RGB 1.
data = U.flatten()
red = img1[:,:,0].flatten()
green = img1[:,:,1].flatten()
blue = img1[:,:,2].flatten()
plt.hist(red, bins=1000, histtype="stepfilled", color="red")
plt.hist(green, bins=1000, histtype="stepfilled", color="green")
plt.hist(blue, bins=1000, histtype="stepfilled", color="blue")
#Obtenga el histograma de cada imagen discriminado por cada componente RGB 2.
data = D.flatten()
red = img2[:,:,0].flatten()
green = img2[:,:,1].flatten()
blue = img2[:,:,2].flatten()
plt.hist(red, bins=1000, histtype="stepfilled", color="red")
plt.hist(green, bins=1000, histtype="stepfilled", color="green")
plt.hist(blue, bins=1000, histtype="stepfilled", color="blue")


# Obtenga la cantidad de objetos de cada imagen.

outputA = cv2.connectedComponentsWithStats(mascaraA,0,cv2.CV_32F)
cantObjA = outputA[0] # Objects quantity
outputB = cv2.connectedComponentsWithStats(mascaraB,0,cv2.CV_32F)
cantObjB = outputB[0] # Objects quantity



#Sume las imágenes A y B, y obtenga la imagen resultante.
imgresult = cv2.add(img1,img2)

#imshow
cv2.imshow("Suma de las imagenes",imgresult)

cv2.waitKey(0)
cv2.destroyAllWindows()
#Develoer: katherine vela
#Script: Number race

#libraries
import os
import sys
import time
from random import randint
plys=[]
dados=[]
puntos=[]
#----------------------------------------------------
 
print("----------------------------------¡Bienvenidos!-------------------------------------")
jugadores = int(input("Digite la cantidad de jugadores entre 2 y 5: "))
while jugadores<=1 or jugadores>=6:
    print("ERROR -> Ingrese un numero entre 2 y 5")
    jugadores = int(input("Digite la cantidad de jugadores: "))

   
#-------------------------------Nivel---------------------------
print("Por favor, seleccione el nivel que desea jugar")
print("[1]. Suma 50 para ganar")
print("[2]. Suma 70 para ganar")
print("[3]. Suma 100 para ganar")
print ("[4].Salir")
op = int(input("Digite Nivel de juego: "))
while op<0 or op>=5:
    print("ERROR -> Ingrese un valor correcto: ")
    op = int(input("Digite Nivel de juego: "))
if op == 1:
  nivel = 50
elif op == 2:
  nivel = 70
elif op == 3:
  nivel = 100
elif op == 4:
        salir = True
else:
        print ("Introduce un numero entre 1 y 4")    
#----------------------------- logica juego ------------------
print("******************************(QUE EMPIECE EL JUEGO)**************************************************")
i=1
while i <= jugadores:
  plys.append(i)
  puntos.append(randint(1,12))
  i = i+1

x = len(puntos)

meta =0
j=0
while j < x:  
  meta = int(puntos[j])+randint(1,12)
  puntos[j] = meta
  meta = 0
  print(puntos)
  j = j+1
num_max=max(puntos)
num_min=min(puntos)
pos_max=puntos.index(max(puntos))
pos_min=puntos.index(min(puntos))
print("*****************************RESULTADO*****************************************************************")
print("Nivel del Juego: ", nivel)
print("jugadores: ",x)
print("Total de puntos: ",puntos)
print("El jugador ganador es: ",pos_max+1, " y su puntaje fue: ",num_max, "Puntos")

#-----------------------------------------------------------------------
print("**********************************************************************************************")
print("****Desarrollado por Victoria Katherine Vela********")
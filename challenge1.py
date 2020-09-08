#Develoer: katherine vela
#Script: Number race

#libraries
import os
import time
from random import randint

py1 = 0
py2 = 0

os.system("cls")

print("[1]. Add 50 to win")
print("[2]. Add 70 to win")
print("[3]. Add 100 to win")
print("please, enter any option")
op = input()

if op == '1':
  while py1<50 or py2<50:    
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    py1 = py1+dice1+dice2
    print("Player 1, your score is: ",py1)
    
    
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    py2 = py2+dice1+dice2
    print("Player 2, your score is: ",py2)    
    time.sleep(1)

    if py1>=50 and py2>=50:
      time.sleep(2)
      print("both reached the goal, It's a draw!!")
      break
    elif py1>=50:
      time.sleep(2)
      print("Player1, You won!!\nYou reach: ",py1," points")
      break
    elif py2>=50:
      time.sleep(2)
      print("Player2, You won!!\nYou reach: ",py2," points")
      break  

elif op == '2':
  while py1<70 or py2<70:    
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    py1 = py1+dice1+dice2
    print("Player 1, your score is: ",py1)
    
    
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    py2 = py2+dice1+dice2
    print("Player 2, your score is: ",py2)    
    time.sleep(1)

    if py1>=70 and py2>=70:
      time.sleep(2)
      print("both reached the goal, It's a draw!!")
      break
    elif py1>=70:
      time.sleep(2)
      print("Player1, You won!!\nYou reach: ",py1," points")
      break
    elif py2>=70:
      time.sleep(2)
      print("Player2, You won!!\nYou reach: ",py2," points")
      break  

elif op == '3':
  while py1<100 or py2<100:    
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    py1 = py1+dice1+dice2
    print("Player 1, your score is: ",py1)
    
    
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    py2 = py2+dice1+dice2
    print("Player 2, your score is: ",py2)    
    time.sleep(1)

    if py1>=100 and py2>=100:
      time.sleep(2)
      print("both reached the goal, It's a draw!!")
      break
    elif py1>=100:
      time.sleep(2)
      print("Player1, You won!!\nYou reach: ",py1," points")
      break
    elif py2>=100:
      time.sleep(2)
      print("Player2, You won!!\nYou reach: ",py2," points")
      break  

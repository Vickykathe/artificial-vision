#Developer: Kathe Vela
#Script: this program let us to generate one random numbers.
#randint => Generates Z numbers.
#uniform => Generates R numbers.
#libraries
import os
from random import randint, uniform

# functions
dice1 = randint(1,6)
dice2 = randint(1,6)

print("Enter first number: ")
x = int(input())
y = int(input("Enter second number: ")) 

print("[1]. 10")
print("[2]. 50")
print("[3]. 100")
print("Please, enter any option (1-3): ")
op = input()

if op == '1' :
    print("10 is: ", )
elif op == '2' :
    print("50 is: ", x - y)
elif op == '3' :
    print("100 is: ", x * y)

else :
    print("::: Invalid option :::")  

def number_list() :
    i = 1
    while i <= 6:
        x =randint(1,100)
        print(x)
        i=i+1

#main
os.system("cls")
print("", dice1)
print("", dice2)
print("::::::::::::::::::::::::::::::")
number_list()


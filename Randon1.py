#Developer: Kathe Vela
#Script: this program let us to generate one random numbers.
#randint => Generates Z numbers.
#uniform => Generates R numbers.
#libraries
import os
from random import randint, uniform

# functions
def rand_integer() :
    nz = randint(1,10)
    return nz

def rand_real():
    nr =uniform(1,10)
    return nr
def number_list() :
    i = 1
    while i <= 10:
        x =randint(1,100)
        print(x)
        i=i+1
#main
os.system("cls")
z = rand_integer()
print("The Z number generated is :",z)
r = rand_real()
print("The R number generated is :",r )
print("::::::::::::::::::::::::::::::")
number_list()



#main
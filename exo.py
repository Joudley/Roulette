import random
import sys

x = random.randint(0,500)
nbr_fwa  = 4
nmbr = input ("Antre yn vale nan enteval 0 a 500 :   ")
if nmbr.isdigit:
    while nbr_fwa >0:
        if int(nmbr)== x:
            print("Bravo. Ou jwenn bon nonb lan ")
            break
        else:
            if int(nmbr) >x:
                print ("Nonb lan tro gro ")
            else:
                print("Nonb lan tro piti ")
            nmbr = input("Antre yn lot nonb :   ")
            nbr_fwa -=1
            print("Ou rete", nbr_fwa,"fwa pouw eseye")
else :
    print("Se pa yon nombre")

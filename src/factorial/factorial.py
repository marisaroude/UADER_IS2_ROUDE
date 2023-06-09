#* calcula el factorial de un nÃºmero                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

import sys

def factorial(num): 
    if num < 0 : 
        print("Factorial de un nÃºmero negativo no existe")

    elif num == 0 : 
        return 1
        
    else: 
        fact = 1
        while(num > 1 ): 
            fact *= num
            num -= 1
        return fact


if len(sys.argv) == 1:
   min = int(input("Debe ingresar el numero minimo del rango: ")) 
else:
    min = int(sys.argv[1])
   #sys.exit()

#El for realiza los factoriales para cada número del rango definido.
for i in range (min,60+1):
    print("Factorial del nro",i, " es: ", factorial(i))
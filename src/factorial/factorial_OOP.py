import sys

class Factorial:
    def __init__(self):
        pass

    def calcular_factorial(self,num):
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


    def run(self,min,max):
        for i in range (min,max+1):
            print("Factorial del nro",i, " es: ", self.calcular_factorial(i))



#Creamos una instancia:
f = Factorial()

if len(sys.argv) == 1: ##Esto quiere decir que no se ingreso un numero, acto seguido se solicita x consola el ingreso
        min = int(input("Ingrese el valor mínimo: "))
        max = int(input("Ingrese el valor máximo: ")) 
else: 
        min = int(sys.argv[1])
        max = int(sys.argv[2]) 
     #sys.exit()

#Llamamos al metodo:
f.run(min,max)
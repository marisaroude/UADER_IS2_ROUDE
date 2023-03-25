import sys

class Factorial:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    
    def run(self,num):
        if num < 0: 
            print("Factorial de un numero negativo no existe")
        elif num == 0: 
            return 1        
        else: 
            while (num < self.min or num > self.max):
                num = int(input(f"Debe ingresar un número dentro del rango: [{self.min},{self.max}]: ")) 
            else: 
                while (num >= self.min and num <= self.max): # Modifia el rango 
                    fact = 1
                    while(num >= self.max): 
                        fact *= num 
                        num -= 1
                    return fact



#Creamos una instancia:
f = Factorial(2,5)

if len(sys.argv) == 1: ##Esto quiere decir que no se ingreso un numero, acto seguido se solicita x consola el ingreso
        num = int(input(f"Deebe ingresar un número dentro del rango")) 
else: 
        num = int(sys.argv[1])  
     #sys.exit()

#Llamamos al metodo:
print("Factorial del nro",num, " es: ", f.run(num)) 
import sys

def factorial(num1, num2): 
    if num1 < 0 or num2 < 0: 
        print("Factorial de un nÃºmero negativo no existe")

    elif num1 == 0 and num2 == 0: 
        return 1
        
    else: 
        fact = 1
        while(num2 > 1): 
            fact *= num2
            num2 -= 1
        return fact 

if len(sys.argv) == 1:
   num1 = int(input("Debe ingresar un número: ")) 
   num2 = int(input("Debe ingresar un número: ")) 
else:
    num = int(sys.argv[1])
   #sys.exit()



for i in range (num1, num2):
    print("Factorial del nro",i, " es: ", factorial(i))
#print("Factorial ",num,"! es ", factorial(num)) 
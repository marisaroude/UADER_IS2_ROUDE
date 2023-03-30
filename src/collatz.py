import sys
import matplotlib.pyplot as plt

def collatz(n): 
    x = n # Asignamos el valor de n a la variable x ya que x es el valor ingresado entre 1 y 10000
    resultado = [n] #Guardamos el primer valor ingresado por consola 
    while (n > 1):
            if n % 2 == 0 : #Cálculo para saber si n es apr 
                n = (n//2) # si n es par lo divide entre dos y le asigna el valor
            else:
                n = (n *3) + 1 #sino, si es impar lo multiplica por 3 y suma uno
            resultado.append(n) #luego almacena el valor en n y así sucesivamente mientras que n > 1
    y = len(resultado) # Asignamos el tamaño de resultado a la variable y ya que y es la cantidad de ietraciones.
    print(resultado)
    return x, y, resultado # Retornamos los valores de x e y como una tupla



#if len(sys.argv) == 1:
#   n = int(input("Debe ingresar un numero entre 1 y 10000: ")) 
#else:
#    n = int(sys.argv[1])
   #sys.exit()        


#Llamamos a la función asignando los valores x,y y resultado que nos retorna la func
valores_x = []
valores_y = []
for i in range (1,10001):
    x,y,resultado = collatz(i)
    valores_x.append(x)
    valores_y.append(y)
    print("el numero de iteraciones para ", x,' es ',y)    
    print()
   


# Configuramos el gráfico
#Mostramos los valores de x e y
plt.plot(valores_x,valores_y,'.')
plt.ylabel('Iteraciones')
plt.xlabel('Número de inicio')
plt.title('Conjetura de Collatz')
    
plt.show()


   
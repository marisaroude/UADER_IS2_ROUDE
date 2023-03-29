import sys
import matplotlib.pyplot as plt

def collatz(n): 
    x = n # Asignamos el valor de n a la variable x ya que x es el valor ingresado entre 1 y 10000

    resultado = [n] #Guardamos el primer valor ingresado por consola 
    if (n >=1 and n <= 10000): #Si el número está entre 1 y 10000 que calcule la conjetura
        while (n > 1):
            if n % 2 == 0 : #Cálculo para saber si n es apr 
                n = (n//2) # si n es par lo divide entre dos y le asigna el valor
            else:
                n = (n *3) + 1 #sino, si es impar lo multiplica por 3 y suma uno
            resultado.append(n) #luego almacena el valor en n y así sucesivamente mientras que n > 1
        y = len(resultado) # Asignamos el tamaño de resultado a la variable y ya que y es la cantidad de ietraciones.
        print(resultado)
        return x, y, resultado # Retornamos los valores de x e y como una tupla
    else: #Si el número no está entre 1 y 10000 que lo vuelva a solicitar
         n = int(input("Debe ingresar un numero entre 1 y 10000: ")) 
         return collatz(n)


if len(sys.argv) == 1:
   n = int(input("Debe ingresar un numero entre 1 y 10000: ")) 
else:
    n = int(sys.argv[1])
   #sys.exit()        


#Llamamos a la función asignando los valores x,y y resultado que nos retorna la func
x,y,resultado = collatz(n)

#Mostramos los valores de x e y
print("valor de x: ",x)
print("valor de y: ",y)

# Configuramos el gráfico
fig, ax = plt.subplots() 
ax.scatter(y, x)
ax.set_xlabel('Iteraciones')
ax.set_ylabel('Número de inicio')
ax.set_title('Conjetura de Collatz')

# Muestra primero el gráfico, para que nos traiga los valores por consola debemos cerrar el gràfico.
plt.show()



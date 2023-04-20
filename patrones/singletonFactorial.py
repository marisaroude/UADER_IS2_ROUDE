#!/usr/python
#*--------------------------------------------------
#* singleton.py
#* excerpt from https://refactoring.guru/design-patterns/singleton/python/example
#*--------------------------------------------------
class SingletonMeta(type): #constructor de nivel sueprior
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}  #se define la instancia
    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances: # si la instancia está vacia significa q es la primera vez q se lo llama
            instance = super().__call__(*args, **kwargs) #llama al super constructor
            cls._instances[cls] = instance 
        return cls._instances[cls]


class Factorial(metaclass=SingletonMeta):
#    def some_business_logic(self):
#        """
#        Finally, any singleton should define some business logic, which can be
#        executed on its instance.
#        """
#
#
    def getFactorial(self,num):
        if num < 0:
            print("Factorial de un numero negativo no existe")    
        elif num == 0:
            return 1 
        else:
            fact = 1
            while (num > 1):
                fact *= num
                num -=1
            return fact



if __name__ == "__main__":
    # The client code.

    s1 = Factorial() #Creo un objeto
    s2 = Factorial() #Creo el segundo
    num = 5
    if id(s1) == id(s2): #si son la misma instancia ingresa en el if
        print(s1) #hago un print de ambos objetos para visualizar que sean iguales.
        print(s2)
        print ("Factorial de ",num, s1.getFactorial(num))
    else:
        print("Singleton failed, variables contain different instances.")


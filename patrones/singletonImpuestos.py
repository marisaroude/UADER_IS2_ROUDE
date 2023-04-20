#!/usr/python
#*--------------------------------------------------
#* singleton.py
#* excerpt from https://refactoring.guru/design-patterns/singleton/python/example
#*--------------------------------------------------
from email.mime import base


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


class Impuestos(metaclass=SingletonMeta):
#    def some_business_logic(self):
#        """
#        Finally, any singleton should define some business logic, which can be
#        executed on its instance.
#        """
#
#
    
    def getIVA(self):
        return "21%"

    def getIIBB(self):
        return "5%"

    def getContribucionesMunicipales(self):
        return "1,2%"

    


if __name__ == "__main__":
    # The client code.

    s1 = Impuestos() #Creo un objeto
    s2 = Impuestos() #Creo el segundo
    
    if id(s1) == id(s2): #si son la misma instancia ingresa en el if
        base_imponible = input("Ingrese un valor: ")
        print('Base imponible: ',base_imponible)
        print('Cálculo sobre la base imponible según IVA: ',base_imponible, ' + ' ,s1.getIVA())
        print('Cálculo sobre la base imponible según IIBB: ',base_imponible, ' + ' ,s1.getIIBB())
        print('Cálculo sobre la base imponible según Contribuciones Municipales: ',base_imponible, ' + ' ,s1.getContribucionesMunicipales())
    else:
        print("Singleton failed, variables contain different instances.")



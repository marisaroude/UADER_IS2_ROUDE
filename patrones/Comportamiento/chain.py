#!/usr/python
#*--------------------------------------------------
#* chain.py
#* Patron chain of command
#* excerpt from https://refactoring.guru/design-patterns
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

def es_primo(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

class Handler(ABC):
    """
    La interfaz de controlador declara un método para construir la cadena
    de controladores. 
    También declara un método para ejecutar una solicitud.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    
    El comportamiento de encadenamiento predeterminado 
    se puede implementar dentro de una clase de controlador base.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler       
        # Devolver un controlador desde aquí nos permitirá vincular controladores en un
        # manera conveniente como esta:
        # mono.set_next(ardilla).set_next(perro)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

   
    
"""
Todos los manipuladores de hormigón gestionan una solicitud o la pasan al siguiente manipulador en
La cadena.
"""


class NumeroPar (AbstractHandler):
    def handle(self,request:Any) -> str:
        if request % 2 == 0:
            return f"Número par: Lo tomo --> {request}" 
        else:
            return super().handle(request)


class NumeroPrimo(AbstractHandler):
    def handle(self, request: int) -> str:
        if es_primo(request):
            return f"Número primo: Lo tomo --> {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    El código del cliente suele ser adecuado para trabajar con un solo 
    controlador. 
    En la mayoría de los casos, ni siquiera es consciente de que el 
    manipulador forma parte de una cadena.
    """

    for numero in range(1,101):
        print(f"\nClient: Quien quiere el nro {numero}?")
        result = handler.handle(numero)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {numero} se ha dejado intacto.", end="")


if __name__ == "__main__":

    pares = NumeroPar()
    primos = NumeroPrimo()

    pares.set_next(primos)

    client_code(pares)
    print("\n")


from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from random import random   
from typing import List

"""Implemente una clase bajo el patrón observer donde una serie de clases 
están subscriptas, cada clase espera que su propio ID 
(una secuencia arbitraria de 4 caracteres) sea expuesta y emitirá un 
mensaje cuando el ID emitido y el propio coinciden. Implemente 4 clases
de tal manera que cada una tenga un ID especifico. 
Emita 8 ID asegurándose que al menos cuatro de ellos coincidan con
ID para el que tenga una clase implementada"""
class Subject(ABC):
    """
    La interfaz Asunto declara un conjunto de métodos para administrar suscriptores.    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Adjunte un observador al sujeto.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Separe a un observador del sujeto.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notifica a todos los observadores sobre un evento
        """
        pass


class ConcreteSubject(Subject):
    """
    El Sujeto posee algún estado importante y notifica a los 
    observadores cuando el estado cambio.
    """

    _state: int = None
    """
    En aras de la simplicidad, el estado del Asunto, 
    esencial para todos los suscriptores, se almacena en esta variable.
    """

    _observers: List[Observer] = []
    """
    Lista de suscriptores. En la vida real, la lista de suscriptores se puede almacenar
    de forma más completa (categorizados por tipo de evento, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Sujeto: +1 suscripción.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    Los métodos de gestión de suscripciones.    
    """

    def notify(self) -> None:
        """
        Activar una actualización en cada suscriptor.
        """

        print("Sujeto: Notificación a los observadores ...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self,id) -> None:
        """
        Por lo general, la lógica de suscripción es solo una fracción
        de lo que realmente puede hacer un Sujeto. 
        Los sujetos suelen tener una lógica comercial importante, 
        que activa un método de notificación cada vez que algo importante 
        está a punto de suceder (o después).
        """

        print("Sujeto: Estoy haciendo algo importante.")
        #self._state = str(randrange(1000, 9999))
        self._state = id
        print(f"Sujeto: Mi estado acaba de cambiar a: {self._state}")
        self.notify()


class Observer(ABC):
    """
    La interfaz de Observer declara el método de actualización, 
    utilizado por los sujetos.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Recibir actualización del sujeto.

        """
        pass


"""
Los Observadores Concretos reaccionan a las actualizaciones emitidas por el Sujeto que les había sido
adjunto a.
"""


class Suscriptor1(Observer):
    def __init__(self, s_1):
        self.s_1 = s_1

    def getId1(self) -> str:
        return self.s_1

    def update(self, subject: Subject) -> None:
        if subject._state == self.getId1():
            print(f"Suscriptor1 (ID: {self.s_1}): Reaccionó al evento")


class Suscriptor2(Observer):
    def __init__(self, s_2):
        self.s_2 = s_2

    def getId1(self) -> str:
        return self.s_2

    def update(self, subject: Subject) -> None:
        if subject._state == self.getId1():
            print(f"Suscriptor2 (ID: {self.s_2}): Reaccionó al evento")


class Suscriptor3(Observer):
    def __init__(self, s_3):
        self.s_3 = s_3

    def getId1(self) -> str:
        return self.s_3

    def update(self, subject: Subject) -> None:
        if subject._state == self.getId1():
            print(f"Suscriptor3 (ID: {self.s_3}): Reaccionó al evento")


class Suscriptor4(Observer):
    def __init__(self, s_4):
        self.s_4 = s_4

    def getId1(self) -> str:
        return self.s_4

    def update(self, subject: Subject) -> None:
        if subject._state == self.getId1():
            print(f"Suscriptor4 (ID: {self.s_4}): Reaccionó al evento")

if __name__ == "__main__":
    # The client code.
    subject = ConcreteSubject()
    #ID de los suscriptores:
    s_1 = '1234'
    s_2 = '5678'
    s_3 = '9123'
    s_4 = '4567'

    #ID que emitirá el Sujeto:
    id_1 = '1234'
    id_2 = '1122'
    id_3 = '9123'
    id_4 = '9123'
    id_5 = '3344'
    id_6 = '9991'
    id_7 = '4567'
    id_8 = '6571'

    #Agrego a los suscriptores
    observer_a = Suscriptor1(s_1)
    subject.attach(observer_a)

    observer_b = Suscriptor2(s_2)
    subject.attach(observer_b)

    observer_c = Suscriptor3(s_3)
    subject.attach(observer_c)

    observer_d = Suscriptor4(s_4)
    subject.attach(observer_d)

    #Realizo las llamadas a las reglas de negocio
    subject.some_business_logic(id_1)
    subject.some_business_logic(id_2)
    subject.some_business_logic(id_3)
    subject.some_business_logic(id_4)
    subject.some_business_logic(id_5)
    subject.some_business_logic(id_6)
    subject.some_business_logic(id_7)
    subject.some_business_logic(id_8)


    #Borro un suscriptor
    subject.detach(observer_a)

    #Realizo una llamada a su ID para chequear si responde...
    subject.some_business_logic(id_1)


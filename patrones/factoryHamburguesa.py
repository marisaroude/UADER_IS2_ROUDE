#!/usr/bin/python3.7
#*--------------------------------------------------
#* factory.py
#* excerpt from https://refactoring.guru/design-patterns/factory/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    #Aquí estamos creando la hamburguesa
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    #Este es el metodo de entrega.
    def metodo_entrega(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        hamburguesa = self.metodo_entrega()

        # Now, use the product.
        result = f"Método de entrega para el producto Hamburguesa: {hamburguesa.operation()}\n"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class CreatorEntregaMostrador(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """
    def metodo_entrega(self) -> Hamburguesa:
        return EntregaMostrador()


class CreatorRetiradaPorCliente(Creator):
    def metodo_entrega(self) -> Hamburguesa:
        return RetiradaPorCliente()

class CreatorEnvioDelivery(Creator):
    def metodo_entrega(self) -> Hamburguesa:
        return EnvioDelivery()

class Hamburguesa(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class EntregaMostrador(Hamburguesa):
    def operation(self) -> str:
        return "{Entregada en mostrador}"


class RetiradaPorCliente(Hamburguesa):
    def operation(self) -> str:
        return "{Retirada por cliente}"

class EnvioDelivery(Hamburguesa):
    def operation(self) -> str:
        return "{Envío por delivery}"


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long ascreator.some_operation() the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """
    print(f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    while True:
        metodo = input("Ingrese el metodo de entrega para la hamburguesa (mostrador/retiro/delivery): ")
        if metodo == 'mostrador':
            client_code(CreatorEntregaMostrador())
            break
        elif metodo == 'retiro':   
            client_code(CreatorRetiradaPorCliente())
            break
        elif metodo == 'delivery': 
            client_code(CreatorEnvioDelivery())
            break
        else:
            print('Debe ingresar un metodo correcto')
        
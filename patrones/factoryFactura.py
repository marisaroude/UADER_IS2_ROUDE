#!/usr/bin/python3.7
#*--------------------------------------------------
#* factory.py
#* excerpt from https://refactoring.guru/design-patterns/factory/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod
#clase factura atributo inpuesto

class Creator(ABC):
    #Aquí estamos creando la factura
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    
    def tipo_factura(self):
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
        factura = self.tipo_factura()

        # Now, use the product.
        result = f"Creando una factura de tipo {factura.operation()}\n  "

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class CreatorIVAResponable(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """
    def tipo_factura(self) -> Factura:
        return IVAResponsable()


class CreatorIVANoInscripto(Creator):
    def tipo_factura(self) -> Factura:
        return IVANoInscripto()

class CreatorIVAExento(Creator):
    def tipo_factura(self) -> Factura:
        return IVAExento()

class Factura(ABC):
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


class IVAResponsable(Factura):
    def operation(self) -> str:
        return "{IVA Responsable, impuesto 21%}"


class IVANoInscripto(Factura):
    def operation(self) -> str:
        return "{IVA No Inscripto, impuesto 10%}"

class IVAExento(Factura):
    def operation(self) -> str:
        return "{IVA Exento, impuesto 20%}"


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long ascreator.some_operation() the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """
    print(f"Factura. Importe total = $10.000.\n"
          f"{creator.some_operation()}", end="")



if __name__ == "__main__":
    while True:
        metodo = input("Ingrese el tipo de factura a imprimir (iva responsable /iva no inscripto /iva exento): ")
        if metodo == 'iva responsable':
            client_code(CreatorIVAResponable())
            break
        elif metodo == 'iva no inscripto':   
            client_code(CreatorIVANoInscripto())
            break
        elif metodo == 'iva exento': 
            client_code(CreatorIVAExento())
            break
        else:
            print('Debe ingresar un tipo de factura correcta')
        
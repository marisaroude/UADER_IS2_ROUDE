from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


"""Represente la lista de piezas componentes de un ensamblado con sus
relaciones jerárquicas. Empiece con un producto principal formado por tres
sub-conjuntos los que a su vez tendrán cuatro piezas cada uno. Genere clases
que representen esa configuración y la muestren. 
Luego agregue un subconjunto opcional adicional también formado por cuatro piezas. (Use el patrón
composite)."""

class Component(ABC):
    """
    La clase de Componente base declara operaciones comunes para ambos, simple y
    objetos complejos de una composición.
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Opcionalmente, el Componente base puede declarar una interfaz para configurar y
        acceder a un padre del componente en una estructura de árbol. También puede
        proporcionar alguna implementación predeterminada para estos métodos.
        """

        self._parent = parent

    """
    En algunos casos, sería beneficioso definir la gestión de niños
    operaciones directamente en la clase de componente base. De esta manera, no necesitarás
    exponer cualquier clase de componente concreto al código del cliente, incluso durante el
    ensamblaje del árbol de objetos. La desventaja es que estos métodos estarán vacíos para
    los componentes a nivel de hoja.

    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        Puede proporcionar un método que permita que el código del cliente determine si un
        componente puede tener hijos.
        """

        return False

    @abstractmethod
    def operation(self) -> str:
        """
        El Componente base puede implementar algún comportamiento predeterminado o dejarlo
        clases concretas (declarando el método que contiene el comportamiento como
        "abstracto").
        """

        pass


class Pieza(Component):
    """
    La clase Pieza representa los objetos finales de una composición. una hoja no puede
    tener hijos.

    Por lo general, son los objetos Pieza los que hacen el trabajo real, mientras que Composite
    los objetos solo delegan a sus subcomponentes.
    """

    def operation(self) -> str:
        return "Pieza"

  

class Composite(Component):
    """
    La clase Composite representa los componentes complejos que pueden tener
    niños. Por lo general, los objetos compuestos delegan el trabajo real a sus
    niños y luego "resumir" el resultado.
    """

    def __init__(self) -> None:
        self._children: List[Component] = []

    """
    Un objeto compuesto puede agregar o quitar otros componentes (tanto simples como
    complejo) hacia o desde su lista secundaria.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        El Composite ejecuta su lógica primaria de una manera particular. Él
        atraviesa recursivamente a través de todos sus hijos, recopilando y sumando
        sus resultados Dado que los hijos del compuesto pasan estas llamadas a sus
        niños, etc., todo el árbol de objetos se recorre como resultado.
        """
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Producto({'+'.join(results)})"


def client_code(component: Component) -> None:
    """
   El código de cliente funciona con todos los componentes a través de la interfaz base.
    """

    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1: Component, component2: Component) -> None:
    """
    Gracias a que las operaciones de child-management están declaradas en el
    clase de componente base, el código del cliente puede funcionar con cualquier componente, simple o
    complejos, sin depender de sus clases concretas.
    """

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":

    print("Creo el arbol con la prama principal")
    tree = Composite()
    client_code(tree)
    print("\n")

    print("Creo la primer rama con sus 4 hojas")
    branch1 = Composite()
    branch1.add(Pieza())
    branch1.add(Pieza())
    branch1.add(Pieza())
    branch1.add(Pieza())
    client_code(branch1)
    print("\n")

    print("Creo la primer rama con sus 4 hojas")
    branch2 = Composite()
    branch2.add(Pieza())
    branch2.add(Pieza())
    branch2.add(Pieza())
    branch2.add(Pieza())
    client_code(branch2)
    print("\n")

    print("Creo la primer rama con sus 4 hojas")
    branch3 = Composite()
    branch3.add(Pieza())
    branch3.add(Pieza())
    branch3.add(Pieza())
    branch3.add(Pieza())
    client_code(branch3)
    print("\n")


    tree.add(branch1)
    tree.add(branch2)
    tree.add(branch3)

    print("Cliente: Ahora tengo un árbol compuesto:")
    client_code(tree)
    print("\n")

    print("Agregamos una rama más con 4 hojas")
    branch4 = Composite()
    branch4.add(Pieza())
    branch4.add(Pieza())
    branch4.add(Pieza())
    branch4.add(Pieza())
    client_code(branch4)
    tree.add(branch4)
    print("\n")
    print("Cliente: Ahora tengo un árbol compuesto con una rama más:")
    client_code(tree)



#*--------------------------------------------------
#* decorator.py
#* excerpt from https://refactoring.guru/design-patterns/decorator/python/example
#*--------------------------------------------------

class Component():
    """
    La interfaz de componente base define operaciones que pueden ser modificadas por
    decoradores
    """

    def operation(self) -> str:
        pass


#Inicializamos la clase Numero con su respectivo init y su operación que en este caso lo que realiza es retornar el número asignado.

class Number(Component):
    """
    Los componentes concretos proporcionan implementaciones predeterminadas de las operaciones. Allá
    puede haber varias variaciones de estas clases.
    """

    def __init__(self, number: int) -> None:
        self._number = number

    def operation(self) -> str:
        return str(self._number)



class Decorator(Component):
    """
    
    La clase Decorator base sigue la misma interfaz que los otros componentes.
    El propósito principal de esta clase es definir la interfaz de envoltura para
    todos los decoradores de hormigón. La implementación predeterminada del código de envoltura.
    podría incluir un campo para almacenar un componente envuelto y los medios para
    inicializarlo.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        """
        El decorador delega todo el trabajo al componente envuelto.
        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()


#Creamos las clases decoradoras.

class DecoratorSuma(Decorator):
    """
    
    Los Decoradores de Concreto llaman al objeto envuelto y alteran su resultado en algunos
    forma.
    """

    def operation(self) -> str:
        """
        Los decoradores pueden llamar a la implementación principal de la operación, en lugar de
        llamando directamente al objeto envuelto. Este enfoque simplifica la extensión
        de las clases de decorador.
        """
        return f"DecoratorSuma({str(int(self.component.operation()) + 2)})" #Aplicamos la operación del decorador, en este caso queremos suma al número a decorar 2

    
    



class DecoratorMultiplicar(Decorator):
    """
    
    Los decoradores pueden ejecutar su comportamiento antes o después de la llamada a un
    objeto envuelto.
    """

    def operation(self) -> str:    
        return f"DecoratorMultiplicar({str(int(self.component.operation()) * 2)})" #Aplicamos la operación del decorador, en este caso queremos multiplicar el número a decorar por 2

class DecoratorDividir(Decorator):
    """
    
    Los decoradores pueden ejecutar su comportamiento antes o después de la llamada a un
    objeto envuelto.
    """

    def operation(self) -> str:
        return f"DecoratorDividir({str(int(self.component.operation()) / 3)})" #Aplicamos la operación del decorador, en este caso queremos dividir el número a decorar por 3


def client_code(component: Component) -> None:
    """
    El código del cliente funciona con todos los objetos que utilizan la interfaz de componentes. Este
    forma en que puede permanecer independiente de las clases concretas de componentes en los que funciona
    con.
    """
    print(f"RESULT: {(component.operation())}", end="") 




if __name__ == "__main__":
    numero = Number(5)
    print("Número a decorar: ")
    client_code(numero)
    print("\n")


    decorator1 = DecoratorSuma(numero)
    decorator2 = DecoratorMultiplicar(numero)
    decorator3 = DecoratorDividir(numero)
    print("Cliente: Ahora tengo 3 componentes decorados:")
    print("\n")
    client_code(decorator1)
    print("\n")
    client_code(decorator2)
    print("\n")
    client_code(decorator3)
    print("\n")
   

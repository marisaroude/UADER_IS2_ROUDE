#*--------------------------------------------------
#* proxy.py
#* excerpt from https://refactoring.guru/design-patterns/proxy/python/example
#*--------------------------------------------------

from abc import ABC, abstractmethod
import os
import sys

#Clase que contiene la logica para realizar ping a una dirección IP
class Ping(ABC):
    """
    La interfaz Ping declara operaciones comunes para RealPing y
    el apoderado. Siempre que el cliente trabaje con RealPing usando este
    interfaz, podrá pasarle un proxy en lugar de un tema real.
    """

    @abstractmethod
    def execute(self, string: str) -> None:
        pass

    @abstractmethod
    def executefree(self, string: str) -> None:
        pass


#Implementamos el método execute(string) de la clase Ping para realizar 10 intentos de ping a la dirección IP contenida en "String"
class RealPing(Ping):
    """
    El RealPing contiene cierta lógica comercial central. Por lo general, RealPing son
    capaz de hacer algún trabajo útil que también puede ser muy lento o sensible -
    p.ej. corregir los datos de entrada. Un Proxy puede resolver estos problemas sin ningún
    cambios en el código de RealPing.
    """

    #Execute toma un string como entrada y comprueba su conectividad con el comando ping del s.o
    def execute(self, string: str) -> None:
        if not string.startswith("192."): #Verificando si la cadena de texto no comienza con la subcadena 192.
            print("Direccion IP invalida")   #En ese caso, dice que la Dirección IP es inválida y sale.
            return
        for i in range(10): #Si comienza con 192. comienza a realizar los pings al host en un ciclo repetitivo de 1 a 10 
            response = os.system("ping " + string)
            if response == 0: #Si el valor es 0 la función indica que el host está en linea.
                print(string, 'En línea.')
            else: #Si es diferente de 0, la función indica que el host está desconectado
                print(string, 'Desconectado.')
                sys.exit() #Este sys.exit finaliza la ejecución en caso de que esté desconectado.


    #En este executeFree no se evalúa la dirección IP
    def executefree(self, string: str) -> None:
        for i in range(10):
            response = os.system("ping " + string)
            if response == 0:
                print(string, 'En línea.')
            else:
                print(string, 'Desconectado.')
                sys.exit() #Este sys.exit finaliza la ejecución en caso de que esté desconectado.



#PingProxy actúa como proxy para la clase Ping
#Acá implementamos el metodo execute(string) de PingProxy 
class PingProxy(Ping):
    """
    El Proxy tiene una interfaz idéntica a RealPing.    """
    def __init__(self, ping: Ping):
        self._ping = ping


    #Este metodo execute, toma un string y realiza una comprobación
    # de conectividad en el host específicado utilizando la clase ping
    # Si la IP es "192.168.0.254" en lugar de ejecutar el ping en esa dirección IP
    # el metodo execute llama al metodo executefree pasandole www.google.com como argumento
    def execute(self, string: str) -> None:
        if string == "192.168.0.254":
            self._ping.executefree("www.google.com")
        else:
            self._ping.execute(string)

    def executefree(self, string: str) -> None:
        self._ping.executefree(string)

        """
        Las aplicaciones más comunes del patrón Proxy son la carga diferida,
        almacenamiento en caché, control de acceso, registro, etc. Un Proxy puede realizar una
        de estas cosas y luego, dependiendo del resultado, pasar la ejecución a
        el mismo método en un objeto RealSubject vinculado.
        """



def client_code(ping: Ping, string: str) -> None:
    """
    Se supone que el código del cliente funciona con todos los objetos (tanto sujetos como
    proxies) a través de la interfaz Asunto para admitir ambos sujetos reales
    y apoderados. En la vida real, sin embargo, los clientes trabajan principalmente con sus verdaderos
    sujetos directamente. En este caso, para implementar el patrón más fácilmente,
    puede extender su proxy de la clase del sujeto real.
    """
    ping.execute(string)


if __name__ == "__main__":
    ping = RealPing()
    proxy = PingProxy(ping)

    print("Ahora hace un ping a una dirección inválida: ")
    ip1 = "8.8.8.8"
    print(ip1)
    client_code(ping,ip1)
    print("\n")

    print("Ahora hace un ping a la dirección en Línea, en este caso Google: ")
    ip2 = "192.168.0.254"
    print(ip2)
    client_code(proxy, ip2)

    print("\n")
    
    print("Ahora hace un ping a una dirección Desconectada: ")
    ip3 = "192.168.0.255"
    print(ip3)
    client_code(ping, ip3)

    print("\n")
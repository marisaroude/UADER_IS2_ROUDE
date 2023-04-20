import os
#*--------------------------------------------------------------------
#* La clase Director orquesta la construcción del objeto indicando 
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------
class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder


   def getAvion(self):
      avion = Avion()
     
      
      # Primero el chasis
      body = self.__builder.getBody()
      avion.setBody(body)
      
      
      # Luego las turbinas
      turbinas = self.__builder.getTurbinas()
      avion.setTurbinas(turbinas)

      # Luego las alas
      alas = self.__builder.getAlas()
      avion.setAlas(alas)

      # Por ultimo el tren de aterrizaje
      tren = self.__builder.getTrenDeAterrizaje()
      avion.setTren(tren)

      # Retorna el avion completo
      return avion

#*----------------------------------------------------------------
#* Esta es la definición de un objeto avion inicializando 
#* todos sus atributos
#*----------------------------------------------------------------

class Avion:
   def __init__(self):
      self.__turbinas = list()
      self.__alas = list()
      self.__tren = None
      self.__body = None

   def setBody(self, body):
      self.__body = body

   def setAlas(self, alas):
      self.__alas = alas

   def setTurbinas(self, turbinas):
      self.__turbinas = turbinas

   def setTren(self, tren):
      self.__tren = tren

   def specification(self):
      print ("Chasis: %s" % (self.__body.shape))
      print ("Alas: %d" % (self.__alas.amount))
      print ("Turbinas: %d\'" % (self.__turbinas.amount))
      print ("Tren de aterrizaje: %d\'" % (self.__tren.amount))

#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class Builder:

      def getBody(self): pass
      def getTurbinas(self): pass
      def getAlas(self): pass
      def getTrenDeAterrizaje(self): pass

#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un Avion
#* Establece instancias para tomar turbinas, alas y tren de aterrizaque
#* estableciendo las partes específicas que (en un avion) 
#* deben tener esas partes
#*-------------------------------------------------------
class AvionBuilder(Builder):
   
   def getTurbinas(self):
      turbinas = Turbinas()
      turbinas.amount = 2
      return turbinas
   
   def getAlas(self):
      alas = Alas()
      alas.amount = 2
      return alas

   def getTrenDeAterrizaje(self):
      tren = Tren()
      tren.amount = 1
      return tren  
   
   def getBody(self):
      body = Body()
      body.shape = "Condor"
      return body

#*----------------------------------------------------------------
#* Define partes genéricas para un avion (sin inicializar)
#*----------------------------------------------------------------

class Body:
   shape = None

class Turbinas:
   amount = None

class Alas:
   amount = None

class Tren:
   amount = None
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():

#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el 
#* proceso de construcción
#*----------------------------------------------------------------
   avionBuilder = AvionBuilder()
   director = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un avion
#*----------------------------------------------------------------   
   director.setBuilder(avionBuilder)
#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un avion según
#* la hoja de ruta
#*----------------------------------------------------------------
   avion = director.getAvion()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   avion.specification()
   print ("\n\n")
#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
   os.system("clear")
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un Avión\n")

   main()

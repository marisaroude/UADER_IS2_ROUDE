import os
#*--------------------------------------------------------------------
#*
#*--- Se definen los métodos de producción, cada uno toma los mismos
#*--- dos atributos: thickness and width lo cual produce una
#*--- lamina acorde a esa especificación
#*--------------------------------------------------------------------

#*--- Abstracción de implementación (ProduceLaminas5mt)
class ProduceLaminas5mt:

	def produce_laminas(self, thickness, width):
		print(f'Fabricando una lámina de 5 metros con un grosor de {thickness} y un ancho de {width} ')
		#print("ProduceLaminas5mt va a fabricar una Lamina de dimensiones(%d,%d)" % (thickness,width))

#*--- Abstracción de implementación (ProduceLaminas10mt)
class ProduceLaminas10mt:

	def produce_laminas(self, thickness, width):
		print(f'Fabricando una lámina de 10 metros con un grosor de {thickness} y un ancho de {width} ')

		#print("ProduceLaminas10mt va a fabricar una Lamina de dimensiones(%d,%d)" % (thickness,width))



#*---Clase Lamina  con sus propiedades pero con método de fabricación flexible
 
class Lamina:

	def __init__(self, thickness, width,produceLaminas):

		self._thickness = thickness
		self._width = width

		self._produceLaminas = produceLaminas

#*---- cuando se invoca la producción invoca al objeto cuyo puntero se almacenó al crear

	def produce(self):

		self._produceLaminas.produce_laminas(self._thickness, self._width)


	def setproduceLaminas(self, produceLaminas):

		self._produceLaminas = produceLaminas


#*-----------------------------------------------------------
#* main
#*-----------------------------------------------------------



#*--- implementa una primer lamina con cierto grosor y ancho  y le asigna ProduceLaminas5mt() para crearlas de 5metros
lamina1 = Lamina(0.5, 1.5,ProduceLaminas5mt())
lamina1.produce()

#*--- implementa una primer lamina con cierto grosor y ancho  y le asigna ProduceLaminas10mt() para crearlas de 10metros
lamina2 = Lamina(0.5, 1.5,ProduceLaminas10mt())
lamina2.produce()


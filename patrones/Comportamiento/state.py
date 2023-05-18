

import os
import sys
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#*-------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):
		self.file = file
		self.content = content
		

	def __str__(self): 
		return str(self.content)
		#return f"Memento(file={self.file}, content={self.content})"

class FileWriterUtility:

	def __init__(self, file):

		self.file = file
		self.content = []
		self.states = [] #Creamos una lista llamada states dentro de la clase para almacenar los estados anteriores.

	#Permite agregar texto al contenido actual del objeto 'filewriterutility'. Cada vez q se llama a este metodo con una cadena de texto, esa cadena se añade al contenido existente.
	def write(self, string):
		self.content.append(string)

	def reemplazar (self,string):
		self.content.replace(str(string),'')

	def save(self):#Modificamos este método para comprobar si la lista tiene más de 4 estados, en caso de ser así, elimina el estado más antiguo antes de añadir el nuevo estado
		if len(self.states) >= 4:
			self.states.pop(0)
			eliminado_content = self.content.pop(0)
			print(f"Se borra el estado: '{eliminado_content}' por cuestiones de espacio.")
			
		self.states.append(Memento(self.file, self.content))


	def undo(self, memento = None,count=0): # El método undo ahora acepta un argumento adicional undo que indicará cuantos estados anteriores se deben deshacer. Si 'count' es 0, se recupera el estado inmediatamente anterior; si 'count' es 1, 2 o 3 recupera los estados anteriores en ese orde.
		count = int(input('¿Cuantos estados deseas borrar?: '))
		if count < len(self.states): #Comprueba si el valor de count es menor que la longitud de la lista self.states, lo cual significa que existe un estado anterior disponible para deshacer.
			memento = self.states [-1 - count] #Si se cumple la condición anterior, se accede al estado anterior correspondiente utilizando. -1 representa el estado más reciente
			self.file = memento.file #establece el archivo en el valor almacenado en el estado anterior
			for i in range(count):
				self.content.pop() #establece el contenido en el valor almacenado en el estado anterior.
		else:
			print("Error, no hay suficientes estados para borrar")
			sys.exit()

	def show_content(self):
		for i in self.content:
			print(i)
	


class FileWriterCaretaker:
	def save(self, writer):
		self.obj = writer.save()

	def undo(self, writer):
		writer.undo(self.obj)


if __name__ == '__main__':
	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar")
	writer = FileWriterUtility("GFG.txt")

	print("Se graba algo en el objeto y se salva")
	writer.write("Clase de IS2 en UADER\n")
	writer.show_content()
	caretaker.save(writer)

	print("Se graba información adicional (1)")
	writer.write("Primer material adicional de la clase de patrones\n")
	writer.show_content()
	caretaker.save(writer)

	print("Se graba información adicional (2)")
	writer.write("Segundo material adicional de la clase de patrones\n")
	writer.show_content()
	caretaker.save(writer)

	print("Se graba información adicional (3)")
	writer.write("Tercer material adicional de la clase de patrones\n")
	writer.show_content()
	caretaker.save(writer)

	print("Se graba información adicional (4)")
	writer.write("Cuarto material adicional de la clase de patrones\n")
	writer.show_content()
	caretaker.save(writer)


	print("se invoca al <undo>\n")
	caretaker.undo(writer)

	print("Se muestra el estado actual\n")
	writer.show_content()





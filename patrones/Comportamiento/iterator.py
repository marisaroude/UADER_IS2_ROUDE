import os
class Iterator:
    def __init__(self, collection):
        self._collection = collection
        print("inicializa iterator")
        self._index = 0

    def __next__(self):
        try:
            result = self._collection[self._index]
            self._index += 1
            return result
        except IndexError:
            print("Error de índice <eol>")
            raise StopIteration

class Collection:
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __iter__(self):
        return Iterator(self._items)

    def add_item(self, item):
        self._items.append(item)



#*--------- Crea colección
collection = Collection()
collection.add_item('I')
collection.add_item('S')
collection.add_item('W')
 
#*-------- La recorre
print('Recorrido en sentido directo: ')
for item in collection:
    print(item)
    
print()

#Una forma es utilizando el método reversed
print('Recorrido en sentido inverso: (1)')
for item in reversed(collection) :
    print(item)

print()
#Otra forma es utilizando la técnica de rebanado
print('Recorrido en sentido inverso: (2)')
for item in collection[::-1]:
    print(item)
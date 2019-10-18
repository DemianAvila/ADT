"""
Colas de prioridad acotada (solo entre 0 y 10), y no acotada (de 0 al infinito)
Es una version extendida de la implementacion de la cola basica, con la variante
de que cada elemento insertado llevará un numero que indica una prioridad especifica,
los elementos son ordenados en base a esa prioridad. 
Si hay mas de un elemento con la misma prioridad
estos se manipulan con el protocolo FIFO

valor (prioridad)

3(10), 5(8), 20(5), 12(3), 11(1), 6(7)
Al principio head y tail esta en el elemento 0, a menor numero es mayor la prioridad

Es decir, queda ordenado como
3
5,3
20,5,3
12,20,5,3
11,12,20,5,3
11,12,20,6,5,3

3(10), 5(8), 20(5), 12(3), 11(1), 6(7),40(5), 30(3), 1(5)
en este caso, el 40 va despues del 20, por que el 20 entró primero y si se borran los elementos del head (primer elemento), saldra primero el 20
11,12,30,20,40,1,6,5,3


Desencolar, saca el head (el que ya llego a la fila de las tortillas)
Desencolar con prioridad (aquel mas cercano al first de la prioridad señalada)
    En el caso de la prioridad 5, eliminara el 20
    
Una cola doble es aquella en la que se puede agregar tanto al final como al inicio, de la misma forma se puede sacar de prinipio y del final. El ADT es el siguiente:
ADT DoubleQueue()
add_first(value) al head
add_last(value) al tail
dequeue_first() borra el first
dequeue_last() borra el last
first() 
last()
is_empty() true/false
lenght()
to_string()
"""
class Queue:
    def __init__(self):
        self.__data=[]

    def add_last(self, value):
        self.__data.append(value)

    def dequeue(self):
        if len(self.__data)>0:
            self.__data.pop(0)
        else:
            print("Lista vacia")

    def first (self):
        if len(self.__data)<0:
            return self.__data[0]
        else:
            print("Lista vacia")
    
    def last (self):
        if len(self.__data)<0:
            return self.__data[len(self.__data)-1]
        else:
            print("Lista vacia")
            
    def length(self):
        return len(self.__data)
    
    def to_string(self):
        print(self.__data)

    def is_empty(self):
        if len self.__data==0:
            return True
        else
        return False
"""
cola=Queue()
cola.add_last(1)
cola.add_last(2)
cola.add_last(3)
cola.to_string()
cola.dequeue()
cola.to_string()
"""    

#implementar cola de prioridad acotada y no acotada, ademas de la cola doble

"""class Queue:
    def __init__(self):
        self.__data=[]"""
        
class DoubleQueue:
    def __init__(self):
        self.__data=[]
    
    def add_last(self, value):
        self.__data.append(value)
    
    def add_first(self, value):
        self.__data.insert(0, value)
        
    def dequeue_first(self):
        if len(self.__data)>0:
            return self.__data.pop(0)
        else:
            print("Lista vacia")
    
    def dequeue_last(self):
        if len(self.__data)>0:
            return self.__data.pop()
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
"""
cola=DoubleQueue()
cola.add_first(1)
cola.add_first(2)
cola.add_first(3)
cola.add_last(2)
cola.add_last(3)
cola.to_string()
cola.dequeue_first()
cola.dequeue_last()
cola.to_string()
"""

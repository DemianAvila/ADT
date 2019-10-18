class DelimitedPriorityQueue:
    def __init__ (self):
        self.__data= []
        self.__prioridad=int(input("Establece tu prioridad maxima: \n"))


    
    def add_element (self, value, priority):
        Nodo=[value, priority]


        if self.__prioridad<priority:
            print("Este elemento excede la prioridad maxima")

        else:

            if len(self.__data)==0:
                self.__data.append(Nodo)

            elif Nodo[1]>self.__data[len(self.__data)-1][1]:
                self.__data.append(Nodo)
        
            else:
                for i in range (len(self.__data)):
                    if Nodo[1]<self.__data[i][1]:
                        tmp=self.__data[i]
                        self.__data[i]=Nodo
                        self.__data.append(tmp)

    def dequeue(self):
        if len(self.__data)>0:
            self.__data.pop(0)
        else:
            print("Lista vacia")            

    def to_string (self):
        print (self.__data)

    def lenght (self):
        return len(self.__data)

    def is_empty(self):
        if len (self.__data)==0:
            return True
        else:
            return False
"""
cola=DelimitedPriorityQueue()
cola.add_element(1,1)
cola.to_string()
cola.add_element(2,0)
cola.to_string()
cola.add_element(3,4)
cola.to_string()
cola.add_element(4,2)
cola.to_string()
cola.add_element(5,3)
cola.to_string()
cola.add_element(6,3)
cola.to_string()
cola.dequeue()
cola.to_string()
"""

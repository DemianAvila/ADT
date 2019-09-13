#Estructura de datos, array
#es un adt (tipo de dato abstracto (nueva clase, objeto, etc con funciones propias)) que almacena elementos con indice

"""Array (n)--->contructor, n= numero de elemntos
get_lenght()----> obtiene la longitud
get_item(index)---> elemento en el indice
set_item(index, v)----> pide el index y el valor, inserta el valor en la lista 
clearing(valor), todos los elementos de arreglo son inicializados con el valor del parametro"""

class Array:
    def __init__(self, n):
        self.__data=[]
        for i in range (n):
            self.__data.append(None)

    def get_length(self):
        return len(self.__data)

    def to_string(self):
        print(self.__data)

    def set_item(self, index, value):
        if index >=0 and index<=len(self.__data):
            self.__data[index]= value
        else:
            print("Fuera de rango")
            
    def get_item(self, index):
        if index>=0 and index<=len(self.__data):
            return self.__data[index]
        else:
            print("Fuera de rango")

    def clearing (self, valor):
        for index in range (len(self.__data)):
            self.__data[index]=valor
    
def main():
    arreglo=Array(10)
    arreglo.to_string()
    print(f"el tamaño es de {arreglo.get_length()}")
    arreglo.set_item(1,12)
    arreglo.to_string()
    arreglo.set_item(12,9)
    print(arreglo.get_item(1))
    print(arreglo.get_item(20))
    arreglo.clearing(4)
    arreglo.to_string()
    
main()

#array2d
"""array2d (rows, cols)
get_num_cols()
get_num_rows()
clearing(value)
set_item(r, c, value)
get_item (r, c)"""

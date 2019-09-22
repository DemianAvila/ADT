#array3d(rows, cols, depth)
#get_num_cols
#get_num_rows
#get_num_depht
#set_item(r,c,d,v)
#get_item(r,c,d)
#clearing(V)
#to_string

class Array3D:
    def __init__(self, rows, cols, depth):
        self.__data=[]
        self.__cols=cols
        self.__rows=rows
        self.__depth=depth


        for i in range (depth):
            tmp=[] #crea una lista
            for j in range (rows):
                tmp2=[] #crea otra lista
                for k in range (cols):
                    tmp2.append(None) #añade "none" a la segunda lista, tantas columnas existan
                tmp.append(tmp2) #añade la segunda lista a la primera lista, tantas filas existas
            self.__data.append(tmp)#añade la primer lista temporal al costructor, tanta prfundidad exista

    def to_string (self):
        print(self.__data)

    def get_num_rows(self):
        return(self.__rows)

    def get_num_cols(self):
        return(self.__cols)
    
    def get_num_depth(self):
        return(self.__depth)
    
    def set_item (self, rows, cols, depth, value): #primero se elige la prfundidad 
        self.__data[depth][rows][cols]=value

    def get_item (self, rows, cols, depth):
        return(self.__data[depth][rows][cols])

    def clearing (self, value):
        for i in range (self.__depth): #acceder a los atributos la clase (del constructor)
            for j in range (self.__rows):
                for k in range (self.__cols):
                    self.__data[i][j][k]=value

"""  
#Para probar el programa
      
def main():
    matriz=Array3D(2,2,2)
    matriz.to_string()
    print(matriz.get_num_rows())
    print(matriz.get_num_cols())
    print(matriz.get_num_depth())
    matriz.set_item (0,1,0,4)
    matriz.to_string()
    print(matriz.get_item(0,1,0))
    matriz.clearing(0)
    matriz.to_string

main()


#como leer un excel con for en python,
#paquete xlrd
#vaciar la informacion en un array3d :v
#pip instal xlrd
"""
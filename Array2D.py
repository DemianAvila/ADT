#array 2D
#array2D(rows,cols)
#get_num_rows()---->regresa numero de filas
#get_num_cols()---->regresa nuemero de columnas
#clearing (value)---->inicializa
#set_item(row, col, val)-----> cambia valor
#get_item(row,col)

class Array2D:
    def __init__(self, rows, cols):
        self.__data = [] #var privada
        self.__row=rows
        self.__col=cols
        for row in range (rows):
            tmp=[]
            for col in range (cols):
                tmp.append(None)
            self.__data.append(tmp)
            
    def to_string(self):
        print(self.__data)

    def get_num_rows(self):
        return self.__row

    def get_num_cols(self):
        return self.__col

    def clearing(self, value):
        for row in range (self.__row):
            for col in range (self.__col):
                self.__data[row][col]=value

    def set_item(self, rows, cols, value):
        if (rows<0 or rows>self.__row) or (cols<0 or cols>self.__col):
            print("Fuera de rango")
        else:
            self.__data[rows][cols]=value
            
    def get_item(self, rows, cols):
        return self.__data[rows][cols]


"""def main():
    arr2d=Array2D(3,5)
    arr2d.to_string()
    print(f"el numero de filas es {arr2d.get_num_rows()}" )
    print(f"el numeros de columnas es {arr2d.get_num_cols()}")
    arr2d.clearing(8)
    arr2d.to_string()
    arr2d.set_item(1,3,2)
    arr2d.to_string()
    arr2d.set_item(5,6,2)
    print(arr2d.get_item(1,3))
main()"""
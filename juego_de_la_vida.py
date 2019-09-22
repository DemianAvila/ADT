#Reglas del juego de la vida (Zero player)
#Si una celula que se encuentra viva tiene 0 o 1 vecino, muere por soledad para la siguente generacion
#Donde los vecinos son las 8 celulas que lo rodean inmediatamente
#2.- Una celula viva que tiene 2 o 3 vecinos, sobrevive para la siguiente generacion
#3.- Una celula viva que tiene 4 o mas vecinos muere por sobre-poblacion para la siguente generacion
#una celula muerta con exactamente 3 vecinos vivos, resulta en un nacimiento, cuya vida empieza en la siguente generacion
#las celulas muertas permanecen muertas
#vivas 1, muertas 0
#Cuantas egneraciones quieres probar

#juego de la vida (rows,cols, generaciones, poblacion inicial)
#get_num_rows()
#get_num_cols()
#configure_next_gen(nueva poblacion)
#set_cell_death(row,col)
#set_cell_alive(row, col)
#is_live_cell(row, col)---->boolean
#get_num_live_neighbors

from Array2D import Array2D
class JuegoDeLaVida:
    def __init__(self,rows,cols,generaciones,poblacion_inicial):
        self.__cuadro=Array2D(rows,cols)
        self.__filas=rows
        self.__columnas=cols
        self.__generaciones=generaciones
        self.__cuadro.clearing(0)
        for cell in poblacion_inicial: 
            self.__cuadro.set_item(cell[0],cell[1],1)
    def to_string(self):
        print(self.__cuadro.to_string())
    def configure_next_generation(self, nueva_generacion):
        self.__cuadro.clearing(0)
        for i in nueva_generacion:
            self.__cuadro.set_item(i[0],i[1],1)
    def set_cell_death(self,row,col):
        self.__cuabro.set_item(row,col,0)
    def set_cell_alive(self,row,col):
        self.__cuabro.set_item(row,col,1)
    def is_live_cell(self,row,col):
        if self.__cuadro.get_item(row,col) == 1:
            return True
        else:
            return False
    def calcula_vecinos(self,x,y):
        vecinos=[x-1,y-1,x+1,y+1]
        if vecinos[0]==-1:
            vecinos[0]=0
        if vecinos[1]==-1:
            vecinos[1]=0
        if vecinos[3]==self.__columnas:
            vecinos[3]=self.__columnas-1
            pass
        if vecinos[2]==self.__filas:
            vecinos[2]=self.__filas-1
            pass
        return vecinos
    def get_num_vecinos_vivos(self,col,row):
        limites=self.calcula_vecinos(col,row)
        cont=0
        for x in range(limites[0],limites[2]+1,1):
            for y in range(limites[1],limites[3]+1,1):
                if self.is_live_cell(x,y):
                    if x==col and y == row:
                        pass
                    else:
                        cont+=1
        return cont

def main():
    inicial=[[1,3],[2,2],[2,3],[2,4],[1,1]]
    X_T=False
    while X_T != True :
        X_num=int(input('Digite el valor del tablero (de 5 en adelante) : '))
        if X_num>=5 :
            X_T=True
        else:
            print("digite un valor adecuado")
    Y_num=X_num
    Gen_T=False
    while Gen_T != True:
        num_generaciones=int(input('Digite el numero de generaciones que desea: '))
        if num_generaciones>0:
            Gen_T = True
        else:
            print("digite un numero de generaciones adecuado")	
    juego=JuegoDeLaVida(X_num,Y_num,num_generaciones,inicial)
    save_data2=[]
    for x in range(num_generaciones):
        print(f"generacion: {x}")
        for r in range(X_num):
            for c in range(Y_num):
                if juego.is_live_cell(r,c):
                    if juego.get_num_vecinos_vivos(r,c) == 0 or juego.get_num_vecinos_vivos(r,c)==1 :
                        pass
                    if juego.get_num_vecinos_vivos(r,c) == 2 or juego.get_num_vecinos_vivos(r,c)==3:
                        lista=[r,c]
                        save_data2.append(lista)
                        pass
                    if juego.get_num_vecinos_vivos(r,c)>3:
                        pass
                    pass
                if juego.is_live_cell(r,c) != True: 
                    if juego.get_num_vecinos_vivos(r,c) > 2 and juego.get_num_vecinos_vivos(r,c)<4 :
                        lista=[r,c]
                        save_data2.append(lista)
                        pass
                    else:
                        pass
                    pass
                pass#fin for
            pass
        juego.to_string()
        juego.configure_next_generation(save_data2)
        for p in range(len(save_data2)):
            save_data2.pop()
            pass
        pass 

    
    
main()

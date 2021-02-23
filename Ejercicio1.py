import numpy as np
    
#Implementacion
T = np.random.randint(1, 5000)  #Se asigna un valor aleatorio entre 1 y 5000 a T
N = []
M = []
Directions = []

#Se agregan T valores aleatorios a N y M
for i in range(T):

    N.append(np.random.randint(1,1000000000))
    M.append(np.random.randint(1,1000000000))

    #La posicion resultante depende del numero de filas o columnas, si el numero de filas (N) es mayor o igual al de columnas (M), sera Left (L) o Right (R) 
    if N[i] >= M[i]:
        
        #Si el numero de filas es par, sera Left (L), si es impar sera Right(R)
        if N[i] % 2 == 0:
            Directions.append("L")

        elif N[i] % 2 != 0:
            Directions.append("R")

    #Si el numero de filas (N) es menor que el numero de columnas (M), sera Up (U) o Down (D)
    elif N[i] < M[i]:

        #Si el numero de filas es par, sera Up (U), si es impar sera Down (D)
        if N[i] % 2 == 0:
            Directions.append("U")

        elif N[i] % 2 != 0:
            Directions.append("D")

#Imprimimos los datos evaluados
print("T = ", T)
for i in range(T):
    print(N[i], " ", M[i])

#Imprimimos la salida con las direcciones
print("Exit values")
for i in range(T):
    print(Directions[i])
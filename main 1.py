from typing import Counter
#le damos la bienvenida al usuario

print("Hola Usuario :D ")
print({f"Cuantos ejercicios quieres añadir? "})

#definimos variables
def Partes_Validas(K,R):
    #cuenta los residuos K
    Contar=[0]*K
    for Num in R:
        Resta=Num % K
        Contar[Resta] +=1

#calcular los pares validos
Partes_Validas=0
for E in range(K): # type: ignore
    if Counter[E]>0:
        Complemento=(K-E)%K # type: ignore
        if Complemento==E:
            Partes_Validas+=Counter[E]*(Counter[E]-1) #pares en el mismo residuo
        elif Complemento<E:
            Partes_Validas+=Counter[E]*Counter[Complemento] #pares dentro del residuo y su complemento
    return Partes_Validas 

T=int(input()) #multiples casos de prueba

for Casos in range(1,T+1):
    print(T)
    
#Creado y desarrollado por Miguel Guerrero C.C 1090381839
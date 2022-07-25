#Diferencia, complemento de un conjunto y diferencia simétrica.

#Vamos a tomar el siguiente conjunto como el conjunto universal.
U = {"a","b",1,2,4, "azul","rojo",312,5,32,12}
#print(U)
A = {"azul",1,4}
B = {"a","azul","rojo",312}
C = {2,4,"a"}

#1. Diferencia.
# print(A)
# print(B)
# C = A - B
# print(C)
# D = A.difference(B)
# print('La diferencia entre A y B es ', D)
# G = B - A
# K = B.difference(A)
# print(G)
# print(K)


#2. Complemento.
#print(U)
#print(A)
# Ac = U - A
# print(Ac)
# Ac = U.difference(A)
# print(Ac)
def complemento(a):
    return U-a

#print(complemento(A))
#print(C)
#print(complemento(C))

#3. Diferencia simétrica.
print(A)
print(C)
print(A.symmetric_difference(C))

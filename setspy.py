#Conjuntos en python
#1. Como escribir un conjunto en python
U = {1,2,3,4,5,6,89,45,32,23,11}
A = {1,2,3,32,23}
B = {4,3,5,32,11}
#print(f'El conjuntos A es {A} y el conjunto B es {B}.')
#2. Verificar con type
#print(type(U))
#3. Ver si es un subconjunto .issubset()
#print(A.issubset(U))
#print(U.issubset(A))
#print(A.issubset(B))
#print(B.issubset(A))
#4. Ver la unión y la interesección
#4.1 unión
C = A | B
#print(C)
#print(A.union(B))
#print(A.union(U))
#4.2 intresección
D = A & B
#print(D)
#print(A.intersection(B))
#print(A.intersection(U))
#5. Ejemplo
V = {'Juan', 'Angelica', 'Daniel', 'Pedro', 'Laura', 'Claudia', 'Carlos'}
H = {'Juan', 'Daniel', 'Pedro', 'Carlos'}
M = {'Angelica', 'Laura', 'Claudia'}

# print(H.issubset(M))
# print(M.issubset(V))

# print(M.union(H))
# print(V.union(H))

#print(H.intersection(M))
print(V.intersection(H))









#Creamos una función que nos da el producto cartesiano entre dos conjuntos
def producto_cartesiano(a,b):
    C = set()
    for i in a:
        for j in b:
            C.add((i,j))
    return C

#Ejemplo
A = {1,2}
B = {1,2,3}
D = producto_cartesiano(B,A)
print(D)
#Cardinal de un conjunto.
#len
c = len(A)
print(c)
def valor_abs(x):
    if x >= 0:
        return x
    else:
        return -x

#Cardinal del producto cartesiano
r = len(D)
print(r)
t = len(B)
print(t)

print(valor_abs(-3))
def filtrar_palabras(lista,n):
    palabras=[]
    for i in range(len(lista)):
        if len(lista[i])>=n:
            palabras.append(lista[i])
    return palabras


lista=["a","s","hsahjKAshdjha","sana"]

print(filtrar_palabras(lista,4))

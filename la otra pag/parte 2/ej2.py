def mas_larga(lista):
    largo=0
    pal=lista[0]
    for i in range(len(lista)):
        if len(lista[i])>largo:
            largo=len(lista[i])
            pal=lista[i]
    return pal


lista=["a","as","asde","0","as","a","asd"]

print(mas_larga(lista))

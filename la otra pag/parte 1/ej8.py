def superposicion(lista,lista2):
    for i in range(len(lista)):
        for j in range(len(lista2)):
            if lista[i]==lista2[j]:
                return True
    else:
        return False


lista=[1,2,3,4,5]
lista2=[6,5]

print(superposicion(lista,lista2))

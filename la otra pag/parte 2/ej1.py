def max_in_list(lista):
    mayor=lista[0]
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor



lista=[1,8,4,7,9,2,3]

print(max_in_list(lista))

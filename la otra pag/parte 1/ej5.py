def sum(lista):
    res=0
    for i in range(len(lista)):
        res+=lista[i]
    return res

def multip(lista):
    res=lista[0]
    for i in range(0,len(lista)):
        res=res*lista[i]
    return res

lista=[1,2,3,4,5]

print(sum(lista))
print(multip(lista))

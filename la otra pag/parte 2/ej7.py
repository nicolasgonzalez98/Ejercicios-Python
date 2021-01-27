def nombres(lista,letra="a"):
    letra=letra.capitalize()
    res=[]
    for i in range(len(lista)):
        lista[i]=lista[i].capitalize()
        if lista[i][0]==letra:
            res.append(lista[i])
    return res


lista=["Nicolas","Alberto","damian","matias","Aaron","amancio"]

print(nombres(lista,"n"))





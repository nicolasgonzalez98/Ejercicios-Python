def es_palindromo(cad):
    cad=cad.lower()
    cad=list(cad)
    pal=[]
    for i in range(len(cad)-1,-1,-1):
        pal.append(cad[i])
    if pal==cad:
        return "Si, son palindromos"
    else:
        return "No, no son palindromos"

print(es_palindromo("amba"))
        

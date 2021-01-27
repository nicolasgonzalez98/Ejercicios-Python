def inversa(cadena):
    cadena=list(cadena)
    inv=[]
    for i in range(len(cadena)-1,-1,-1):
        inv.append(cadena[i])
    inv="".join(inv)
    return inv

print(inversa("Nicolas Gonzalez"))
    

def cant_mayus(cad):
    cant=0
    for i in range(len(cad)):
        if cad[i]>='A' and cad[i]<='Z':
            cant+=1
        elif cad[i] in ('Á','É','Í','Ó','Ú'):
            cant+=1
    return cant

cad=input("ingrese palabra")

print(cant_mayus(cad))

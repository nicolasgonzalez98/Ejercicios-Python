def cant_year(act):
    dicc={}
    while len(dicc)<3:
        nom=input("Ingrese el nombre: ")
        nac=int(input("Ingrese año de nacimiento de %s: "%nom))
        dicc[nom]=act-nac
    for nombres in dicc:
        print(nombres,"tiene",dicc[nombres])

cant_year(2020)
    
    

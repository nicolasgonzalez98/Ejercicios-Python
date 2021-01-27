def vocal(a):
    a=a.capitalize()
    vocales=['A','E','I','O','U']
    if a in vocales:
        return True
    else:
        return False
    

print(vocal('B'))

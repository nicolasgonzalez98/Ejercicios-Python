def bin_dec(num):
    num=list(reversed(list(str(num))))
    dec=0
    for i in range(len(num)):
        if num[i]=='1':
            dec=dec+2**i
    return dec

    


lista=11100
bin_dec(lista)
print(bin_dec(lista))

primos=[]
multiplos=[]
num=600851475143
valor=round(num/2)+1

def es_primo(num):
    for n in range(2, num):
        if num%n == 0:
            return
    primos.append(num)



for i in range(2,valor):
	if num%i==0:
		multiplos.append(i)
	print(multiplos)
print('Ya estan los multiplos.')

for n in multiplos:
	es_primo(n)

print('Ya estan los primos.')
print(primos)		

print(primos[-1])

lista=[1,2]
pares=[2]
while True:
	num=lista[-1]+lista[-2]
	lista.append(num)
	if num<=4000000 and num%2==0:
		pares.append(num)
	elif num>4000000:
		break




print(sum(pares))

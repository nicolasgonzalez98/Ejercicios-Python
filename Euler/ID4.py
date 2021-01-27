def divisibleDesde1a10():
	numeros=list(range(1,100000000))
	multiplos=list(range(1,21))
	interes=[]
	for i in numeros:
		contador=0
		for n in multiplos:
			if i%n==0:
				contador+=1
		if contador==20:
			interes.append(i)
			print(interes)
			
			
		
divisibleDesde1a10()

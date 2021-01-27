def divisibleDesde1a10():
	found=False
	i=20
	while found==False:
		c=0
		for x in range(1,21):
			if i%x==0:
				c+=1
		if c==20:
			print(i)
			found= True
		i+=1
			
			
		
divisibleDesde1a10()

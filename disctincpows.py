distinct_Pow=[]

#Generates a list of distinct powers for a^b where a and b are in[2,100]
for a in range(2,101):
	for b in range(2,101):
		pow=a**b
		if pow not in distinct_Pow:
			distinct_Pow.append(pow)
	

	
print len(distinct_Pow)

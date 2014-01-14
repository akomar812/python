#finds the largest palindromic number made from the product of 2 3-digit numbers

#if a number is palindromic, it is put in the following list
prod_List=[]

#returns true if a number is palindromic
def palin_Check(n):

	i=0
	j=1
	count=0
	while i < len(n)//2:
		if n[i] == n[len(n)-j]:
			j+=1
			count+=1
			i+=1
		elif n[i]!=n[len(n)-j]:
			break
	if count==len(n)//2:
		return True
	
big=0

#Generate and check the possible multiplications for palindromes
for a in range(100,1000):
	for b in range(100,1000):
		prod=a*b
		if palin_Check(str(prod)):
			prod_List.append(a*b)

for num in prod_List:
	if num>big:
		big=num
		
print big
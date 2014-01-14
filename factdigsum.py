from math import factorial

x=factorial(100)
x=str(x)
rolling_sum=0

for indx in range(0, len(x)):
	for chk in range(0,10):
		if str(chk)==x[indx]:
			rolling_sum+=chk
print rolling_sum
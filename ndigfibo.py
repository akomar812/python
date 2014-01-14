#fibonacci function
def fibonacci(f_0,f_1):
	return f_0 + f_1

#seeds for fibonacci sequence	
fn1=0
fn=1
#x=f_n+1
x=0
#n=target fibonacci length
n=raw_input("Find the first fibonacci number of what length?")
#count=number of iterations needed to achieve fibonacci number of given length
count=0

while len(str(x)) != int(n):
	x = fibonacci(fn1, fn)
	count+=1
	fn1=fn
	fn=x
print x
print count
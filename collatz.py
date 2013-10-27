#This program is slow as shit

#Collatz function
def collatz(x):
	if x % 2 == 0:
		x = x / 2
	else:
		x = (3 * x) + 1
	return x

max_latz=0


for num in range(1,1000001):
	num_dump=num
	counter=0
	while num != 1:
		num=collatz(num)
		counter+=1
	if counter > max_latz:
		big_num=num_dump
		max_latz=counter
	
print big_num
print max_latz


#returns the number of occurences of the value of "item" in the list "sequence"
def count(sequence, item):
	i=0
	counter=0
	while i<len(sequence):
		if sequence[i]==item:
			counter+=1
		i+=1
	return counter

#user generate sequence
lst=[]
done=False
while not done:
	print "Input item to add to list, input 'done' to complete"
	user=raw_input()
	if user!="done":
		lst.append(user)
	else:
		done=True

#Count instances of 
print "Input the the list item you would like to count occurrences of"
countof=raw_input()
print count(lst, countof)


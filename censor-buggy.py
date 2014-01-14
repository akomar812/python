def censor(text, word):
	text_list=text.split()
	x=0
	while x < len(text_list):
		if text_list[x]==word or text_list[x]==word.upper() or text_list[x]==word.lower():
			text_list[x] = "*" * len(word)
		x+=1
	return " ".join(text_list)
	
print censor("hey there, hey why aren't you responding? hey! HEY!", "hey")
def censor(text, word):
	text_list=text.split()
	x=0
	while x < len(text_list):
		if text_list[x]==word:
			text_list[x] = "*" * len(word)
		x+=1
	return " ".join(text_list)

word=raw_input("What word would you like to censor?")
print censor("Hey hey mama say the way you move, gon make me sweat, gon make me groove",word)

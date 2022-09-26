import string 


letter_l = list(string.ascii_lowercase)
letter_u = list(string.ascii_uppercase)
letter_p = list(string.punctuation)
nletters_l = 	{}
nletters_u = {}




def encryption(word,step):
	for x in range(0, len(letter_l)):
		nletters_l[letter_l[x]] = letter_l[x+step-len(letter_l)]
	for x in range(0, len(letter_u)):
		nletters_u[letter_u[x]] = letter_u[x+step-len(letter_u)]

	word = list(word)
	new_word = []
	for l in word:
		if l != " ":
			if l in letter_l:
				new_word.append(nletters_l[l])
			elif l in letter_u:
				new_word.append(nletters_u[l])
			elif l in letter_p:
				new_word.append(l)
		else:
			new_word.append(" ")


	new_word = "".join(new_word)
	return new_word







print(encryption("aaa" , 3) == "ddd")
print(encryption("ZZZ" , 3) == "CCC")
print(encryption("bBb" , 3) == "eEe")
print(encryption("CcC," , 3) == "FfF,")


step = int(input("step : "))
word = input("word : ")
print(encryption(word))
input()

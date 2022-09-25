import string 


letter_l = list(string.ascii_lowercase)
letter_u = list(string.ascii_uppercase)
nletters_l = 	{}
nletters_u = {}
new_word = []



def encryption(word , new_word):

	word = list(word)
	for l in word:
		if l != " ":
			if l in letter_l:
				new_word.append(nletters_l[l])
			elif l in letter_u:
				new_word.append(nletters_u[l])
		else:
			new_word.append(" ")

	new_word = "".join(new_word)
	return new_word






step = int(input("step : "))
word = input("word : ")



for x in range(0, len(letter_l)):
	nletters_l[letter_l[x]] = letter_l[x+step-len(letter_l)]
for x in range(0, len(letter_u)):
	nletters_u[letter_u[x]] = letter_u[x+step-len(letter_u)]



print(encryption(word, new_word))


input()
txt = input("Enter input text: ")
tokens = txt.split(" ")
for i in range(len(tokens)):
	a = 0
	while tokens[i][a] in ['!','.',',','?','/','\"',"\'",";"] :
		tokens[i] = tokens[i][a+1:]
	a = 0
	while tokens[i][-(a+1)] in ['!','.',',','?','/','\"',"\'",";"] :
		tokens[i] = tokens[i][:-(a+1)]
print("Tokens are:",tokens)
print("Total tokens:",len(tokens))
print("Total types of tokens:",len(set([i.lower() for i in tokens])))
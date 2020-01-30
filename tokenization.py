def tokenizer(txt) :
	tokens = txt.split(" ")
	for i in range(len(tokens)):
		a = 0
		while tokens[i][a] in ['!','.',',','?','/','\"',"\'",";"] :
			tokens[i] = tokens[i][a+1:]
		a = 0
		while tokens[i][-(a+1)] in ['!','.',',','?','/','\"',"\'",";"] :
			tokens[i] = tokens[i][:-(a+1)]
	return tokens

def main() :
	txt = input("Enter input text: ")
	tokens = tokenizer(txt)
	print("Tokens are:",tokens)
	print("Total tokens:",len(tokens))
	print("Total types of tokens:",len(set([i.lower() for i in tokens])))

if __name__ == '__main__' :
	main()
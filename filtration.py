import re, os, codecs
from tokenization import tokenizer

def filtration(txt) :
	tokens = tokenizer(txt)
	out = []
	for i in range(len(tokens)) :
		if re.search(r'[a-zA-Z0-9]',tokens[i][0]) :
			out.append(tokens[i])
	return out

def main():
        f = codecs.open('input1.txt', encoding='UTF-8')
        txt = f.read()
        tokens = tokenizer(txt)
        print("Tokens before filtration:",tokens)
        tokens = filtration(txt)
        print("Tokens after filtration:",tokens)

if __name__ == '__main__' :
	main()
import re
txt = input()
tokens = txt.split(" ")
for i in range(len(tokens)):
	a = 0
	while tokens[i][a] in ['!','.',',','?','/','\"',"\'",";"] :
		tokens[i] = tokens[i][a+1:]
	a = 0
	while tokens[i][-(a+1)] in ['!','.',',','?','/','\"',"\'",";"] :
		tokens[i] = tokens[i][:-(a+1)]
print("Tokens before filtration:",tokens)
out = []
for i in range(len(tokens)) :
	if re.search(r'[a-zA-Z0-9]',tokens[i][0]) :
		out.append(tokens[i])
print("Tokens after filtration:",out)
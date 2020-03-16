import re
nouns="I,you,bill,back,table,chair,apple,fox,bike,dog,boy,city,country,car,saw,bat,park".split(",")
verbs="said,ran,is,walk,sell,talk,command,belong,try,understand,love,play,park,back,consider".split(",")
verbd="ate,promised,saw".split(",")
verbn="promised,sunken".split(",")
preps="of,with,at,from,into,to,in,for,on,by,about,like".split(",")
conj="that,and,but".split(",")
art="a,an,the,that".split(",")
pronoun="I,it,he,him,his,she,her,hers".split(",")
adj="bad,good,beautiful,strange,handsome,tall,short,odd".split(",")
quants="many,few,several".split(",")
adv="that"
neg="not"
def category(root):
    cat=[]
    if root in nouns:
        cat.append("NN")
    if root in verbs:
        cat.append("VB")
    if root in verbd:
        cat.append("VBD")
    if root in verbn:
        cat.append("VBN")
    if root in quants:
        cat.append("QT")
    if root in preps:
        cat.append("IN")
    if root in art:
        cat.append("DET")
    if root in conj:
        cat.append("conj")
    if root in pronoun:
        cat.append("PRP")
    if root in adj:
        cat.append("JJ")
    if root in adv:
        cat.append("ADV")
    if root in neg:
        cat.append("NEG")
    
    return cat
dict ={}
def tokenize_form(sentence):
    tokens=sentence.split()
    f_tokens=[]
    roots=[]
    for t in tokens:
        w=re.compile(r'[a-zA-Z]+').findall(t)
        #print(w)
        f_tokens.extend(w)
    for w in f_tokens:
      roots.append(w)
      if w.endswith("ing"):
          root=re.sub(r'ing$','',w)
          cat=category(root)
          dict[w]=cat
          print(w,cat)
      else:
          cat=category(w)
          dict[w]=cat
          print(w,cat)    return roots
string=input("Enter sentence:")
verbs=tokenize_form(string)
import re
# string=input("Enter string to preprocess:")
#tokenisation
tokens=string.split()

#filtration
f_tokens=[]
for t in tokens:
    w=re.compile(r'[a-zA-Z]+').findall(t)
    f_tokens.extend(w)
print("After resolving ambiguity")
#rules
for w in f_tokens:
    if len(dict[w])>1:
        i=f_tokens.index(w)
        cat=dict[f_tokens[i-1]]
        cat1=dict[f_tokens[i+1]]

        #rule1
        if 'VBN' in dict[w] and'VBD' in dict[w]:
            if(cat==['PRP']):
                print(w, "VBD")
            else:
                print(w, "VBN")
        #rule2        
        if 'NN' in dict[w] and'VB' in dict[w]:
            if(cat==['IN']):
                print(w, "VB")
            else:
                print(w, "NN")
        #rule3  
        if 'NN' in dict[w] and 'VB' in dict[w]:
            if (cat==['DET']):
                print(w, "NN")
            else:
                print(w, "VB")
        #rule4
        if cat!=['VB'] and cat1 in[['JJ'],['ADV'],['QT']]:
            print(w,"ADV")
        elif cat1==['PRP']:
            print(w, "CONJ")
        else:
            print(w,"DET")

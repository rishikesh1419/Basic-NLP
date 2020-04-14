test_list = ['You book a flight', 'I read a book', 'You book']   
print ("The original list is : " + str(test_list)) 
count=0
new_list=[]
for i in test_list: 
    if count==0:
        i="(eos) "+i+" (eos)"        
    else:
        i=i+" (eos)"
    new_list.append(i)
    count+=1
word_list=[]
for i in new_list:
    x=i.split()
    word_list.extend(x)
print("Word list: ",word_list)
print("New list: ",new_list)
res = [(x, i.split()[j + 1]) for i in new_list  
       for j, x in enumerate(i.split()) if j < len(i.split()) - 1]   
print ("The formed bigrams are : " + str(res))

def prob_calc(a,b):
    prob=(res.count((b,a))+1)/(word_list.count(b)+len(set(word_list)))
    return prob
wordset=list(set(word_list))
print("\t",end="")
for i in wordset:
    print("  ",i, end="")
print()
for i in wordset:
    print(i,":\t", end="")
    for j in wordset:
        ans=prob_calc(j,i)
        print("%.3f  "%ans,end="")
    print()


from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
f=open("input.txt")
text=f.read()
tokens=word_tokenize(text)
print("\nTokens are: ",tokens) 

print("\nSTOP WORD REMOVAL: ")
stop_words = set(stopwords.words('english'))
filtered_sentence = [ w for w in tokens if not w in stop_words] 
filtered_sentence = [] 
  
for w in tokens: 
    if w not in stop_words: 
        filtered_sentence.append(w) 

print("Filtered sentence: ",filtered_sentence)

print("\nSTEMMING: ")
stemmer = PorterStemmer()
for word in filtered_sentence:
    print(stemmer.stem(word))

print("\nLEMMATIZATION: ")
lemma= WordNetLemmatizer()
for word in filtered_sentence:
    print(lemma.lemmatize(word))

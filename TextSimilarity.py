import io
import random
import string
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
warnings.filterwarnings('ignore')
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True)

with open('MLCourse.txt','r', encoding='utf8', errors ='ignore') as fin:
	raw = fin.read().lower()

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
lemmer = WordNetLemmatizer()

def LemTokens(tokens):
	return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
	return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are
talking to me"]

def greeting(sentence):
	for word in sentence.split():
		if word.lower() in GREETING_INPUTS:
			return random.choice(GREETING_RESPONSES)

def response(user_response):
	robo_response=''
sent_tokens.append(user_response)
TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
tfidf = TfidfVec.fit_transform(sent_tokens)
vals = cosine_similarity(tfidf[-1], tfidf)
idx=vals.argsort()[0][-2]
flat = vals.flatten()
flat.sort()
req_tfidf = flat[-2]
if(req_tfidf==0):
	robo_response=robo_response+"I am sorry! I don't understand you"
	return robo_response
else:
	robo_response = robo_response+sent_tokens[idx]
	return robo_response

flag=True
print("Bot : Hey, Got any queries?")

while(flag==True):
	user_response = input()
user_response=user_response.lower()

if(user_response!='bye'):
	if(user_response=='thanks' or user_response=='thank you' ):
		flag=False
		print("Bot : You are welcome..")
	else:
		if(greeting(user_response)!=None):
			print("Bot : "+greeting(user_response))
		else:
			print("Bot :",end="")
			print(response(user_response))
	sent_tokens.remove(user_response)
else:
	flag=False
	print("Bot : Bye! Register soon !")

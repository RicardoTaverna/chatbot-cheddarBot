# Projeto II - CheddarBot
# Ricardo Taverna
# Ygor Stengrat 

import nltk
import numpy as np
import random
import string
import mensagens
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

arquivo = open('C:\\Users\\taver\\Desktop\\Projetos\\Interpretadores\\ProjetoII\\chatbot.txt', 'r', errors = 'ignore')

leitura = arquivo.read()
leitura = leitura.lower()

nltk.download('punkt')
nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(leitura)
word_tokens = nltk.word_tokenize(leitura)

#importar mensagens.py

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

def resposta(user_response):
    robo_response=''
    sent_tokens.append(resposta_usuario)    
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


print("CHEEDARBOT: My name is CheedarBot. I'm here to guide you for you buying your pizza. If you want to exit, type Bye!")
while(flag==True):
    resposta_usuario = input()
    resposta_usuario=resposta_usuario.lower()
    if(resposta_usuario!='bye'):
        if(resposta_usuario=='thanks' or resposta_usuario=='thank you' ):
            flag=False
            print("CHEEDARBOT: You are welcome..")
        else:
            if(mensagens.greeting(resposta_usuario)!=None):
                print("CHEEDARBOT: "+mensagens.saldacao(resposta_usuario))
            else:
                print("CHEEDARBOT: ",end="")
                print(resposta(resposta_usuario))
                sent_tokens.remove(resposta_usuario)
    else:
        flag=False
        print("CHEEDARBOT: Bye! take care..")

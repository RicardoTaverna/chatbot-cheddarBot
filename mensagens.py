import nltk
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

respostaPedido = ("yes", "yep", "y", "start", "let's go",) #Reposta Usuario
pedidoResposta = ["Whats size of your pizza? (Small, Medium, Big)"]     #Resposta Bot

def start(sentence):
    for word in sentence.split():
        if word.lower() in respostaPedido:
            return random.choice(pedidoResposta)

respostaTamanho = ("small", "medium", "big",) #Reposta Usuario
tamanhoResposta = ["I would like Stuffed Crust? Cheedar, Catupiry, No"]     #Resposta Bot

def tamanho(sentence):
    for word in sentence.split():
        if word.lower() in respostaTamanho:
            return random.choice(tamanhoResposta)
            

respostaSabor = ("cheedar", "catupiry", "no",) #Reposta Usuario
saborResposta = ["What flavor does your pizza have? \nCheese,\nPepperoni,\nChicken"]     #Resposta Bot

def sabor(sentence):
    for word in sentence.split():
        if word.lower() in respostaSabor:
            return random.choice(saborResposta)
respostaSabor = ("cheedar", "catupiry", "no",) #Reposta Usuario
saborResposta = ["What flavor does your pizza have? \nCheese,\nPepperoni,\nChicken"]     #Resposta Bot

def sabor(sentence):
    for word in sentence.split():
        if word.lower() in respostaSabor:
            return random.choice(saborResposta)
            











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



# Projeto II - CheddarBot
# Ricardo Taverna
# Ygor Stengrat 

import nltk
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

arquivo = open('C:\\Users\\taver\\Desktop\\Projetos\\chatbot-cheddarBot\\chatbot.txt', 'r', errors = 'ignore')


leitura = arquivo.read()
leitura = leitura.lower()

nltk.download('punkt')
nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(leitura)
word_tokens = nltk.word_tokenize(leitura)
lemmer = nltk.stem.WordNetLemmatizer()

# remove pontuação
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

def form():
    adress = input('CHEEDARBOT: Your Adress')
    number = input('CHEEDARBOT: the number of your house')
    phone = input('CHEEDARBOT: your phone number')
    rand = random.randint(10, 99)
    pedido = '#1000'+ str(rand)
    formulario = {'adress': adress, 'number': number, 'phone':phone, 'ticket': pedido}
    return pedido

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

respostaPedido = ("yes", "yep", "y", "start", "let's go",) #Reposta Usuario
pedidoResposta = ["Whats size of your pizza?"] #Resposta Bot

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
            

respostaSaborBorda = ("cheedar", "catupiry", "no",) #Reposta Usuario
saborRespostaBorda = ["What flavor does your pizza have? \nCheese,\nPepperoni,\nChicken"]     #Resposta Bot

def saborBorda(sentence):
    for word in sentence.split():
        if word.lower() in respostaSaborBorda:
            return random.choice(saborRespostaBorda)

respostaSabor = ("cheese", "pepperoni", "chicken",) #Reposta Usuario
saborResposta = ["Do you want to withdraw ah the counter? "]     #Resposta Bot

def sabor(sentence):
    for word in sentence.split():
        if word.lower() in respostaSabor:
            return random.choice(saborResposta)

respostaRetirar = ("yes", "yep", "y", "start", "let's go",) #Reposta Usuario
retirarResposta = ["Type your Address, first yout street (Initialize with street)"]     #Resposta Bot

def entrega(sentence):
    for word in sentence.split():
        if word.lower() in respostaRetirar:
            return random.choice(retirarResposta)


ticket = '#1000'+ str(random.randint(10, 99))    
respostaEntrega = ("no", "n", "nop", "none",)
entregaResposta = ["Ok, your ticket number is " + ticket]

def retirar(sentence):
    for word in sentence.split():
        if word.lower() in respostaEntrega:
            return random.choice(entregaResposta)

respostaNumero = ("street")

print("CHEEDARBOT: My name is CheedarBot. I'm here to guide you for you buying your pizza. If you want to exit, type Bye! If you want to start, type start")

counter = 0
while(flag==True):
    resposta_usuario = input('USER: ')
    resposta_usuario=resposta_usuario.lower()
    if(resposta_usuario!='bye'):
        if(resposta_usuario=='thanks' or resposta_usuario=='thank you' ):
            flag=False
            print("CHEEDARBOT: You are welcome..")
        elif((start(resposta_usuario)!=None) and counter == 0):
            print("CHEEDARBOT: " +start(resposta_usuario))
            counter = counter + 1
        elif((tamanho(resposta_usuario)!=None) and counter == 1):
            print("CHEEDARBOT: " +tamanho(resposta_usuario))
            counter = counter + 1
        elif((saborBorda(resposta_usuario)!=None) and counter == 2):
            print("CHEEDARBOT: " +saborBorda(resposta_usuario))
            counter += 1

        # Empaquei    
        elif((sabor(resposta_usuario)!= None) and counter == 3):
            print("CHEEDARBOT: " +sabor(resposta_usuario))
            counter += 1
            #aqui
            if((retirar(resposta_usuario)!= None)  and counter == 4):
                print("CHEEDARBOT: " +entrega(resposta_usuario))
                ticket = form()
                print('CHEEDARBOT: your ticket is {}'.format(ticket.get(3)))
                counter += 1
            elif((retirar(resposta_usuario)!= None)  and counter == 4):
                print("CHEEDARBOT: " +retirar(resposta_usuario))
        else:
            print("CHEEDARBOT: ",end="")
            print(resposta(resposta_usuario))
            sent_tokens.remove(resposta_usuario)

    else:
        flag=False
        print("CHEEDARBOT: Bye! take care..")

import random

with open('data/shakespere.txt','r',encoding='latin-1') as f:
    lines = f.readlines()

poems = {}

len_poem = 17
num_poems = int(len(lines)/len_poem)
for i in range(num_poems):
    start = i * len_poem
    index = lines[start].strip()
    poem = lines[start+2:start+16]
    poems[index] = poem


for index in poems.keys():
    print(f"{index}{poems[index][0].strip()}")    

model = {}

def clean_word(word):
    word = word.replace(",","")
    word = word.replace("!","")
    word = word.replace("'","")
    word = word.replace(".","")
    word = word.replace("?","")
    word = word.replace("\\n","")
    word = word.lower().strip()

    return word



def addtomodel(sentence):
    global model 
    words = sentence.split(" ")
    for i in range (len(words)-1):
        word = clean_word(words[i])
        after = words[i+1]
        if word in model.keys():
            after_list = model[word]
            if after not in after_list:
                after_list.append(after)
        else:
            model[word] = [after]

def print_model():
    for key, value in model.items():
        print(f"{key}{value}")



for index in poems.keys():
    poem = poems[index]
    for s in poem:
        addtomodel(s)

def poem_maker():
    global model
    poem ={}

    sentence = ""

    word = random.choice(list(model.keys()))

    for j in range (14):
        for i in range(8):
            sentence+=word + " "
            after_list = model[word]
            if len(after_list)==0:
                break
            else:
                word = random.choice(after_list)
        poem.append(sentence)

poem_maker()


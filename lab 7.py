
#part 1
import random


def words(filename):
    fp = open(filename)
    temp_list = list()
    for each_line in fp:
        each_line = each_line.strip()
        temp_list.append(each_line)

    words = tuple(temp_list)
    fp.close()

    return words

articles = Words('articles.txt')
nouns = Words('nouns.txt')
verbs = Words('verbs.txt')
prepositions = Words('prepositions.txt')

def sentence():
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    number = int(input('Enter number of sentences: '))
    for count in range(number):
        print(sentence())


#part 2

import random

hedges=("Please tell me more.",
"Many of my patients tell me the same thing.",
"Please continue.")
qualifiers=("Why do you say that ",
"You seem to think that ",
"Can you explain why ");
replacements={"I":"you","me":"you","my":"your",
"we":"you","us":"you","mine":"yours",
"you":"I","are":"am"}
def T(sentence):
    probability=random.randint(1,4)
    if probability==1:
        return random.choice(hedges)
    return random.choice(qualifiers)+changePerson(sentence)

def B(sentence):
    words=sentence.split()
    replyWords=[]
    for i in range(len(words)):
        if words[i]=="you" and i<len(words)-1 and words[i+1]=="are":
            replyWords.append(replacements.get("you","you"))
            replyWords.append(replacements.get("are","are"))
        elif words[i]=="are" and i>0 and words[i-1]!="you":
            replyWords.append("are")
        elif words[i]=="are" and i>0 and words[i-1]=="you":
            continue
        else:
            replyWords.append(replacements.get(words[i],words[i]))
    return " ".join(replyWords)

def main():
    print('Good morning, I hope you are well today.')
    print('What can I do for you?')
    while True:
        sentence=input("\n>> ")
        if sentence.upper()=="QUIT":
            print("Have a nice day")
            break
        print(reply(sentence))

#part 3

number = 0
with open('text.txt','r') as file:
    data = file.read()
    lines = data.split()
    number+=len(lines)
print(number)

def count(list):
    m ={}
    for item in list:
        if item in m:
            m[item] +=1
        else:
            m[item]=1
    for key, value in m.items():
        print(key,value)
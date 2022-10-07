#f
import random
v = ['Ahmed','Anas','omar','mohammed']
print(random.choice(v))
#g
from random import sample
v = ['Ahmed','Anas','omar','mohammed']
print(sample(v,2))
#h
m = "random statement:WFHEWEFHONSODFK,UIEFNAIENFN"
for i in range(10000):
    print(random.choice(m))

#i
from random import shuffle
player=['Neymar','Salah','cristiano','messi','ronalidinoho','hulk','mohammed','hart']
shuffle(player)
print(player)


#j
from random import shuffle

team_1 = ['Neymar','Salah','cristiano','messi','ronalidinoho','hulk','mohammed','hart']
team_2 = ['Ahmed','Anas','omar','mohammed','samir','othman','khalid','youssef']
shuffle(team_1 +team_2)
print(team_1 +team_2)
#part 1
X=int(input("Enter a Value for 'X': "))
Y=int(input("Enter a Value for 'Y': "))
print("")
list1=[]
for i in range (X):
    list2=[]
    for j in range(Y):
        list2.append(i * j)
    list1.append(list2)

print(list1)
#part 2
p = [40,9,5,6,8,2,92]
even, odd = 0, 0
for jj in p:
    if jj % 2 ==0:
        even += 1
    else:
        odd += 1
print('even numbers:', even)
#part 3

L =[[i,j,k] for i in range(1) for j in range(1) for k in range(2)]
print(L)

#part 4

import random

g = ['1','2','3','4','5','6','7','8','9','10','j','q','k']
dictionary ={}
s = ['club','diamond','heart','spade']
for i in s:
    dictionary[i] = g
for i in dictionary:
    print(i,'-',dictionary[i][random.randint(0,12)])
v = s[random.randint(0, 4)]
print(v, dictionary[v][random.randint(0,12)])

#part 5
numero = [2,4,7,9,9,8,6,5,10]
print('squares of the list:')
new = list(map(lambda x: x**2, numero))
print(new)
print('cube of numbers in list:')
new2 = list(map(lambda x: x**3, numero))
print(new2)

#part 6

from functools import reduce
def p(x,y): return(x+y)
ll = ['eggs','bacon','burger','rice']
lll = ['sprite','cola','juice','water']
meal = reduce(p,ll+lll)
print(meal)

#part 7
def t(n):
    return n*n
list1=[3,4,7,6,9,10]
list2= map(t, list1)
print(list2)
print(list(list2))

#part 8

list_1 =[2,3,4,5,6]
list_2 =[4,5,6,7,8]
answer=map(lambda x, y: x+ y, list_1, list_2)
print('answer is:')
print(list(answer))

#part 9
y = ['my','name','is','anas']
b = list(map(list, y))
print('the list is:')
print(b)

#part 10

numb = [7,-6,4,-8,9,-9,2,7,-1]
nnumb = list(filter(lambda x: x>0, numb))
print('new list is:', nnumb)

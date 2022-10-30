g = {"name": "Anas", "age": 19, "gender": "male", "occupation": "Student"}

print (g["age" ])
print (g.items())
list = []
for x,y in g.items():
    list.append ((x,y))
print (list)
list. sort()
print ("Sorted list",list)
#2

def rec(x):
    if x == 0:
        return x
    print(x)
    return rec(x -1)

print (rec (5))

def rec(w, q =0):
   print(q)
   if q==w:
       return
   rec(w,q + 1)
rec(10)

#3

def poly(x):
    return x ** 3 + 2 * x - 1
n = map(poly, (1,2,3,4))
print("result")
print(n)
for i in n:
   print(i)

#4
newlist = list(map(lambda x: 3*x**4+2*x**2+x, mList))
print ("Using  new function :", newfunclist)



#5

mList = [1, 2, 3, 8, 9, 18, 10, 16,]
nList = list(filter(lambda x: (x % 3 == 0), mList))
print (n_List)

#6

from functools import reduce


def minimum(f, g):
    return f if f < g else g


def maximum(f, g):
    return f if f > g else g


num = [1, 3, 9, 7, 4]
print('the minimum in the list is', reduce(minimum, num))
print ('the maximum in the list is', reduce (maximum, num))
import random
L = []
for i in range(50):
    L.append(random.randint(0,10))
print(L)
for i in range(50):
    L[i]**=2
print(L)
quantity = 0
for i in L:
    if i > 50:
        quantity +=1
print(quantity)
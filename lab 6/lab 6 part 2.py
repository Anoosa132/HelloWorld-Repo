a = ['What is the capital of France?','What is the longest river in the United States?','Which state has only one neighbor?']
b = ['Paris','Mississippi Missouri','Maine']
x = len(a)
i=0
c=[""]*x
while i<x:
    print(a[i])
    n=input('Enter a guess')
    print(n)
    if n ==b[i]:
        print('right')
    else:
        print('wrong')
    c[i]=n
    i=i+1
v=0
count=0
while v<x:
    if c[v]==b[v]:
        count+=1
    v+=1
print('You got '+str(count)+' answers')

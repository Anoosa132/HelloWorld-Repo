f = open('writefile.txt','w')
f.write("My name is summer")
f.close()

r = open('writefile.txt','r')
print(r.read())
fo = open('temps.txt')
f1 = open('ftemps.txt','w+')
for i in range(5):
    c = float(i)
    F = (9*c + (32*5))/5
    f1.write(str(F)+"\n")

f1.close()
fo.close()
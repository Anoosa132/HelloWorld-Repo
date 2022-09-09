for i in range(5):
    print("Hello, my name is Anas")

#part 1
for i in range(3):
    num = eval(input("Enter a number: "))
    print("The square of your number is ", num * num)
print("The loop is done. ")

#pat1(2)
for i in range(5,0,-1):
    print(i, end=' ')
print('Blast off!!')

#part2
for i in range(4):
    print('*'*6)

#part 2(2)
for i in range(8):
    print('*'*(i+1))

#part 3
from random import randint

x = randint(1,10)
print('A number between 1 and 10: ', x)

#part3(2)
from random import randint

num = randint(1,10)

guess = eval(input('Enter your guess: '))

if guess==num:
    print('You got it!')

else:
    print('sorry. The number ', num)
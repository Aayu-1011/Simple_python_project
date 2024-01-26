from random import randint
random_number=randint(0,10)
print(random_number)

x=-1
while x!=random_number:
    if x!=-1:
        print("Wrong guess")
    x=input("enter a number:")
    x=int(x)
print("you guessed correctly")
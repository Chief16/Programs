import random

a = random.randint(1,20)

user = 0
count = 0
cont = True

def game()
while cont:
    user = input("Guess a number: ")
    if user == "exit":
        break
    user = int(user)
    count+=1
    if user > a:
        print("Too High")
    elif user < a:
        print("Too low")
    else:
        print("Correct!")
        print("You got correct in {} guesses".format(count))
        print("-------------------------------------")
        break


    

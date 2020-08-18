import random
a = random.randint(1,9)
guess = 0
count = 0
while guess != a and guess != "exit":
    guess = input(" Guess a number :")
    if guess == "exit" :
        break
    guess = int(guess)
    count += 1
    if guess < a :
     print("you guessed a low number")
    elif guess > a :
        print("You guessed a high Number")
    else :
        print("you guessed Right number")
        print(" And it took only ",count,"tries")

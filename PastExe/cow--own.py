import random
def compare_numbers(number, user_guess):
    cowbull = [0,0]
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1]+=1
        else :
            cowbull[0]+=1
    return cowbull
if __name__=="__main__":
    playing = True
    number = str(random.randint(0,9999))
    guesses = 0

    print("Lets Play a Game !")

    while playing:
        user_guess = input("Guess a 4 digit number : ")
        if user_guess == "exit":
            break
        cowbullcount = compare_numbers(number,user_guess)
        guesses+=1

        print("You have "+ str(cowbullcount[0]) +" cows, and "+ str(cowbullcount[1]) +" bulls. ")

        if cowbullcount[1]==4:
            playing = False
            print("You got the right guess "+ str(number) +" in "+ str(guesses) +" guess. ")
            break
        else:
            print("you got wrong")

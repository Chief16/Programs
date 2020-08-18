import random


def game():
    a = random.randint(1, 11)
    print(a)

    user_guess = 0
    chance = 4

    while True:
        user = int(input("Guess a number: "))
        user_guess += 1
        chance -= 1

        if user == a:
            print("You got it Right!")
            print(f"You got right in {user_guess} Guess with {chance} chances remaining")
            print("------------------------")
            x = input("Want to Play Again? [Y/N] ")
            x.lower()
            if x == "y":
                game()
            else:
                print("Bye Bye!!!")
                break


        elif user != a:
            print("Wrong Guess... Try Again")
            if chance == 0:
                print("Out of Chances")
                print("------------------------")
                x = input("Want to Play Again? [Y/N]  ")
                x.lower()
                if x == "y":
                    game()
                else:
                    print("Bye Bye!!!")
                    break


if __name__ == '__main__':
    game()

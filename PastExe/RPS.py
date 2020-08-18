a = input("What is your name? ")
b = input("What is your name? ")


def rps():
    while True:
        print("-------------Type exit for quiting the game-------------")
        a_ans = input(f"{a}, choose one from rock, paper, scissors : ")
        a_ans=a_ans.lower()
        if a_ans == "exit":
            break
        b_ans = input(f"{b}, choose one from rock, paper, scissors : ")
        b_ans=b_ans.lower()

        if b_ans != "exit":
            if a_ans == b_ans:
                print('its a tie')
            elif a_ans == 'rock':
                if b_ans == 'scissors':
                    print("rock wins")
                else:
                    print("paper wins")
            elif a_ans == 'scissors':
                if b_ans == 'paper':
                    print("scissors wins")
                else:
                    print("rock wins")
            elif a_ans == 'paper':
                if b_ans == 'rock':
                    print("paper wins")
                else:
                    print("scissors wins")
        else:
            break


rps()
print("Thanks For Playing")

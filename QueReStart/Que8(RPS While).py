options = ["ROCK","PAPER","SCISSORS"]
print(options)



while True:
    user1 = input("Choose one Rock, Paper or Scissors: ")
    user2 = input("Choose one Rock, Paper or Scissors: ")
    a = user1.upper()
    b = user2.upper()

    if a == "ROCK" and b == "PAPER":
        print("Congrats User2 won!")
        break
    elif a == "PAPER" and b == "SCISSORS":
        print("Congrats User2 won!")
        break
    elif a == "ROCK" and b == "SCISSORS":
        print("Congrats User1 won!")
        break
    else:
        print("Wrong Input")
    

        
    

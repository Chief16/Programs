'''Please choose one'''


while True:
    user1 = input("Choose one Rock, Paper or Scissors: ")
    user2 = input("Choose one Rock, Paper or Scissors: ")
    a = user1.lower()
    b = user2.lower() 
    
    def rps(a,b):
        if a=="rock":
            if b == "paper":
                print("user2 won")
            else:
                print("user1 won")

        elif a=="paper":
            if b == "scissors":
                print("user2 won")
            else:
                print("user1 won")

        elif a=="scissors":
            if b == "rock":
                print("user2 won")
            else:
                print("user1 won")

        else:
            print("Wrong Input")
rps(a,b)


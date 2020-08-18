num = int(input("Enter the no :" ))
check = int(input("Enter the no :" ))

if num % 4 == 0 :
  print("The no. is multiple of 4")
elif num % 2 == 0:
  print("The number is even no.")
else:
  print("The number is odd no.") 
if num % check == 0:
  print (num, "is divisible of", check)
else:
  print(num, "is not divisible of", check)

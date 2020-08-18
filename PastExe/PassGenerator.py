import random
z = int(input("Enter the digit of password :"))
a = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*?"
passlen = z
result = ' '.join(random.sample(a,passlen))
print(result)

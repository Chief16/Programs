import random
a = int(input("Enter the digit :"))
text = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345677890!@#$%^&*()?"
passlen = a
result = ' '.join(random.sample(text,passlen))
print(result)

name = input("Enter a name: ")
name = name.lower()
c = name[::-1]
if c == name:
    print(True)
else:
    print(False)

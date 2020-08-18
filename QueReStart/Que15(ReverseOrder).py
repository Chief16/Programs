def reversefn(x):
  b = x.split()
  c = " ".join(map(str, b[::-1]))
  print(c)

a = input("Enter the Line: ")
reversefn(a)
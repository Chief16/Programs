def main():
	text =str(input("Enter your name :"))
	var = text.split()
	var.reverse()
	result = ' '.join(var)
	print(result)
main()

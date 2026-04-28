a = input("Enter the first string: ")
b = input("Enter the second string: ")
if a[::-1] == b:
    print("\n",b," is a reverse of ",a)
else:
    print("\n",b," is not a reverse of ",a)

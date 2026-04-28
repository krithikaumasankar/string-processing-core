a = input("Enter the string: ")
print("The substrings are:-")
for i in range(len(a)):
    for j in range(len(a)-i):
        if a[i:j+i+1] != a:
            print(a[i:j+i+1])

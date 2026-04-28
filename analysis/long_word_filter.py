s = input("Enter the string: ").split(" ")
found = 0
for s in s:
    if len(s) > 5:
        print(s)
        found += 1
if not found:
    print("There is no five letter word...")

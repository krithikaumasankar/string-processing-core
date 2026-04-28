s1 = input("Enter a string: ")
s2 = input("Enter another string: ")
if len(s1) == len(s2) and s2 in (s1+s1):
    print("The second string is a rotational of first string")
else:
    print("The second string is not a rotational of first string")

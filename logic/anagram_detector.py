a = input("Enter first word: ")
b = input("Enter second word: ")

if sorted(a) == sorted(b):
    print("It is an anagram")
else:
    print("It is not an anagram")

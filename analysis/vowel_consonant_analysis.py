a = input("Enter a string: ")
v = 0
c = 0

for i in range(len(a)):
    if a[i].isalpha():
        if a[i] in "aeiouAEIOU":
            v += 1
        else:
            c += 1

print("\nVowels:", v)
print("Consonants:", c)

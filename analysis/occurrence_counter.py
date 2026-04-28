a = input("Enter string: ")
visited = []

for ch in a:
    if ch not in visited:
        count = a.count(ch)		# object.count(value)
        print(ch, "appears", count, "times")
        visited.append(ch)		# list_name.append(value)

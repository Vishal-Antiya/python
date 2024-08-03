items = ["apple", "banana", "orange", "apple", "mango"]
duplicate = set()

for i in items:
    if i in duplicate:
        print(i)
        break
    duplicate.add(i)
    

input = "broorf"
op = ""

for i in input:
    if input.count(i)==1:
        op += i
        break
print(op)

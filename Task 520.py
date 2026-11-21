line = input("Enter line: ")

upper = 0
lower = 0

for c in line:
    if c.isupper():
        upper += 1
    elif c.islower():
        lower += 1

print("UPPER CASE", upper)
print("LOWER CASE", lower) 
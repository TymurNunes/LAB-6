words = input().split()

maximum = 0

for word in words:
    if len(word) > maximum:
        maximum = len(word)

print(maximum)
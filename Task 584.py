numbers = list(map(int, input().split()))
repeated = []

for n in numbers:
    if numbers.count(n) > 1 and n not in repeated:
        repeated.append(n)

print(*repeated)
n = int(input())
total = 0
counter = 0

for i in range(n):
    num = float(input())
    total += num
    counter += 1

average = total / counter

print(f"{average:.2f}")
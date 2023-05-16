n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    num = int(input())
    if num < 200:
        p1 += 1
    if 200 <= num <= 399:
        p2 += 1
    if 400 <= num <= 599:
        p3 += 1
    if 600 <= num <= 799:
        p4 += 1
    if num >= 800:
        p5 += 1

p1_total = p1 / n * 100
p2_total = p2 / n * 100
p3_total = p3 / n * 100
p4_total = p4 / n * 100
p5_total = p5 / n * 100

print(f"{p1_total:.2f}%")
print(f"{p2_total:.2f}%")
print(f"{p3_total:.2f}%")
print(f"{p4_total:.2f}%")
print(f"{p5_total:.2f}%")
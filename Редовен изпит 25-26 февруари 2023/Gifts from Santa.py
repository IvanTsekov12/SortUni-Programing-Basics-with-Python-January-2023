n = int(input())
m = int(input())
s = int(input())

for house in range(m, n - 1, -1):
    if house % 2 == 0 and house % 3 == 0:
        if house == s:
            break
        else:
            print(house, end=" ")
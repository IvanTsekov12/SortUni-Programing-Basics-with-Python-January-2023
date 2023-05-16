n = int(input())
is_bigger = False
current = 1

for rows in range(1, n + 1):
    for col in range(1, rows + 1):

        if current > n:
            is_bigger = True
            break
        print(str(current) + ' ', end="")
        current += 1
    if is_bigger:
        break
    print()

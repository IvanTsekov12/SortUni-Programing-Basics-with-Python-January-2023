number = int(input())
number = str(number)
for i in range(1, int(number[2]) + 1):
    for n in range(1, int(number[1]) + 1):
        for d in range(1, int(number[0]) + 1):
            print(f"{i} * {n} * {d} = {i * n * d};")

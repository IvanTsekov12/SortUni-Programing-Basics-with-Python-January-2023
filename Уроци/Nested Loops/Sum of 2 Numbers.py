start = int(input())
end = int(input())
magic_num = int(input())
counter = 0
breaker = False

for num1 in range(start, end+ 1 ):
    for num2 in range(start, end + 1):
        counter += 1

        if num1 + num2 == magic_num:
            breaker = True
            print(f"Combination N:{counter} ({num1} + {num2} = {num1 + num2})")
            break
    if breaker:
        break

if not breaker:
    print(f"{counter} combinations - neither equals {magic_num}")

from sys import maxsize

numbers_line = int(input())

last_sum = -maxsize
diff_num = -maxsize

for num in range(numbers_line):
    numbers = int(input())
    numbers2 = int(input())

    new_sum = numbers + numbers2
    if num == 0:
        last_sum = new_sum

    if last_sum != new_sum:
        if abs(last_sum - new_sum) > 0:
            diff_num = abs(new_sum - last_sum)

        last_sum = new_sum

if diff_num == -maxsize:
    print(f"Yes, value={last_sum}")

else:
    print(f"No, maxdiff={diff_num}")
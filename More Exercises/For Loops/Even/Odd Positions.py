from sys import maxsize

n = int(input())
even_sum = 0
odd_sum = 0
even_max_num = -maxsize
odd_min_num = maxsize
even_min_num = maxsize
odd_max_num = -maxsize
even_nums = 0
odd_nums = 0

for i in range(1, n + 1):
    num = float(input())
    if i % 2 == 0:
        even_sum += num
        even_nums += 1
    else:
        odd_sum += num
        odd_nums += 1
    if i % 2 == 0 and num > even_max_num:
        even_max_num = num
    elif i % 2 != 0 and num > odd_max_num:
        odd_max_num = num
    if i % 2 == 0 and num < even_min_num:
        even_min_num = num
    elif i % 2 != 0 and num < odd_min_num:
        odd_min_num = num

print(f"OddSum={odd_sum:.2f},")
if odd_nums == 0:
    print(f"OddMin=No,")
    print(f"OddMax=No,")
else:
    print(f"OddMin={odd_min_num:.2f},")
    print(f"OddMax={odd_max_num:.2f},")

print(f"EvenSum={even_sum:.2f},")
if even_nums == 0:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
else:
    print(f"EvenMin={even_min_num:.2f},")
    print(f"EvenMax={even_max_num:.2f}")

import sys

n = int(input())
sum_nums = 0
max_num = -sys.maxsize

for i in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_nums += num

if max_num == sum_nums - max_num:
    sum_nums -= max_num
    print("Yes")
    print(f"Sum = {sum_nums}")
else:
    print("No")
    sum_nums -= max_num
    print(f"Diff = {abs(max_num - sum_nums)}")
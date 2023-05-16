n = int(input())

total_grade = 0
total_grade_sum = 0

while True:
    command = input()
    if command == "Finish":
        break

    grdes_sum = 0

    for _ in range(n):
        grdes_sum += float(input())

    total_grade_sum += grdes_sum
    total_grade += n

    print(f"{command} - {grdes_sum / n:.2f}.")

print(f"Student's final assessment is {total_grade_sum / total_grade:.2f}.")
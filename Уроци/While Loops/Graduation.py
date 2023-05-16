name = input()
grades_counter = 0
years_counter = 0
failed_counter = 0

while True:
    current_grade = float(input())

    if current_grade < 4:
        failed_counter += 1
        if failed_counter == 2:
            print(f"{name} has been excluded at {years_counter + 1} grade")
            break

    else:
        years_counter += 1
        grades_counter += current_grade

        if years_counter == 12:
            average = grades_counter / 12
            print(f"{name} graduated. Average grade: {average:.2f}")
            break

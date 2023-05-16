bad_grades = int(input())
bad_grades_counter = 0
problem_counter = 0
total_grades = 0
last_problem = ""

while True:
    command = input()
    if command == "Enough":
        print(f"Average score: {(total_grades / problem_counter):.2f}")
        print(f"Number of problems: {problem_counter}")
        print(f"Last problem: {last_problem}")
        break
    grade = int(input())
    total_grades += grade
    if command != "Enough":
        last_problem = command
    if grade <= 4:
        bad_grades_counter += 1
    if command != "Enough" or bad_grades_counter < bad_grades:
        problem_counter += 1
    if bad_grades_counter >= bad_grades:
        print(f"You need a break, {bad_grades_counter} poor grades.")
        break



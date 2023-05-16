students = int(input())

bad_grades = 0
medium_grades = 0
good_grades = 0
very_good_grades = 0
total = 0

for i in range(students):
    grade = float(input())
    total += grade
    if 2.00 <= grade <= 2.99:
        bad_grades += 1
    elif 3 <= grade <= 3.99:
        medium_grades += 1
    elif 4 <= grade <= 4.99:
        good_grades += 1
    elif grade >= 5:
        very_good_grades += 1

average = total / students
bad_percents = (bad_grades / students) * 100
medium_percents = (medium_grades / students) * 100
good_percents = (good_grades / students) * 100
very_good_percents = (very_good_grades / students) * 100

print(f"Top students: {very_good_percents:.2f}%")
print(f"Between 4.00 and 4.99: {good_percents:.2f}%")
print(f"Between 3.00 and 3.99: {medium_percents:.2f}%")
print(f"Fail: {bad_percents:.2f}%")
print(f"Average: {average:.2f}")
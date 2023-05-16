mins = 0
hours = 0

while True:
    if mins == 60:
        hours += 1
        mins = 0
    print(f"{hours} : {mins}")
    mins += 1
    if hours == 23 and mins > 59:
        break

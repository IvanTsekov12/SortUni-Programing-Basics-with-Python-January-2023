secs = 0
mins = 0
hours = 0

while True:
    if secs == 60:
        mins += 1
        secs = 0
    if mins == 60:
        hours += 1
        mins = 0
    print(f"{hours} : {mins} : {secs}")
    secs += 1
    if hours == 23 and mins == 59 and secs > 59:
        break

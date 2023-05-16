season = input()
group_type = input()
students = int(input())
nights = int(input())
total = 0
sport = ""

if season == "Winter":
    if group_type == "boys" or group_type == "girls":
        total = nights * 9.6 * students
    elif group_type == "mixed":
        total = nights * 10 * students
    if group_type == "girls":
        sport = "Gymnastics"
    elif group_type == "boys":
        sport = "Judo"
    elif group_type == "mixed":
        sport = "Ski"
elif season == "Spring":
    if group_type == "boys" or group_type == "girls":
        total = nights * 7.2 * students
    elif group_type == "mixed":
        total = nights * 9.5 * students
    if group_type == "girls":
        sport = "Athletics"
    elif group_type == "boys":
        sport = "Tennis"
    elif group_type == "mixed":
        sport = "Cycling"
elif season == "Summer":
    if group_type == "boys" or group_type == "girls":
        total = nights * 15 * students
    elif group_type == "mixed":
        total = nights * 20 * students
    if group_type == "girls":
        sport = "Volleyball"
    elif group_type == "boys":
        sport = "Football"
    elif group_type == "mixed":
        sport = "Swimming"
if students >= 50:
    total = total - (total * 0.5)
elif 20 <= students < 50:
    total = total - (total * 0.15)
elif 10 <= students < 20:
    total = total - (total * 0.05)

print(f"{sport} {total:.2f} lv.")
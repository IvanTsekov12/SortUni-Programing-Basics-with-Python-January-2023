groups = int(input())
total_people = 0

musala = 0
monblan = 0
kilimandzharo = 0
k2 = 0
everest = 0

musala_total = 0
monblan_total = 0
kilimandzharo_total = 0
k2_total = 0
everest_total = 0

for members in range(groups):
    members_count = int(input())
    total_people += members_count
    if members_count <= 5:
        musala += members_count
    elif 6 <= members_count <= 12:
        monblan += members_count
    elif 13 <= members_count <= 25:
        kilimandzharo += members_count
    elif 26 <= members_count <= 40:
        k2 += members_count
    elif members_count >= 41:
        everest += members_count

musala_total = (musala / total_people) * 100
monblan_total = (monblan / total_people) * 100
kilimandzharo_total = (kilimandzharo / total_people) * 100
k2_total = (k2 / total_people) * 100
everest_total = (everest / total_people) * 100

print(f"{musala_total:.2f}%")
print(f"{monblan_total:.2f}%")
print(f"{kilimandzharo_total:.2f}%")
print(f"{k2_total:.2f}%")
print(f"{everest_total:.2f}%")
floors = int(input())
ap_per_floor = int(input())

ap_name = ""
ap_num = 0
for cr_floor in range(floors, 0, -1):
    for num in range(ap_per_floor):
        apa_num = cr_floor * 10 + num
        if cr_floor == floors:
            ap_name = f"L{apa_num}"
        elif cr_floor % 2 == 0:
            ap_name = f"O{apa_num}"
        elif cr_floor % 2 != 0:
            ap_name = f"A{apa_num}"
        print(ap_name, end=" ")
    print()

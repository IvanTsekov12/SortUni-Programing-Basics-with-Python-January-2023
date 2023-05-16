stadium_capacity = int(input())
fans = int(input())
sector_A = 0
sector_B = 0
sector_V = 0
sector_G = 0

for _ in range(fans):
    sector = input()
    if sector == "A":
        sector_A += 1
    elif sector == "B":
        sector_B += 1
    elif sector == "V":
        sector_V += 1
    elif sector == "G":
        sector_G += 1

sector_A_total = (sector_A / fans) * 100
sector_B_total = (sector_B / fans) * 100
sector_V_total = (sector_V / fans) * 100
sector_G_total = (sector_G / fans) * 100
fans_to_capacity = (fans / stadium_capacity) * 100

print(f"{sector_A_total:.2f}%")
print(f"{sector_B_total:.2f}%")
print(f"{sector_V_total:.2f}%")
print(f"{sector_G_total:.2f}%")
print(f"{fans_to_capacity:.2f}%")
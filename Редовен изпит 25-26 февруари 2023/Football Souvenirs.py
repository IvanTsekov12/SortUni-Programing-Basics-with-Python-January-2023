team = input()
souvenir_type = input()
souvenir_count = int(input())
total = 0

if team == "Argentina":
    if souvenir_type == "flags":
        total = souvenir_count * 3.25
        print(f"Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.")
    elif souvenir_type == "caps":
        total = souvenir_count * 7.2
        print(f"Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.")
    elif souvenir_type == "posters":
        total = souvenir_count * 5.1
        print(f"Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.")
    elif souvenir_type == "stickers":
        total = souvenir_count * 1.25
        print(f"Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.")
    else:
        print("Invalid stock!")
elif team == "Brazil":
    if souvenir_type == "flags":
        total = souvenir_count * 4.2
        print(f"Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.")
    elif souvenir_type == "caps":
        total = souvenir_count * 8.5
        print(f"Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.")
    elif souvenir_type == "posters":
        total = souvenir_count * 5.35
        print(f"Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.")
    elif souvenir_type == "stickers":
        total = souvenir_count * 1.2
        print(f"Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.")
    else:
        print("Invalid stock!")
elif team == "Croatia":
    if souvenir_type == "flags":
        total = souvenir_count * 2.75
        print(f"Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.")
    elif souvenir_type == "caps":
        total = souvenir_count * 6.9
        print(f"Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.")
    elif souvenir_type == "posters":
        total = souvenir_count * 4.95
        print(f"Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.")
    elif souvenir_type == "stickers":
        total = souvenir_count * 1.1
        print(f"Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.")
    else:
        print("Invalid stock!")
elif team == "Denmark":
    if souvenir_type == "flags":
        total = souvenir_count * 3.1
        print(f"Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.")
    elif souvenir_type == "caps":
        total = souvenir_count * 6.5
        print(f"Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.")
    elif souvenir_type == "posters":
        total = souvenir_count * 4.8
        print(f"Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.")
    elif souvenir_type == "stickers":
        total = souvenir_count * 0.9
        print(f"Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.")
    else:
        print("Invalid stock!")
else:
    print("Invalid country!")

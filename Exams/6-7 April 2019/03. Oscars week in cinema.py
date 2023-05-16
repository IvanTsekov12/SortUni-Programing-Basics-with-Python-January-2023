movie_name = input()
salon_type = input()
tickets_bought = int(input())

total = 0

if salon_type == "normal":
    if movie_name == "A Star Is Born":
        total = tickets_bought * 7.5
    elif movie_name == "Bohemian Rhapsody":
        total = tickets_bought * 7.35
    elif movie_name == "Green Book":
        total = tickets_bought * 8.15
    elif movie_name == "The Favourite":
        total = tickets_bought * 8.75
elif salon_type == "luxury":
    if movie_name == "A Star Is Born":
        total = tickets_bought * 10.5
    elif movie_name == "Bohemian Rhapsody":
        total = tickets_bought * 9.45
    elif movie_name == "Green Book":
        total = tickets_bought * 10.25
    elif movie_name == "The Favourite":
        total = tickets_bought * 11.55
elif salon_type == "ultra luxury":
    if movie_name == "A Star Is Born":
        total = tickets_bought * 13.5
    elif movie_name == "Bohemian Rhapsody":
        total = tickets_bought * 12.75
    elif movie_name == "Green Book":
        total = tickets_bought * 13.25
    elif movie_name == "The Favourite":
        total = tickets_bought * 13.95

print(f"{movie_name} -> {total:.2f} lv.")
bottles = int(input())
total_detergent = bottles * 750
counter = 0
dishes = 0
pots = 0

while True:
    counter += 1
    for_washing = input()

    if for_washing != "End":
        for_washing = int(for_washing)
        if counter % 3 != 0:
            needed_detergent = for_washing * 5
            total_detergent -= needed_detergent
            dishes += for_washing
        else:
            needed_detergent = for_washing * 15
            total_detergent -= needed_detergent
            pots += for_washing
    if total_detergent >= 0 and for_washing == "End":
        print("Detergent was enough!")
        print(f"{dishes} dishes and {pots} pots were washed.")
        print(f"Leftover detergent {total_detergent} ml.")
        break
    elif total_detergent < 0:
        print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")
        break


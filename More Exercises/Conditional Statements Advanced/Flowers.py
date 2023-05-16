hrizantemi = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
total = 0
total_flowers = hrizantemi + tulips + roses

hrizantemi_price = 0
roses_price = 0
tulips_price = 0

if season == "Spring" or season == "Summer":
    if holiday == "Y":
        hrizantemi_price = 2 + (2 * 0.15)
        roses_price = 4.1 + (4.1 * 0.15)
        tulips_price = 2.5 + (2.5 * 0.15)
        total = (roses * roses_price) + \
                (hrizantemi * hrizantemi_price) + \
                (tulips * tulips_price)
    elif holiday == "N":
        hrizantemi_price = 2
        roses_price = 4.1
        tulips_price = 2.5
        total = (roses * roses_price) + \
                (hrizantemi * hrizantemi_price) + \
                (tulips * tulips_price)
    if tulips > 7 and season == "Spring":
        total = total - (total * 0.05)
    if total_flowers > 20:
        total = total - (total * 0.2)
elif season == "Autumn" or season == "Winter":
    if holiday == "Y":
        hrizantemi_price = 3.75 + (3.75 * 0.15)
        roses_price = 4.5 + (4.5 * 0.15)
        tulips_price = 4.15 + (4.15 * 0.15)
        total = (roses * roses_price) + \
                (hrizantemi * hrizantemi_price) + \
                (tulips * tulips_price)
    elif holiday == "N":
        hrizantemi_price = 3.75
        roses_price = 4.5
        tulips_price = 4.15
        total = (roses * roses_price) + \
                (hrizantemi * hrizantemi_price) + \
                (tulips * tulips_price)
    if roses >= 10 and season == "Winter":
        total = total - (total * 0.1)
    if total_flowers > 20:
        total = total - (total * 0.2)
print(f"{(total + 2):.2f}")
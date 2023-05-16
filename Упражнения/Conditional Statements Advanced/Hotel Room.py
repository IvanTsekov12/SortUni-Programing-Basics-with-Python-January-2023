month = input()
stays = int(input())
studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50 * stays
    apartment = 65 * stays
    if stays > 7 and stays <= 14:
        studio = studio - (studio * 0.05)
    elif stays > 14:
        studio = studio - (studio * 0.3)
        apartment = apartment - (apartment * 0.1)
elif month == "June" or month == "September":
    studio = 75.2 * stays
    apartment = 68.7 * stays
    if stays > 14:
        studio = studio - (studio * 0.2)
        apartment = apartment - (apartment * 0.1)
elif month == "July" or month == "August":
    studio = 76 * stays
    apartment = 77 * stays
    if stays > 14:
        apartment = apartment - (apartment * 0.1)

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")
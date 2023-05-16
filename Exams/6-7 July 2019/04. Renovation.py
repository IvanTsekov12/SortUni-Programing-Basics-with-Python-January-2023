height = int(input())
width = int(input())
not_painted = int(input()) / 100
total = height * width * 4
total2 = total - (total * not_painted)

while True:
    paint = input()
    if paint != "Tired!":
        paint = int(paint)
        total2 -= paint
    else:
        print(f"{int(total2)} quadratic m left.")
        break
    if total2 < 0:
        print(f"All walls are painted and you have {int(abs(total2))} l paint left!")
        break
    elif total2 == 0:
        print("All walls are painted! Great job, Pesho!")
        break
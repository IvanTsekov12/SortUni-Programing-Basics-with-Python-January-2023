kilometers = int(input())
time_of_day = input()

if kilometers < 20 :
    if time_of_day == "day":
        print(f"{(kilometers * 0.79) + 0.7:.2f}")
    elif time_of_day == "night":
        print(f"{(kilometers * 0.9) + 0.7:.2f}")
elif 20 <= kilometers < 100:
    print(f"{kilometers * 0.09:.2f}")
else:
    print(f"{kilometers * 0.06:.2f}")
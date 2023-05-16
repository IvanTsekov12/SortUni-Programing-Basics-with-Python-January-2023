days_off  = int(input())

working_days = 365 - days_off

playtime_working_days = working_days * 63
playtime_days_off = days_off * 127
total_playtime = playtime_days_off + playtime_working_days

if total_playtime <= 30000:
    time_left = 30000 - total_playtime
    print("Tom sleeps well")
    print(f"{time_left // 60} hours and {time_left % 60} minutes less for play")
else:
    time_left = total_playtime - 30000
    print("Tom will run away")
    print(f"{time_left // 60} hours and {time_left % 60} minutes more for play")
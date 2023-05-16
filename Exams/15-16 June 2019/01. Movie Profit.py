movie_name = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
cinema_percentage = int(input()) / 100

daily_income = tickets * ticket_price
total_income = days * daily_income

total = total_income * (1 - cinema_percentage)

print(f"The profit from the movie {movie_name} is {total:.2f} lv.")
import sys

movies_count = int(input())

total = 0

highest_rating = 0
lowest_rating = sys.maxsize

highest_movie = ""
lowest_movie = ""

for _ in range(movies_count):
    movie_name = input()
    movie_rating = float(input())
    if movie_rating > highest_rating:
        highest_rating = movie_rating
        highest_movie = movie_name
    elif movie_rating < lowest_rating and movie_rating < highest_rating:
        lowest_rating = movie_rating
        lowest_movie = movie_name
    total += movie_rating

average_rating = total / movies_count

print(f"{highest_movie} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")



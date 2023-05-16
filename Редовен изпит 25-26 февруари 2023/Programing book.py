one_page_price = float(input())
one_cover_price = float(input())
discount = int(input()) / 100
designer_price = float(input())
from_team = int(input()) / 100

total_price = (one_page_price * 899) + (one_cover_price * 2)
discounted_price = total_price - (total_price * discount)
new_sum = discounted_price + designer_price
final_sum = new_sum - (new_sum * from_team)

print(f"Avtonom should pay {final_sum:.2f} BGN.")
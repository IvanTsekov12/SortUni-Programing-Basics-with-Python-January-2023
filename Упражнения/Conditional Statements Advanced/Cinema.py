type = input()
rows = int(input())
columns = int(input())
ticket_price = 0
total = 0

if type == "Premiere":
    ticket_price = 12
    total = (columns * rows) * ticket_price
elif type == "Normal":
    ticket_price = 7.5
    total = (columns * rows) * ticket_price
elif type == "Discount":
    ticket_price = 5
    total = (columns * rows) * ticket_price

print(f"{total:.2f} leva")
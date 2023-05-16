h = float(input())
w = float(input())
width_without_coridor = w - 1
desk = 70
desk_count = (width_without_coridor * 100) // desk
rows = 120
rows_count = (h * 100) // rows
total_desks = desk_count * desk
total_rows = rows_count * rows
seats = (rows_count * desk_count) - 3
print(seats)

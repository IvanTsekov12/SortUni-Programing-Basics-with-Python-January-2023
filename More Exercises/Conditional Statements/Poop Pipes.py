v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_filled = p1 * h
p2_filled = p2 * h
total_filled = p1_filled + p2_filled

if total_filled <= v:
    print(f"The pool is {total_filled / (v/100):.2f}% full. Pipe 1: {p1_filled / (total_filled/100):.2f}%. Pipe 2: {p2_filled / (total_filled/100):.2f}%.")
else:
    print(f"For {h:.2f} hours the pool overflows with {total_filled - v:.2f} liters.")
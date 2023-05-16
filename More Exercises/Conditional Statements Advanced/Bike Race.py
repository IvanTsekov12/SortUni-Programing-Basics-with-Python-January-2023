juniors = int(input())
seniors = int(input())
trace_type = input()
total_contestents = juniors + seniors
juniors_total = 0
seniors_total = 0
total = 0

if trace_type == "trail":
    juniors_total = juniors * 5.5
    seniors_total = seniors * 7
    total = juniors_total + seniors_total
elif trace_type == "cross-country":
    if total_contestents < 50:
        juniors_total = juniors * 8
        seniors_total = seniors * 9.5
        total = juniors_total + seniors_total
    elif total_contestents >= 50:
        juniors_total = juniors * 8
        seniors_total = seniors * 9.5
        juniors_total = juniors_total - (juniors_total * 0.25)
        seniors_total = seniors_total - (seniors_total * 0.25)
        total = juniors_total + seniors_total
elif trace_type == "downhill":
    juniors_total = juniors * 12.25
    seniors_total = seniors * 13.75
    total = juniors_total + seniors_total
elif trace_type == "road":
    juniors_total = juniors * 20
    seniors_total = seniors * 21.5
    total = juniors_total + seniors_total
total = total - (total * 0.05)
print(f"{total:.2f}")

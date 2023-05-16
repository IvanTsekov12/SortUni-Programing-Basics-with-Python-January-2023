number = int(input())
isvalid = (number >= 100 and number <= 200) or number == 0

if not(isvalid):
    print("invalid")
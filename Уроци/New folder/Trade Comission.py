city = input()
sales = float(input())
commission = 0

if city == "Sofia":
    if sales >= 0 and sales <= 500:
        commission = sales * 0.05
        print(f"{commission:.2f}")
    elif sales > 500 and sales <= 1000:
        commission = sales * 0.07
        print(f"{commission:.2f}")
    elif sales > 1000 and sales <= 10000:
        commission = sales * 0.08
        print(f"{commission:.2f}")
    elif sales > 10000:
        commission = sales * 0.12
        print(f"{commission:.2f}")
    else:
        print("error")
elif city == "Varna":
    if sales >= 0 and sales <= 500:
        commission = sales * 0.045
        print(f"{commission:.2f}")
    elif sales > 500 and sales <= 1000:
        commission = sales * 0.075
        print(f"{commission:.2f}")
    elif sales > 1000 and sales <= 10000:
        commission = sales * 0.1
        print(f"{commission:.2f}")
    elif sales > 10000:
        commission = sales * 0.13
        print(f"{commission:.2f}")
    else:
        print("error")
elif city == "Plovdiv":
    if sales >= 0 and sales <= 500:
        commission = sales * 0.055
        print(f"{commission:.2f}")
    elif sales > 500 and sales <= 1000:
        commission = sales * 0.08
        print(f"{commission:.2f}")
    elif sales > 1000 and sales <= 10000:
        commission = sales * 0.12
        print(f"{commission:.2f}")
    elif sales > 10000:
        commission = sales * 0.145
        print(f"{commission:.2f}")
    else:
        print("error")
else:
    print("error")
tabs_opened = int(input())
salary = int(input())

for tax in range(tabs_opened):
    tab_name = input()
    if tab_name == "Facebook":
        salary -= 150
    elif tab_name == "Instagram":
        salary -= 100
    elif tab_name == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(abs(salary))



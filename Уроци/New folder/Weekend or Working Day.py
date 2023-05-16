day = input()

if day == "Monday" or day == "Tuesday" or day == "Wednesday" \
        or day == "Thursday" or day == "Friday":
    print("Working day")
elif day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Error")

# if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
#     print("Working day")
# elif day in ["Saturday","Sunday" ]:
#     print("Weekend")
# else:
#     print("Error")




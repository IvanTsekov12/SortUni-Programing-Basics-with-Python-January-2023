student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0

while True:
    command = input()
    if command == "Finish":
        break

    free_spaces = int(input())
    temp_total_tickets = 0

    for _ in range(free_spaces):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "standard":
            total_tickets += 1
            standard_tickets += 1
            temp_total_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
            total_tickets += 1
            temp_total_tickets += 1
        elif ticket_type == "student":
            student_tickets += 1
            total_tickets += 1
            temp_total_tickets += 1
        elif ticket_type == "End":
            break
    print(f"{command} - {(temp_total_tickets / free_spaces) * 100:.2f}% full.")
print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kid_tickets / total_tickets) * 100:.2f}% kids tickets.")
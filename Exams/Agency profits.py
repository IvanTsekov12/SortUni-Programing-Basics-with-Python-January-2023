company_name = input()
adult_tickets = int(input())
children_tickets = int(input())
adult_ticket_price = float(input())
tax = float(input())

children_ticket_price = (adult_ticket_price - (adult_ticket_price * 0.7)) + tax
adult_ticket_price += tax

total = (adult_ticket_price * adult_tickets) + (children_ticket_price * children_tickets)
total = total * 0.2

print(f"The profit of your agency from {company_name} tickets is {total:.2f} lv.")

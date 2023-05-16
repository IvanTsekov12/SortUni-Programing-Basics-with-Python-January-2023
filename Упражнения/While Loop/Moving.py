free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())
total_free_space = free_space_height * free_space_width * free_space_length
needed_space = 0

while True:
    boxes = input()
    if boxes != "Done":
        boxes = int(boxes)
        needed_space += boxes
    if needed_space > total_free_space and boxes != "Done":
        print(f"No more free space! You need {abs(total_free_space - needed_space)} Cubic meters more.")
        break
    elif needed_space <= total_free_space and boxes == "Done":
        print(f"{abs(needed_space - total_free_space)} Cubic meters left.")
        break

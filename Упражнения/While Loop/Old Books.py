fav_book = input()
book_counter = 0

while True:
    book = input()
    if book == fav_book:
        print(f"You checked {book_counter} books and found it.")
        break
    if book == "No More Books":
        print(f"The book you search is not here!\nYou checked {book_counter} books.")
        break
    if book != fav_book and book != "No More Books":
        book_counter += 1

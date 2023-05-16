import string

al_letters = string.punctuation
word = ""
n_counter = 0
o_counter = 0
c_counter = 0
temp_word = ""

while True:
    command = input()
    is_letter = 'a' <= command <= 'z' or 'A' <= command <= 'Z'
    if command != "End":
        if command == "n" and n_counter < 1:
            n_counter += 1
            continue
        elif command == "o" and o_counter < 1:
            o_counter += 1
            continue
        elif c_counter < 1 and command == "c":
            c_counter += 1
            continue
        if not is_letter:
            continue
    if n_counter == 1 and o_counter == 1 and c_counter == 1:
        o_counter = 0
        n_counter = 0
        c_counter = 0
        word += " "
        temp_word = ""
    word += command
    temp_word += command
    if command == "End" and (n_counter < 1 or o_counter < 1 or c_counter < 1):
        if word.__contains__(temp_word):
            word = word.replace(temp_word, "")
            break
print(word)


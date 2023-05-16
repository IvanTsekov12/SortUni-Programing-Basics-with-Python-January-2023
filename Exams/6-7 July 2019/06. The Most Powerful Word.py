power = 0
powerful_word = ""

while True:
    word = input()
    if word == "End of words":
        break
    temp_power = 0
    for i in range(len(word)):
        temp_power += ord(word[i])
    if (word[0] == 'A' or word[0] == 'E' or word[0] == 'I' or word[0] == 'U' or word[0] == 'Y' or word[0] == 'O') \
            or (word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'u' or word[0] == 'y' or word[0] == 'o'):
        temp_power *= len(word)
    else:
        temp_power //= len(word)
    if temp_power > power:
        power = temp_power
        powerful_word = word

print(f"The most powerful word is {powerful_word} - {power} ")

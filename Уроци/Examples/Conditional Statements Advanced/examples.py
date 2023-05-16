# # number = int(input())
# #
# # if number > 0:
# #     pass
# #     if number == 0:
# #         print("Zero")
# #     else:
# #         print("Positive")
# # else:
# #     print("Negative")
#
#
# import string
#
# main_string = string.ascii_letters
# first_word = ''
# final_string = ''
#
# c_counter = 0
# o_counter = 0
# n_counter = 0
#
# end = 'End'
#
# while end == "End":
#     if c_counter >= 1 and o_counter >= 1 and n_counter >= 1:
#         first_word += ' '
#         final_string += first_word
#         first_word = ''
#         c_counter = 0
#         o_counter = 0
#         n_counter = 0
#         letter_count = 0
#
#     letter = input()
#
#     if letter == "End":
#         break
#
#     if letter == 'C' or letter == 'c':
#         c_counter += 1
#
#         if c_counter > 1:
#             first_word += letter
#         continue
#
#     if letter == 'O' or letter == 'o':
#         o_counter += 1
#
#         if o_counter > 1:
#             first_word += letter
#         continue
#
#     if letter == 'N' or letter == 'n':
#         n_counter += 1
#
#         if n_counter > 1:
#             first_word += letter
#         continue
#
#     if letter in main_string:
#         first_word += letter
#
# print(final_string)

count_c = 0
count_o = 0
count_n = 0
word = ''
new_word = ''

command = input()
while command != 'End':
    if 'a' <= command <= 'z' or 'A' <= command <= 'Z':
        if command == 'n' and count_n == 0:
            count_n += 1
        elif command == 'c' and count_c == 0:
            count_c += 1
        elif command == 'o' and count_o == 0:
            count_o += 1
        else:
            word += command

        if count_o == 1 and count_c == 1 and count_n == 1:
            new_word = new_word + word + ' '

            word = ''
            count_n = 0
            count_o = 0
            count_c = 0

    command = input()

print(new_word)
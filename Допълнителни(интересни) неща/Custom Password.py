from string import ascii_letters, digits, punctuation
import random

signs_combination = ascii_letters + digits + punctuation

length = int(input("Enter password length: "))

password_generator = ''.join(random.sample(signs_combination, length))

print(f'Your password is: {password_generator}')


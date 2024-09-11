import random as rd
import string

def generate_password():
    capital_letters = tuple(string.ascii_uppercase)
    lower_case_letters = tuple(string.ascii_lowercase)
    numbers = tuple(string.digits)
    special_chars = tuple(string.punctuation)

    chosen_characters = [
        rd.sample(capital_letters, 4),
        rd.sample(lower_case_letters, 4),
        rd.sample(numbers, 4),
        rd.sample(special_chars, 4)
    ]

    character_list = sum(chosen_characters, [])
    rd.shuffle(character_list)

    return ''.join(character_list)


def save_to_file(text):
    file = open('../password.txt', 'w')
    file.write(text)
    file.close()


password = generate_password()
save_to_file(password)

import math


def greet(name, location):
    print(f"Hello, {name}.")
    print(f"What is it like in {location}.")
    print("Isn't the weather nice today?")


def number_of_cans():
    height = int(input("Height of wall :"))
    width = int(input("Width of wall :"))
    cover = int(input("Coverage :"))

    total_cans = math.ceil((height * width) / cover)
    print(f"You'll need {total_cans} cans of paint.")


def prime_chacker(number):
    ls = []
    for i in range(1, 100):
        if number % i == 0:
            ls.append(i)

    if [1, number] != ls:
        print("it's not a prime number.")
    else:
        print("it's a prime number")


def caesar_cipher():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']
    alphabet_upper = [a.upper() for a in alphabet]

    exited = 'yes'

    while exited == 'yes':
        direction = ""
        while direction not in ["ENCODE", "DECODE"]:
            direction = input("Type Encode to encrypt, type Decode to decrypt : ").upper()
        user_text = input("Type your message : ")
        shift = int(input("Type the shift number : "))
        end_text = ""
        new_list = alphabet_upper + alphabet

        if direction == "DECODE":
            shift = (shift % len(new_list)) * -1

        for char in user_text:
            if char in new_list:
                position = new_list.index(char)
                new_position = position + shift
                end_text += new_list[new_position if new_position < len(new_list) else new_position % len(new_list)]
            else:
                end_text += char

        print(f"Here's the {direction} result: {end_text}")
        exited = input("Type 'yes' if you want to go again. Otherwise type 'no' : ")
        if exited == 'no':
            print("Okie, Bye!")


if __name__ == '__main__':
    caesar_cipher()

    # prime_chacker(int(input("Check this number : ")))

    # number_of_cans()

    # greet(input("Text Your Name : "),
    #       input("Where are you from : "))


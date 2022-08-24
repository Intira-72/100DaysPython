import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def nato_alphabet():
    word = input("Enter a word: ").upper()
    try:    
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_alphabet()
    else:    
        print(output_list)


if __name__ == '__main__':
    nato_alphabet()
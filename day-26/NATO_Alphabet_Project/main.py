import pandas as pd

nato_alp_dict = {row.letter: row.code for index, row in pd.read_csv("nato_phonetic_alphabet.csv").iterrows()}
user_phonetic = [nato_alp_dict[word] for word in input("Enter a words: ").upper()]

print(user_phonetic)
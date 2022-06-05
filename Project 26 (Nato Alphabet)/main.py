import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
print(new_dict)

word = input("Enter a word: ").upper()

output = [new_dict[i] for i in word]
print(output)
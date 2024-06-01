# student_dict = {
#     "student": ["Sanskar", "James", "Lily"], 
#     "score": [96, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass


# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd

data = pd.read_csv(r"D:\sankhu codes and stuff\angela yu course\python\pandas\NATO-alphabet-start\NATO-alphabet-start\nato_phonetic_alphabet.csv")
print(data.to_dict)
print("heelo")

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}


phonetic = {row.letter: row.code for(index, row) in data.iterrows()}


word = input(" enter a word :").upper()

output = [phonetic[letter] for letter in word]


print(output)  

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.



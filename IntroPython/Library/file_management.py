# OS
import os

print(os.getcwd())  # get file directory

# JSON
import json

user = '{"name": "Ilham", "age": 21, "city": "Bekasi"}'
user_JSON = json.loads(user)
print(user_JSON['name'])

# Pickle, list transmission
import pickle

dictionary_example = {1: "6", 2: "2", 3: "f"}
pickle_output = open("dict.pickle", "wb")
pickle.dump(dictionary_example, pickle_output)
pickle_output.close()

pickle_input = open("dict.pickle", "rb")
dictionary_result = pickle.load(pickle_input)
pickle_input.close()

print(dictionary_result)

import json
from difflib import get_close_matches

# import difflib to use get_close_matches
# get_close_matches() is used to get closest possible item

# load the .json file
dict = json.load(open("data.json"))

# take desired word from user
word = input()

word = word.lower()


# covert the word into lower cases, because almost all keywords in .json file in small letter

# translation
def translate(word):
    if word in dict:
        return dict[word]

    # covert the word into tittle format
    # because some words in .json file are in tittle format
    elif word.title() in dict:
        return dict[word.title()]

    # covert the word into capital format
    # because some words in .json file are in capital format
    elif word.upper() in dict:
        return dict[word.upper()]

    # to find the closest possible words
    # get_close_matches("any word", a list or dictionary or tuple where the data is stored)
    elif len(get_close_matches(word, dict.keys())) > 0:
        # just checking the length of the possible matched words

        print("Did you mean %s instead?" % get_close_matches(word, dict.keys()))
        # %s is string literal in python

        # take word from user
        close_word = input("type the word: ")
        close_word = close_word.lower()

        if close_word in dict:
            return dict[close_word]

        elif close_word.title() in dict:
            return dict[close_word.title()]

        elif close_word.upper() in dict:
            return dict[close_word.upper()]

        else:
            return "the word doesn't match..."

    else:
        print("sorry, couldn't find it...")


output = translate(word)

# to print the results in column
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

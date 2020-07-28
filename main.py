import json
from difflib import get_close_matches

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (360, 480)

# load .json file
dict = json.load(open("data.json"))

class DictManager(GridLayout):

    # init method for keywords
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # declare an empty list for storing nearest matched words
        self.keys = []

        # declare an empty string for storing translated strings
        self.obj = ""

    def search_btn(self, word):

        # converting input text to lower
        word = word.lower()

        # method for translation
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

            # just checking the length of the possible matched words
            elif len(get_close_matches(word, dict.keys())) > 0:

                # storing the nearest matched keys in the list
                self.keys = get_close_matches(word, dict.keys())
                return self.keys

            else:
                self.d_out.text = "\n\nsorry, couldn't find the word..."

        # assign the translate() in a variable
        self.output = translate(word)

        # to print the results in column
        if type(self.output) == list:
            for self.item in self.output:
                 self.obj += ("\n=> %s" % self.item)

            # return the string in TextInput
            # checking if the keys[] is empty
            if self.keys == []:
                self.d_out.text = self.obj

            # if not then return the keys in TextInput and let users to choose which word they want to know
            else:
                self.d_out.text = ("\nnearest matched words:\n\n=> %s" % self.keys)

        # if output is not a list then
        else:
            self.obj = self.output
            self.d_out.text = ("\n=> %s" % self.obj)

class DictionaryApp(App):
    def build(self):
        return DictManager()

DictionaryApp().run()
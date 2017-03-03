mydrugs = {'lisinopril': 'high blood pressure',
           'metformin': 'high blood sugar',
           'mobic': 'inflammatory pain'}

print mydrugs['mobic']

# The following below accesses functions and variables in the mystuff.py script

import mystuff

mystuff.greet()
print mystuff.myName


# -------------------



class Person():
    def __init__(self):
        self.statement = "I AM A LIVING AND BREATHING PERSON!!! YEA!!!"
        self.age = []
        self.height = []


william = Person()
william.age = 30

print william.age
print william.height
print william.statement


# --------------------

class Song():

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "Happy birthday to you",
                   "and yaddy yaddy ya...."])

happy_bday.sing_me_a_song()

champions = ["We are the champions",
             "We are the champions!!!",
             "No time for losers...",
             "Because WE ARE THE CHAMPIONS",
             "OF THE WORLD!!!"]

champions_sung = Song(champions)
champions_sung.sing_me_a_song()
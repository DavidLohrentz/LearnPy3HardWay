#!/usr/bin/python3

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["\nHappy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there\n"])

bulls_on_parade = Song(["The rally around tha family",
                        "With pockets full of shells",
                        "Add a new line and seee if it is there\n"])

there_are_places = Song(["There are places I remember, all my life",
                         "Though some have changed",
                         "Some forever, not for better",
                         "Some have gone and some remain\n"

])

sunset = "Sunset is an angel weeping"
holding = "Holding out a bloody sword"
no = "No matter how I squint I cannot"
make = "Make out what it's pointing toward"
sometimes = "Sometimes you feel like you've lived too long"
days = "Days drip slowly on the page"
you = "You catch yourself"
pacing = "Pacing the cage\n"

pacing_the_cage = Song([sunset, holding, no, make, sometimes, days, you, pacing])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

there_are_places.sing_me_a_song()

pacing_the_cage.sing_me_a_song()
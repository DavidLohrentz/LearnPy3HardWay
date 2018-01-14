from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last scene_map
        current_scene.enter()


class Death(Scene):

    quips = [
        "WTF? You suck, and you are an asshole, and you are dead.",
        "He gone.",
        "Go directly to jail. Do not go to the start and do not collect $200.",
        "Moka can do this better than you can.",
        "You should try tiddlywinks instead. Buh, bye"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            Aliens have invaded your ship and blah, blah, blah. . . .
            about to pull a weapon to blast you.
            """))

        action = input("> ")

        if action == "shoot!" or "shit":
            print(dedent("""
                Quick on the draw, blah blah blah
                Then he eats you.
                """))

            return 'death'

        elif action == "dodge!":
            print(dedent("""

                Like a world class boxer . . .
                the Gothon stomps on your head and eats you.
                """))

            return death

        elif action == "tell a joke":
            print(dedent("""
                Lucky for you . . . blah blah blah blah
                blah blah blah blah blah blah blah blah
                blah jump through the Armory Door.
                """))

            return 'laser_weapon_armory'

        else:

            print("DOES NOT COMPUTE, YO!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
              You do a dive roll blah, blah blah.
              There is a keypad lock on the box and you need
              the code to remove the bomb. You get six guesses,
              then the lock closes forever and you cant get
              the bomb. The code is between 1 and 100.
              """))


        code = randint(1, 100)
        guess = int(input("[keypad]> "))
        guesses = 1

        while guess != code and guesses < 6:
          if guess > code:
              print("Too high.")
          elif guess < code:
              print("Too low.")
          else:
              pass
          guesses += 1
          guess = int(input("[keypad]> "))



        if guess == code:
          print(dedent("""
                The container clicks open and the seal breaks,
                letting gas out. You grab the neutron bomb and run
                as fast as you can to the bridge where you must place
                it in the right spot.
                """))
          return 'the_bridge'

        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a sickening
                melting sound as the mechanism is fused together. You decide
                to sit there until the Gothons blow up the ship and you die.
                """))
            return 'death'



class TheBridge(Scene):

    def Enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

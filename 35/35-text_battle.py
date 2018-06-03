import time

import random
from actors import Wizard, Dragon, SmallAnimal, Creature

def main():


    print_header()

    game_loop()



def print_header():
    print('---------------------------')
    print('       Battle Game')
    print('---------------------------')
    print()


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, scaliness=50, breaths_fire = True),
        Wizard('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandolf', 75)


    while True:

        active_creature = random.choice(creatures)
        print('-----------------------------------------------------------')
        print('A {} with level {} has appeared.'.format(active_creature.name, active_creature.level))
        print()

        selection = input('Do you [a]ttack, [r]un-away, or [l]ook around? ')

        if selection == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard now hides to recover.")
                time.sleep(5)
                print("The wizard returns now")
        elif selection == 'r':
            print("The wizard flees...")
            print()

        elif selection == 'l':
            print("The wizard looks around and notices;")
            for i, creature in enumerate(creatures):
                print('  ({}) {}'.format(i+1, creature))
            print()

        else:
            print('Exiting game...')
            break

        if not creatures:
            print("You defeated all the creatures.  Exiting the game!")
            break

if __name__ == '__main__':
    main()
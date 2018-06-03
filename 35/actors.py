import random

class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature {} of level {}".format(self.name, self.level)

    def attach(self):
        pass

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.breaths_fire = breaths_fire
        self.scale_thickness = scaliness

    def get_defensive_roll(self):
        roll = super().get_defensive_roll()
        fire_mod = 5 if self.breaths_fire else 1
        scale_mod = self.scale_thickness / 10

        return roll * fire_mod * scale_mod



class SmallAnimal(Creature):

    def get_defensive_roll(self):
        return super().get_defensive_roll() / 2


class Wizard(Creature):
    # def __init__(self, name, level):
    #     super().__init__(name, level)

    def attack(self, creature):
        print('The Wizard {} attacks {}!'.format(self.name, creature.name))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print('You roll {}...'.format(my_roll))
        print('{} rolls {}...'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('The wizard has triumped over {}.'.format(creature.name))
            print()
            return True
        else:
            print('{} has won over the wizard.'.format(creature.name))
            print()
            return False



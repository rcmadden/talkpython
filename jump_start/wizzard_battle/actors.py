import random


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature: {} of leverl {}".format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    # inherit from pareent class
    # def __init__(self, name, level):
    #     # self.name = name
    #     # self.level = level
    #     super().__init__(name, level)

    def attack(self, creature):
        print('The wizard {} attacks {}!'.format(
            self.name, creature.name
        ))

        # my_roll = random.randint(1, 12) * self.level
        my_roll = self.get_defensive_roll()
        # creature_roll = random.randint(1,12) * creature.level
        creature_roll = creature.get_defensive_roll()

        print("{} roll {}".format(self.name, my_roll))
        print("{} rolls {}".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("{} triumphs over {}".format(self.name, creature.name))
            return True
        else:
            print("The wizard has been DEFEATED!!!")
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        # base_roll = random.randint(1, 12) * self.level
        # inherits the action of superclass do not have to maintain * in 2 places
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()

        # fire_modifier = None
        # if self.breaths_fire:
        #     fire_modifier = 5
        # else:
        #     fire_modifier = 1

        # 1 line replaces 5 lines above
        # fire_modifier = VALUE_IF_TRUE if SOME_TEST else VALUE_IF FALSE
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10
        return base_roll * fire_modifier * scale_modifier

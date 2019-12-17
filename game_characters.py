import random


class Perso:
    """classe generique"""

    def __init__(self, name):
        """Initialise les bases des class"""
        self.current_life_point = self.max_life_point
        self.name = name
        self._height = random.randrange(170, 190)
        self._weight = random.randrange(70, 90)

    def __repr__(self):
        return "{} the {}. ".format(self.name, self.__class__.__name__)

    def _get_height(self):
        print(f"votre taille est {self._height} cm")
        return self._height

    def _get_weight(self):
        print(f"Votre poids est {self._weight} kg")
        return self._weight

    def _set_height(self, height):
        self._height = height

    def _set_weight(self, weight):
        self._weight = weight

    height = property(_get_height, _set_height)
    weight = property(_get_weight, _set_weight)

    def attack(self):
        """Définie l'attaque génerique"""
        magic_d = random.randrange(1, self.magic)
        bow_d = random.randrange(1, self.bow)
        sword_d = random.randrange(1, self.sword)
        if magic_d >= bow_d and magic_d >= sword_d:
            weapon = "magic"
            attack_point = magic_d
        elif bow_d >= magic_d and bow_d >= sword_d:
            weapon = "bow"
            attack_point = bow_d
        elif sword_d >= magic_d and sword_d >= bow_d:
            weapon = "sword"
            attack_point = sword_d
        return weapon, attack_point



    def defend(self, weapon, attack_point):
        """Définie la défence génerique"""
        if weapon == "magic":
            result = random.randrange(1, self.magic)
            if result < attack_point:
                self.current_life_point -= attack_point
        elif weapon == "bow":
            result = random.randrange(1, self.bow)
            if result < attack_point:
                self.current_life_point -= attack_point
        elif weapon == "sword":
            result = random.randrange(1, self.sword)
            if result < attack_point:
                self.current_life_point -= attack_point


class Wizard(Perso):
    max_life_point = 12
    magic = 12
    bow = 10
    sword = 8

    def attack(self):
        arm_2, attack_2 = super(Wizard, self).attack()
        attack_1 = random.randrange(1, self.magic)
        attack_point = max(attack_1, attack_2)
        if arm_2 == "sword":
            attack_2 += (self.weight + self.height)//40
        elif arm_2 == "bow":
            attack_2 += (self.height - 170) % 3
        if attack_point == attack_1:
            return "magic", attack_1
        else:
            return arm_2, attack_2


class Archer(Perso):
    max_life_point = 12
    magic = 10
    bow = 12
    sword = 8


    def attack(self):
        weapon, attack_point = super(Archer, self).attack()
        if weapon == "bow" or weapon == "magic":
            attack_point += 1
        if weapon == "sword":
            attack_point += self.height//40
        elif weapon == "magic":
            attack_point += self.weight//20
        return weapon, attack_point


class Warrior(Perso):
    max_life_point = 16
    magic = 8
    bow = 10
    sword = 12

    def attack(self):
        weapon, attack_points = super(Warrior, self).attack()
        if weapon == "magic":
            attack_points += self.weight//30
        elif weapon == "bow":
            attack_points += (self.height - 170) % 3
        return weapon, attack_points

class Dwarf:
    def bonus(self, weapon, attack_points):
        if weapon == "sword":
            attack_points += 2
        return weapon, attack_points

class Elf:
    def bonus(self, weapon, attack_points):
        if weapon == "bow":
            attack_points += 2
        return weapon, attack_points

class DwarfWizard(Wizard, Dwarf):
    pass

class ElfWizard(Wizard, Elf):
    pass

class DwarfArcher(Archer, Dwarf):
    pass

class ElfArcher(Archer, Elf):
    pass

class DwarfWarrior(Warrior, Dwarf):
    pass

class ElfWarrior(Warrior, Elf):
    pass


# legolas = ElfArcher("legolas")
# gimli = ElfWarrior("gimli")
# gandalf = ElfWizard("Gandalf")
#
# merlin = Wizard("Merlin")


#Attack 1 gandalf attack arthur:
# arm, points = gandalf.attack()
# print(gandalf, arm, points)
# legolas.defend(arm, points)
# print(legolas, legolas.current_life_point)

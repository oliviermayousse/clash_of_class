import unittest
import game_characters as game


class TestStringMethods(unittest.TestCase):

    def test_create_archer(self):

        self.JeanTarge = game.Archer("JeanTarge")
        print("{}: Max life : {} / magic: {} / bow: {} / sword: {}".format(self.JeanTarge,self.JeanTarge.max_life_point,
                                                                    self.JeanTarge.magic,self.JeanTarge.bow,
                                                                    self.JeanTarge.sword,))
        self.assertEqual(self.JeanTarge.name, 'JeanTarge')
        self.assertEqual(self.JeanTarge.max_life_point, 12)
        self.assertEqual(self.JeanTarge.magic, 10)
        self.assertEqual(self.JeanTarge.bow, 12)
        self.assertEqual(self.JeanTarge.sword, 8)

    def test_create_warrior(self):

        self.JeanFleuret = game.Warrior("JeanFleuret")
        print("{}: Max life : {} / magic: {} / bow: {} / sword: {}".format(self.JeanFleuret,self.JeanFleuret.max_life_point,
                                                                    self.JeanFleuret.magic,self.JeanFleuret.bow,
                                                                    self.JeanFleuret.sword,))
        self.assertEqual(self.JeanFleuret.name, 'JeanFleuret')
        self.assertEqual(self.JeanFleuret.max_life_point, 16)
        self.assertEqual(self.JeanFleuret.magic, 8)
        self.assertEqual(self.JeanFleuret.bow, 10)
        self.assertEqual(self.JeanFleuret.sword, 12)

    def test_create_wizard(self):

        self.Nabil = game.Wizard("Nabil")
        print("{}: Max life : {} / magic: {} / bow: {} / sword: {}".format(self.Nabil,self.Nabil.max_life_point,
                                                                    self.Nabil.magic,self.Nabil.bow,
                                                                    self.Nabil.sword,))
        self.assertEqual(self.Nabil.name, 'Nabil')
        self.assertEqual(self.Nabil.max_life_point, 12)
        self.assertEqual(self.Nabil.magic, 12)
        self.assertEqual(self.Nabil.bow, 10)
        self.assertEqual(self.Nabil.sword, 8)




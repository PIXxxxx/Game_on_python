import unittest
from game.cards.minions import Minion
from game.cards.spells import Spell


class TestMinion(unittest.TestCase):
    def test_minion_creation(self):
        minion = Minion(name="Дракон", attack=5, health=10)
        self.assertEqual(minion.name, "Дракон")
        self.assertEqual(minion.attack, 5)
        self.assertEqual(minion.health, 10)

class TestSpell(unittest.TestCase):
    def test_spell_creation(self):
        fireball = Spell(name = "Огненный шар", attack=3, cost=2)
        self.assertEqual(fireball.name, "Огненный шар")
        self.assertEqual(fireball.attack, 3)
        self.assertEqual(fireball.cost, 2)
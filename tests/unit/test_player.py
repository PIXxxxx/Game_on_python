import unittest
from game.players.base import Player
from game.cards.minions import Minion

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(name="TestPlayer")
        self.minion = Minion(name="Дракон", attack=5, health=10)

    def test_player_initialization(self):
        self.assertEqual(self.player.name, "TestPlayer")
        self.assertEqual(self.player.health, 30)
        self.assertEqual(self.player.mana, 0)
        self.assertEqual(self.player.hand, [])
        self.assertEqual(self.player.field, [])

    def test_draw_card(self):
        self.player.deck = [self.minion]
        self.player.draw_card()
        self.assertEqual(len(self.player.hand), 1)
        self.assertEqual(self.player.hand[0].name, "Дракон")

    def test_play_card(self):
        self.player.hand = [self.minion]
        played_card = self.player.play_card(0)
        self.assertEqual(played_card.name, "Дракон")
        self.assertEqual(len(self.player.hand), 0)
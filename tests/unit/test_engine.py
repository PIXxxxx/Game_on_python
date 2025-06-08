class TestGameEngine(unittest.TestCase):
    def setUp(self):
        self.player1 = Mock()
        self.player2 = Mock()
        self.engine = GameEngine(self.player1, self.player2)

    def test_initial_state(self):
        self.assertIsNone(self.engine.current_player)

    def test_start_game(self):
        self.engine.start_game()
        self.assertEqual(self.engine.current_player, self.player1)
        self.player1.draw_cards.assert_called_with(3)
        self.player2.draw_cards.assert_called_with(4)  # Второй игрок получает "монетку"
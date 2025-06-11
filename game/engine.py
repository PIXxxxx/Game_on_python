import random
from game.utils.logger import GameLogger


class GameEngine:
    def __init__(self, player1, player2, logger=None):
        self.player1 = player1  # Первый игрок
        self.player2 = player2  # Второй игрок
        self.current_player = None
        self.turn_number = 0
        self.logger = logger or GameLogger()
        self.history = []

    def start_game(self):
        """Инициализация новой игры"""
        self.current_player = self.player1
        self.turn_number = 1

        # Раздача начальных карт
        self.player1.draw_cards(3)
        self.player2.draw_cards(4)  # Второй игрок получает +1 карту

        self.logger.log_game_start()

    def switch_turn(self):
        """Передача хода другому игроку"""
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        self.turn_number += 1
        self.current_player.start_turn(self.turn_number)

        self.logger.log_turn_switch(self.current_player.name)

    def play_card(self, card_index, target=None):
        """Попытка сыграть карту"""
        player = self.current_player
        card = player.hand[card_index]

        # Проверка условий
        if card.cost > player.mana:
            raise ValueError("Недостаточно маны!")

        # Применение эффекта карты
        card.play(player, target)
        player.hand.pop(card_index)

        # Запись в историю
        self.history.append({
            'turn': self.turn_number,
            'player': player.name,
            'action': f'Play {card.name}'
        })

    def is_game_over(self):
        """Проверка условий конца игры"""
        return (
                self.player1.health <= 0
                or self.player2.health <= 0
                or self.turn_number > 50  # Макс. число ходов
        )

    def get_winner(self):
        """Определение победителя"""
        if self.player1.health > self.player2.health:
            return self.player1
        elif self.player2.health > self.player1.health:
            return self.player2
        else:
            return None  # Ничья

    def play_bot_turn(self):
        """Автоматический ход бота"""
        if not isinstance(self.current_player, BotPlayer):
            return

        # Простейший ИИ: выбирает случайную карту, которую может сыграть
        playable_cards = [
            card for card in self.current_player.hand
            if card.cost <= self.current_player.mana
        ]

        if playable_cards:
            card = random.choice(playable_cards)
            self.play_card(self.current_player.hand.index(card))

        self.switch_turn()
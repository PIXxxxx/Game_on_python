import random
from game import GameEngine, HumanPlayer, BotPlayer
from game.cards import Minion, Spell
from game.utils.config import ConfigManager
from game.utils.logger import GameLogger

def create_sample_cards():
    """Создаем тестовые карты для демонстрации"""
    return [
        Minion("Волк", cost=2, attack=3, health=2),
        Minion("Медведь", cost=4, attack=5, health=4),
        Spell("Огненный шар", cost=4, effect=lambda target: target.take_damage(6)),
        Minion("Дракон", cost=8, attack=8, health=8)
    ]


def main():
    # Инициализация системы
    logger = GameLogger("game.log")
    config = ConfigManager("settings.cfg")

    # Создаем игроков
    player1 = HumanPlayer("Игрок 1")
    player2 = BotPlayer("Компьютер")

    # Даем игрокам карты
    all_cards = create_sample_cards()
    player1.deck = random.sample(all_cards, 3)
    player2.deck = random.sample(all_cards, 3)

    # Создаем игровой движок
    engine = GameEngine(player1, player2, logger=logger)

    print("=== Добро пожаловать в карточную игру! ===")
    print(f"Игрок 1: {player1.name}")
    print(f"Игрок 2: {player2.name}")
    print("=========================================")

    # Запуск игры
    engine.start_game()

    # Главный игровой цикл
    while not engine.is_game_over():
        print("\n" + "=" * 40)
        print(f"Ход {engine.turn_number}: {engine.current_player.name}")
        print(f"Мана: {engine.current_player.mana}/{engine.turn_number}")

        # Показываем карты в руке
        print("\nВаши карты:")
        for i, card in enumerate(engine.current_player.hand, 1):
            print(f"{i}. {card.name} (Стоимость: {card.cost})")

        # Ход игрока или бота
        if isinstance(engine.current_player, HumanPlayer):
            choice = input("Выберите карту для игры (1-3) или 'end' для завершения хода: ")
            if choice.lower() == 'end':
                engine.end_turn()
                continue

            try:
                card_index = int(choice) - 1
                engine.play_card(card_index)
            except (ValueError, IndexError):
                print("Неверный ввод! Попробуйте снова.")
        else:
            # Ход бота
            print("\nБот делает ход...")
            engine.play_bot_turn()

        # Проверка условий победы
        if engine.check_win_conditions():
            break

    # Конец игры
    winner = engine.get_winner()
    print("\n" + "=" * 40)
    print(f"Игра окончена! Победитель: {winner.name}")
    logger.log_game_end(winner)


if __name__ == "__main__":
    main()
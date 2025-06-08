class Player:
    def __init__(self, name: str, health: int = 30):
        self.name = name
        self.health = health
        self.mana = 0
        self.hand = []
        self.deck = []
        self.field = []

    def draw_card(self) -> bool:
        """Добавляет карту из колоды в руку."""
        if self.deck:
            self.hand.append(self.deck.pop())
            return True
        return False

    def play_card(self, index: int):
        """Играет карту из руки по индексу."""
        if 0 <= index < len(self.hand):
            return self.hand.pop(index)
        return None

    def take_damage(self, amount: int):
        """Наносит урон игроку."""
        self.health -= amount
        return self.health > 0
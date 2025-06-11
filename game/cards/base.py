class Card:
    def __init__(self, name, cost, attack, health, effect=None):
        self.name = name
        self.cost = cost
        self.attack = attack
        self.health = health
        self.effect = effect

    def play(self, player, opponent=None, target=None):
        player.use_mana(self.cost)
        if self.effect and target:
            self.effect.apply(target)

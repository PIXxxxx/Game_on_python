import datetime
from typing import Optional


class GameLogger:
    def __init__(self, log_file: str = "game.log"):
        self.log_file = log_file
        self._init_log_file()

    def _init_log_file(self):
        """Создает файл лога с заголовком"""
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"\n{'=' * 50}\n")
            f.write(f"NEW GAME SESSION {datetime.datetime.now()}\n")
            f.write(f"{'=' * 50}\n\n")

    def _write_log(self, level: str, message: str):
        """Базовая функция записи"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level.upper()}] {message}\n"

        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)

    # Основные методы логирования
    def log_game_start(self):
        self._write_log("info", "Game initialized")

    def log_turn_switch(self, player_name: str):
        self._write_log("info", f"Turn switched to {player_name}")

    def log_card_play(self, player_name: str, card_name: str):
        self._write_log("info", f"{player_name} plays card: {card_name}")

    def log_error(self, error_type: str, details: str):
        self._write_log("error", f"{error_type}: {details}")

    def log_game_end(self, winner: Optional[str]):
        if winner:
            self._write_log("info", f"Game over. Winner: {winner}")
        else:
            self._write_log("info", "Game over. Draw")

    def log_custom_event(self, event_type: str, data: dict):
        """Для нестандартных событий (сетевые ошибки и т.д.)"""
        self._write_log("event", f"{event_type}: {str(data)}")
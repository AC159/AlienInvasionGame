class GameStats:
    # Track statistics for the alien invasion

    def __init__(self, ai_settings):
        # Initialize statistics
        self.ai_settings = ai_settings
        self.reset_stats()

        # High score should never be reset
        self.high_score = 0

        # Start the game in an active state
        self.game_active = False

    def reset_stats(self):
        # Initialize statistics that can change during the game
        self.ships_left = self.ai_settings.ships_limit
        self.score = 0
        self.level = 1




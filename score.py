import pygame

class Score():
    player_score = 0

    def get_score(self):
        return self.player_score

    def increase_score(self):
        self.player_score += 1
    
    def __str__(self):
        return f"{self.player_score}"
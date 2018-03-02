import enemies.enemy
import enemies.curvingenemy
import enemies.zigzagenemy
import random

class EnemiesManager():
    def __init__(self, game):
        self.game = game
        self.chances = "e" * 40 + "c" * 30 + "z" * 30

    def spawnEnemy(self):
        n = random.randint(0, len(self.chances) - 1)
        if self.chances[n] == "e":
            e = enemies.enemy.Enemy(self.game)
        if self.chances[n] == "c":
            e = enemies.curvingenemy.CurvingEnemy(self.game)
        if self.chances[n] == "z":
            e = enemies.zigzagenemy.ZigZagEnemy(self.game)
        return e

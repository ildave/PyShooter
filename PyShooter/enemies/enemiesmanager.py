import enemies.enemy
import enemies.curvingenemy
import random

class EnemiesManager():
    def __init__(self, game):
        self.game = game
        self.chances = "e" * 70 + "c" * 30

    def spawnEnemy(self):
        n = random.randint(0, 99)
        if self.chances[n] == "e":
            e = enemies.enemy.Enemy(self.game)
        if self.chances[n] == "c":
            e = enemies.curvingenemy.CurvingEnemy(self.game)
        return e

import enemies.enemiesmanager


class Wave:
    """Represents a wave of enemies.

    A wave knows how many enemies it should contain and can spawn
    them into a given sprite group using the shared EnemiesManager.
    """

    def __init__(self, game, enemies_manager, size):
        self.game = game
        self.enemies_manager = enemies_manager
        self.size = size

    def spawn(self, enemies_group):
        """Spawn all enemies for this wave into the provided group."""
        for _ in range(self.size):
            enemy = self.enemies_manager.spawnEnemy()
            enemies_group.add(enemy)






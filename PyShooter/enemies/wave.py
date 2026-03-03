import enemies.enemiesmanager


class Wave:
    """Represents a wave of enemies.

    A wave knows how many enemies it should contain and can
    sequentially spawn them into a given sprite group using the
    shared EnemiesManager.
    """

    def __init__(self, game, enemies_manager, size):
        self.game = game
        self.enemies_manager = enemies_manager
        self.size = size
        self.spawned = 0

    @property
    def done_spawning(self):
        return self.spawned >= self.size

    def spawn_next(self, enemies_group):
        """Spawn the next enemy in this wave, if any remain."""
        if self.done_spawning:
            return
        enemy = self.enemies_manager.spawnEnemy()
        enemies_group.add(enemy)
        self.spawned += 1






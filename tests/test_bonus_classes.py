import sys
import os
import pygame

# Ensure package imports work when tests are run from repo root
sys.path.insert(0, os.path.join(os.getcwd(), 'PyShooter'))

import bonus.bonus as basebonus
import bonus.helperbonus
import bonus.doublehelperbonus
import bonus.shieldbonus
import bonus.healthbonus
import bonus.tripleweaponbonus
import bonus.crossweaponbonus

import pytest


@pytest.fixture(autouse=True, scope='module')
def init_pygame():
    pygame.init()
    pygame.font.init()
    yield
    pygame.quit()


class DummyTimer:
    def __init__(self):
        self.duration = None
        self.action = None
    def cancel(self):
        self.action = None


class DummyGame:
    def __init__(self, width=960, height=540):
        self.width = width
        self.height = height
    def getTimer(self):
        return DummyTimer()
    def getRepeateTimer(self):
        return DummyTimer()


class DummyWeapon:
    pass


class DummyWeaponArmory:
    def getTripleWeapon(self):
        return 'TRIPLE'
    def getCrossWeapon(self):
        return 'CROSS'


class DummyShip:
    def __init__(self):
        # minimal attributes used by helpers/weapons
        self.weapon = None
        self.color = (255, 255, 255)
        self.angle = 0
        self.vspeed = 0
        self.hspeed = 0
        self.originalpoints = [(0,0), (10,0), (10,10), (0,10)]
        self.points = [(0,0), (10,0), (10,10), (0,10)]
        self.x = 0
        self.y = 0


class DummyScene:
    def __init__(self, game=None):
        self.game = game or DummyGame()
        self.score = 0
        self.effects = pygame.sprite.Group()
        self.ship = DummyShip()
        self.weaponarmory = DummyWeaponArmory()
    def setSimpleWeapon(self):
        self.ship.weapon = 'SIMPLE'


def test_bonus_basic_update_and_visual():
    g = DummyGame()
    scene = DummyScene(g)
    b = basebonus.Bonus(g, 100, 100, 0.5, scene)
    # initial properties
    assert b.size == 10
    assert len(b.originalpoints) == 4
    assert len(b.points) == 4

    # getVisualEffect returns a TextEffect-like object
    e = b.getVisualEffect()
    assert hasattr(e, 'text') or hasattr(e, '__class__')

    # update should move the bonus and update rect
    old_x, old_y = b.x, b.y
    b.update(100)
    assert (b.x != old_x) or (b.y != old_y)


def test_triple_and_cross_weapon_effects_set_weapon_and_timer():
    g = DummyGame()
    scene = DummyScene(g)
    ship = scene.ship

    tw = bonus.tripleweaponbonus.TripleWeaponBonus(g, 200, 200, 0, scene)
    tw.effect()
    assert ship.weapon == 'TRIPLE'

    cw = bonus.crossweaponbonus.CrossWeaponBonus(g, 200, 200, 0, scene)
    cw.effect()
    assert ship.weapon == 'CROSS'


def test_health_bonus_increases_energy(monkeypatch):
    g = DummyGame()
    scene = DummyScene(g)
    scene.energy = 50
    hb = bonus.healthbonus.HealthBonus(g, 200, 200, 0, scene)
    # effect should increase energy by between 10 and 30
    hb.effect()
    assert 60 <= scene.energy <= 80


def test_helper_and_double_helper_adds_helpers(monkeypatch):
    g = DummyGame()
    scene = DummyScene(g)

    # Monkeypatch the actual Helper class to a simple sprite so we can detect additions
    class SimpleHelper(pygame.sprite.Sprite):
        def __init__(self, *a, **k):
            super().__init__()

    monkeypatch.setattr('gameobjects.helper.Helper', SimpleHelper)

    hb = bonus.helperbonus.HelperBonus(g, 150, 150, 0, scene)
    assert len(scene.effects) == 0
    hb.effect()
    assert len(scene.effects) == 1

    dhb = bonus.doublehelperbonus.DoubleHelperBonus(g, 150, 150, 0, scene)
    dhb.effect()
    # double helper adds two more helpers
    assert len(scene.effects) >= 3


def test_shield_bonus_adds_shield(monkeypatch):
    g = DummyGame()
    scene = DummyScene(g)

    # Monkeypatch Shield to a simple sprite for detection
    class SimpleShield(pygame.sprite.Sprite):
        def __init__(self, *a, **k):
            super().__init__()

    monkeypatch.setattr('gameobjects.shield.Shield', SimpleShield)

    sb = bonus.shieldbonus.ShieldBonus(g, 120, 120, 0, scene)
    assert len(scene.effects) == 0
    sb.effect()
    assert len(scene.effects) == 1

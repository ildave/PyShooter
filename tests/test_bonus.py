import sys
import os

# Ensure package imports work when tests are run from repo root
sys.path.insert(0, os.path.join(os.getcwd(), 'PyShooter'))

from bonus.bonusmanager import BonusManager


class G:
    width = 960
    height = 540


def test_get_random_bonus_not_none():
    """getRandomBonus() should never return None for many samples."""
    bm = BonusManager(G(), None)
    for _ in range(50):
        b = bm.getRandomBonus()
        assert b is not None

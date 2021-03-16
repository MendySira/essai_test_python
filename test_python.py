#import tp_casino.py
from tp_casino import Joueur

j1 = Joueur("The Mike", 2000)

def test_create_user():
    assert j1 != None, "le joueur n'a pas été crée"

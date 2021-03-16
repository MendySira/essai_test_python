from tp_casino import Joueur
from tp_casino import Casino
from tp_casino import getArgentMise
from tp_casino import getNumeroMise

j1 = Joueur("The Mike", 2000)
c1 = Casino("Casa Blanca", j1)

def test_create_user():
    assert j1 != None, "le joueur n'a pas été crée"
    

def test_argent_positif():
    assert j1.argent >= 0, "l'argent de l'utilisateur est  négatif "

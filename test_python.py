#Les test en python se fait à l aide de assert et ca met assertion error aux cas ou la condition n est pas respecter
def somme(a,b):
    x = a + b
    return x;
def test_somme():
    a = 2
    b = 4
    x = somme(a,b)
    assert x >= 0

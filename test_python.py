#Les test en python se fait à l aide de assert et ca met assertion error aux cas ou la condition n est pas respecter
def positif(a,b):
    x = a + b
    assert x >= 0
def negatif(a,b):
    x = a + b
    assert x < 0

positif(2,4)
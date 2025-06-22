"""
# Operateurs sur les chaines de characteres

Certains operateurs permettent de verifier la composition d'une chaine 
de characteres. 

L'objectif est, pour chaque `assert`, d'appeler une methode sur `a` afin 
de verifier la condition en commentaire (toute les conditions en commentaires
sont vraies). 

[Doc: liste des methodes de strings](https://docs.python.org/3/library/stdtypes.html#string-methods)
"""

# Do not touch!
a = "Hello"

# TODO
assert not a       # a starts with 'Hel'
assert not a       # a doesn't end with 'thon'
assert not a       # a contains 'll'
assert not a       # a is composed of letters
assert not a       # a is not numerical

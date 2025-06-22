"""
# Opérateurs sur les chaines de charactères

Certains opérateurs permettent de verifier la composition d'une chaine 
de charactères. 

L'objectif est, pour chaque `assert`, d'appeler une méthode sur `a` afin 
de verifier la condition en commentaire (toute les conditions en commentaires
sont vraies). 

[Doc: liste des méthodes de strings](https://docs.python.org/3/library/stdtypes.html#string-methods)
"""

# Do not touch!
a = "Hello"

# TODO
assert not a       # a starts with 'Hel'
assert not a       # a doesn't end with 'thon'
assert not a       # a contains 'll'
assert not a       # a is composed of letters
assert not a       # a is not numerical

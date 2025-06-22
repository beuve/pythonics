"""
# Probleme de logique

Cet exercice est simplement un probleme de logique dans lequel une seule valeur est
possible pour `a`, `b` et `c` de façon a ce qu'aucun assert ne renvoi d'erreur.

Il existe 8 combinaison possibles pour `a`, `b` et `c`, ainsi un brut force est possible 
pour cet exercice. Neenmoins vous êtes encourage a reflechir et ne pas tester toutes les 
combinaisons possibles.

Modifiez les valeurs de `a`, `b` et `c` jusqu'a ne plus avoir d'erreur.

[Doc: Operateurs booleens](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
"""

# TODO
a = ...
b = ...
c = ...

# Do not touch!
assert a or b
assert not (not a or c)
assert b and not c


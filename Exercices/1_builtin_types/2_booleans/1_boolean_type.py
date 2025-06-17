"""
# Expressions booléennes

Python intègre des type booléen, mais ceux-ci ne sont pas nécessaires pour les conditions
des `if` ainsi que les boucles `while`. 

Les booléen `True` et `False` sont de types `bool`, qui est lui même un sous-type de `int`. 
Les booléens étant des entiers, ils doivent en avoir le comportement et donc ils peuvent être
additionné. Dans ces cas, `True` vaut `1` et `False` vaut `0`.

Modifiez les valeurs de `a`, `b` et `c` jusqu'à ne plus avoir d'erreur.
Edit the values of a, b, and c such that each assert passes.

[Doc: opérateurs Booléen](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
"""

# TODO
a = ...
b = ...
c = ...

# Do not touch!
assert a and b and c

assert (a == True) == True
assert (b == True) == False

assert isinstance(a, int)
assert not isinstance(a, bool)

assert isinstance(b, int)
assert not isinstance(b, bool)

assert isinstance(c, int)
assert isinstance(c, bool)

"""
# Casting des variables

Modifiez les valeurs de `a`, `b` et `c` jusqu'a ne plus avoir d'erreur.
Les valeurs de `a`, `b` et `c` peuvent être deduites des resultats des operations.

`b` ne devrait pas être definie en utilisant un litteral (e.g., b = 2), mais en utilisant
une fonction pour caster la valeur de `a` dans le type demande. De façon similaire, `c`
doit être definie en utilisant une fonction pour caster la valeur de `a`.

[Python doc](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
"""

# TODO
a = ...
b = ...
c = ...

# Do not touch!
assert a == b
assert a == c.real == 2
assert b == c.imag
assert isinstance(a, int)
assert isinstance(b, float)
assert isinstance(c, complex)

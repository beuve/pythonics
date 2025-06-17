"""
# Opérations sur les complexes

Les opérateurs vu dans l'exercice précédent sont aussi disponibles pour les complexes.
Les valeurs de `a` et `b` peuvent être déduites des résultats des opérations. 

Modifiez les valeurs de `a` et `b`, ainsi que les opérateurs `@` (en respectant les commentaires) jusqu'à ne plus avoir d'erreur.

[Doc: Opérateurs numériques](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
"""

# TODO
a = ...
b = ...

assert  a @ b ==  5 - 1j             # Addition
assert  a @ b == -1 + 7j             # Substraction
assert  a @ b == 18 + 1j             # Multiplication
assert  a @ b == -0.24 + 0.68j       # Division

# Do not touch!
assert  a.real == 2 and b.imag == -4

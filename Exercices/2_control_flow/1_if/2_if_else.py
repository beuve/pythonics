"""
# If / Else

Le commentaire `Values: [...]` donne l'ensemble des valeurs possibles de `b`. L'objectif
est de remplacer chaque `...` de façon a ce que chaque `assert` passe. Pour valider
l'exercice, essayez l'ensemble des valeurs de `b`.

[Syntax: If statement](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement)
[Doc: If statement](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
"""

# TODO
b = ... # Values: [True, False, None]
a = ...

# Do not touch!
assert (b and (a == 1)) or (b == None and a == 2) or (not b and (a == 3))

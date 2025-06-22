"""
# Operateur ternaire

Un operateur ternaire est un operateur `if`, ce qui signifie que contrairement a 
un `if` classique, celui-ci renvoie une valeur. Il est utils pour conditionellement 
initialiser une variable en une seule ligne sans avoir a d'abord creer la variable
et ensuite lui affecter sa valeur avec un `if` (comme dans l'exercice `if statement`
precedent).

L'objectif ici est de reproduire l'exercice `if statement` en utilisant un operateur
ternaire.

Le commentaire `Values: [...]` donne l'ensemble des valeurs possibles de `b`. L'objectif
est de remplacer chaque `...` de façon a ce que chaque `assert` passe. Pour valider
l'exercice, essayez l'ensemble des valeurs de `b`.

[Syntax: Conditional expression](https://docs.python.org/3/reference/expressions.html#conditional-expressions)
[Doc: If statement](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
[Wiki: Ternary operators](https://en.wikipedia.org/wiki/Ternary_operation#Computer_science)
"""

# TODO
b = ... # Values: [True, False]
a = ...

# Do not touch!
assert b and (a == 2) or not b and (a == 1)


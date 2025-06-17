"""
# Nombre d'arguments arbitraires

En Python, une fonction peut être définie pour accepter un nombre variable
d'arguments positionnels grâce à la syntaxe `*args`. Ce paramètre spécial
regroupe tous les arguments supplémentaires passés lors de l'appel dans un tuple.

Cela permet d'écrire des fonctions flexibles capables de traiter un nombre
d’arguments inconnu à l'avance, sans lever d’erreur, et sans devoir définir
plusieurs signatures.

Modifiez `f` jusqu'à ne plus avoir d'erreur.

[Syntax: Function definition](https://docs.python.org/3.10/reference/compound_stmts.html#function-definitions)
[Doc: arbitrary argument lists](https://docs.python.org/3.13/tutorial/controlflow.html#arbitrary-argument-lists)
"""

# TODO
def f():
  ...

# Do not touch!
assert f(1) == [1]
assert f(1,2,3) == [1, 2, 3]
assert f(1,2,3,4) == [1, 2, 3, 4]

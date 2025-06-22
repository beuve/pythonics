"""
# Nombre d'arguments arbitraires

En Python, une fonction peut être definie pour accepter un nombre variable
d'arguments positionnels grâce a la syntaxe `*args`. Ce parametre special
regroupe tous les arguments supplementaires passes lors de l'appel dans un tuple.

Cela permet d'ecrire des fonctions flexibles capables de traiter un nombre
d’arguments inconnu a l'avance, sans lever d’erreur, et sans devoir definir
plusieurs signatures.

Modifiez `f` jusqu'a ne plus avoir d'erreur.

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

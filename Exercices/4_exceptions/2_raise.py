"""
# `raise`

Il est possible de lever des exception manuellement dans les fonctionalités
que l'on implémente. Pour cela, le mot clés `raise` est utilisé.

L'objectif de cet exercice est de refaire l'exercice `for else` en utilisant
des exceptions.

La fonction find permet de trouver l'indice de la première occurence de
`value` dans `list`. Si cette valeur n'existe pas, find doit lever une
exception de type `IndexError`.

[Syntax: raise](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement)
[Doc: built-in exceptions](https://docs.python.org/3/library/exceptions.html)
[Doc: IndexError](https://docs.python.org/3/library/exceptions.html#IndexError)
"""

# TODO
def find(value, list):
  ...

# Do not touch!
try:
  a = find(2, [1, 2, 3])
except IndexError:
  a = -1
assert a == 1

try:
  a = find(2, [1, 3])
except IndexError:
  a = -1
assert a == -1

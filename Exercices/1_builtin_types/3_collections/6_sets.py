"""
# Sets

Un set est un collection d'éléments qui ne retiens pas l'ordre d'insertion,
mais pour lequel la recherche d'un élément est en O(1) (contrairement à
O(n) pour les lists non triées). 

Effectuez les actions spécifiés après chacun des TODO.

[Syntax: sets](https://docs.python.org/3/reference/expressions.html#set-displays)
[Doc: set](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
[Doc: Time complexity](https://wiki.python.org/moin/TimeComplexity)
"""

s = set()                      # Do not touch!
s                              # TODO: Add one element
assert s == {1}                # Do not touch!
s                              # TODO: Add multiple elements at once
assert len(s) == 3             # Do not touch!
s                              # TODO: Remove element
assert 2 not in s              # Do not touch!
s                              # TODO: Union with another set
assert s == {1, 3, 4, 5}       # Do not touch!
s                              # TODO: Empty the set
assert s == set()              # Do not touch!

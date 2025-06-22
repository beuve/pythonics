"""
# Lists

Une liste est une collection qui stock les élements de façon ordonnée. 
Dans python, il n'y a par défaut pas de file ou de pile, les `list` sont utilisé
comme tableau, pile ou file.

En python, les lists sont implémentées avec des tableaux dynamiques. L'avantage 
par rapport à des lists chainées sont: l'accessibilité et la modification des éléments
en O(1). Cependant, un inconvénient est l'insertion en O(1) *amorti* signifiant que dans
de rare cas l'insertion peut prendre plus de temps.

Effectuez les actions spécifiés après chacun des TODO.

[Syntax: lists](https://docs.python.org/3/reference/expressions.html#list-displays)
[Doc: lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
[Doc: Time complexity](https://wiki.python.org/moin/TimeComplexity)
"""

a = []                       # Do not touch!
a                            # TODO: Add a single element
assert a == [2]              # Do not touch!
a                            # TODO: Add an element at the begining of the list
assert a == [3, 2]           # Do not touch!
a                            # TODO: Remove the last element of a
assert a == [3]              # Do not touch!
a                            # TODO: Append the list [5, 4, 6] to the end of a
assert a == [3, 2, 5, 4, 6]  # Do not touch!
a                            # TODO: Revert the list
assert a == [6, 4, 5, 2, 3]  # Do not touch!
a                            # TODO: Sort a
assert a == [2, 3, 4, 5, 6]  # Do not touch!
a                            # TODO: Remove all elements of a
assert a == []               # Do not touch!


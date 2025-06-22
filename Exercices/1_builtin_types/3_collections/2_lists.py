"""
# Lists

Une liste est une collection qui stock les elements de façon ordonnee. 
Dans python, il n'y a par defaut pas de file ou de pile, les `list` sont utilise
comme tableau, pile ou file.

En python, les lists sont implementees avec des tableaux dynamiques. L'avantage 
par rapport a des lists chainees sont: l'accessibilite et la modification des elements
en O(1). Cependant, un inconvenient est l'insertion en O(1) *amorti* signifiant que dans
de rare cas l'insertion peut prendre plus de temps.

Effectuez les actions specifies apres chacun des TODO.

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


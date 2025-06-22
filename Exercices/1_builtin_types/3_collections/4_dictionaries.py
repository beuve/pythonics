"""
# Dictionnaires

Les dictionnaires sont des structures de donnees associant des cles a 
des valeurs. La recherche d'un element etant donne sa cle est en O(1).

Effectuez les actions specifies apres chacun des TODO.

[Syntax: dict](https://docs.python.org/3/reference/expressions.html#dictionary-displays)
[Doc: dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)  
[Doc: Time complexity](https://wiki.python.org/moin/TimeComplexity)
"""

d = {}                         # Do not touch!
d                              # TODO: Add key-value pair
assert d == {"name": "Alice"}  # Do not touch!
d                              # TODO: Add another key-value
assert d["age"] == 30          # Do not touch!
d                              # TODO: Remove "name" key
assert "name" not in d         # Do not touch!
d                              # TODO: Add using update
assert d == {"age": 30, "city": "Paris"}  # Do not touch!
d                              # TODO: Clear the dictionary
assert d == {}                 # Do not touch!

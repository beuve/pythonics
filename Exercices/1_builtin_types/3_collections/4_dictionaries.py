"""
# Dictionnaires

Les dictionnaires sont des structures de données associant des clés à 
des valeurs. La recherche d'un élément étant donné sa clé est en O(1).

Effectuez les actions spécifiés après chacun des TODO.

[Doc: Time complexity](https://wiki.python.org/moin/TimeComplexity)
[Doc: dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)  
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

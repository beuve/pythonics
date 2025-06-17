"""
# Slices

Un slice est une sous ensemble, pas nécessairement contiguë des éléments d'une liste. 
Les slices peuvent être utilisés avec les `list` et les `slices`. Dans python, les
slices sont des copies, et donc modifier la liste d'origine ne modifie pas les slices.

Effectuez les actions spécifiés après chacun des TODO.

[Doc: Opérations sur les séquences](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
"""

a = [3, 2, 5, 4, 6]   # Do not touch!
assert a == [2, 5]    # TODO: Create a slice of the second and third value of a
assert a == [3, 5, 6] # TODO: Create a slice of each evenly indexed elements
b = a                 # TODO: Copy a in b
assert a == b         # Do not touch!
assert a is not b     # Do not touch!

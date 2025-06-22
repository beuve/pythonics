"""
# Tuples

En python, les tuples sont des collections tres similaires au lists, 
la difference majeur est qu'ils sont imutables.

Effectuez les actions specifies apres chacun des TODO.

[Doc: Tuples](https://docs.python.org/3/library/stdtypes.html#tuples)
[Wiki: Variable shadowing](https://en.wikipedia.org/wiki/Variable_shadowing#:~:text=In%20computer%20programming%2C%20variable%20shadowing,is%20known%20as%20name%20masking.)
"""

a = ()                 # Do not touch!
a                      # TODO: Add a single element
assert a == (1,)       # Do not touch!
a                      # TODO: Add two more elements at the end
assert a == (1, 3, 2)  # Do not touch!
a                      # TODO: Sort the tuple
assert a == (1, 2, 3)  # Do not touch!
a                      # TODO: Reset tuple to empty
assert a == ()         # Do not touch!

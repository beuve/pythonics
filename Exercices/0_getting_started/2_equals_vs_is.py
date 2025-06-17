"""
# Différence entre `==` et `is`

- `==` vérifie si deux objets ont la même **valeur**.  
- `is` vérifie si deux objets sont **la même instance** en mémoire.

Complétez ou modifiez le code ci-dessous pour que tous les `assert` passent,
en tenant compte de cette différence.

[Syntax: comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)
"""

a = [1, 2, 3]
b = a
c = [1, 2, 3]


assert a @ c        # mêmes valeurs
assert a @ b        # même instance
assert not (a @ c)  # pas la même instance

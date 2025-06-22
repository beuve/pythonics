"""
# Comparaisons

Python fourni des operateurs de comparaisons de valeurs. 
Il en existe 4 types : 

- Les relations d'ordre (Superieur ou egal, inferieur ou egal)
- Les relations d'ordre stricts (Superieur, inferieur)
- Les relation d'egalite  (Egal, different)
- Les relation d'identite (Est le même, n'est pas le même)

Ces differentes comparaisons fonctionnent sur la pluspart des types primitifs de python
(pas tous : Les relations d'ordre ne fonctionnent pas sur les complexes). Pour les collections
comme les str ou les lists, l'_ordre lexicographique_ est utilise.

Les relations d'identite ont ete vu dans un exercice precedent, dans cette exercice 
les trois autres seront vu.

Modifiez les operateurs `@` (en respectant les commentaires) jusqu'a ne plus avoir d'erreur.

[Syntax: Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)
[Doc: Comparisons](https://docs.python.org/3/library/stdtypes.html#comparisons)
[Wiki: Ordre lexicographique](https://fr.wikipedia.org/wiki/Ordre_lexicographique)
"""

# Numbers 
assert 1 @ 1   # Equality
assert 1 @ 2   # Equality
assert 1 @ 2   # Strict order
assert 2 @ 1   # Strict order
assert 1 @ 1   # Order 
assert 2 @ 1   # Order 

# Strings
assert "hello" @ "hello"   # Equality
assert "Hello" @ "hello"   # Equality
assert "hello" @ "world"   # Strict order
assert "hello" @ "World"   # Strict order

# List
assert [1, 2] @ [1, 2]   # Equality
assert [1, 2] @ [2, 1]   # Equality
assert [1, 2] @ [1, 3]   # Order
assert ["hello", "World"] @ ["hello", "world"]   # Order

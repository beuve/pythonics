"""
# Matches

Il peut arriver de vouloir tester a la chaine non pas la valeur d'une expression,
mais son motif. Par exemple, pour une liste, il peut être necessaire d'effectuer 
des traitement differents si la liste comporte 0, 1 ou plus de 1 elements.

Ce type de control de flux s'appelle du _filtrage par motif_ (ou _pattern matching_ en anglais)
et est tres commun dans les languages de programmation fonctionnels. Leurs fonctionnalites
sont tres similaire aux switches de `C`, mais offres plus de possibilites (les switches en 
`C` ne comparant que la valeur et pas le motif).

Modifiez les valeurs de `a`, `b` et `c` jusqu'a ne plus avoir d'erreur.

[Syntax: Match statement](https://docs.python.org/3.10/reference/compound_stmts.html#the-match-statement)
[Doc: Match statement](https://docs.python.org/3/tutorial/controlflow.html#match-statements)
[Wiki: Filtrage par motif](https://fr.wikipedia.org/wiki/Filtrage_par_motif)
"""

# TODO
b = ... # Values: [[], ()]
a = ... # Values: [[], [2,3], [1,4], [2,4]]
c = ...

# Do not touch!
assert ((isinstance(b, list) and a == []) and (c == 1)) or (
  (isinstance(b, list) and a[1] == 4) and c == a[0]) or (
  (isinstance(b, list) and a[1] == 3) and c == 2 * a[0])

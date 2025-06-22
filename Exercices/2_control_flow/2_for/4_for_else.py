"""
# `for` - `else`

Contrairement à beaucoup d'autres languages, les boucles `for` (et `while`) en python 
peuvent comporter un `else`. 

Les instructions du `else` sont executées lorsque la condition de la boucle 
`for` n'est plus vérifiée. Ainsi, si un `break` vient couper la boucle, 
le `else` ne sera pas executé.

Trouver l'indice du premier 2 dans la liste `a`. Arrêtez la boucle quand 
celui-ci à été trouvé. Si la valeur n'éxiste pas, `b` doit valoir -1. 

Dans notre cas, initialiser `b` à -1 aurait le même effet que de changer sa valeur
avec un `else`. Le mieux serait de lever une exception indiquant que la valeur 
n'a pas été trouvée, ce qui demanderait plus d'efforts sans le `else`.

[Syntax: for](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)
[Doc: else in loops](https://docs.python.org/3/tutorial/controlflow.html#else-clauses-on-loops)
"""

# TODO
a = ... # Values: [1, 2, 3], [1, 3]
b = ...

# Do not touch!
assert (len(a) == 3 and b == 1) or (len(a) == 2 and b == -1)

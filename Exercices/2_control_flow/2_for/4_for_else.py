"""
# `for` - `else`

Contrairement a beaucoup d'autres languages, les boucles `for` (et `while`) en python 
peuvent comporter un `else`. 

Les instructions du `else` sont executees lorsque la condition de la boucle 
`for` n'est plus verifiee. Ainsi, si un `break` vient couper la boucle, 
le `else` ne sera pas execute.

Trouver l'indice du premier 2 dans la liste `a`. Arrêtez la boucle quand 
celui-ci a ete trouve. Si la valeur n'existe pas, `b` doit valoir -1. 

Dans notre cas, initialiser `b` a -1 aurait le même effet que de changer sa valeur
avec un `else`. Le mieux serait de lever une exception indiquant que la valeur 
n'a pas ete trouvee, ce qui demanderait plus d'efforts sans le `else`.

[Syntax: for](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)
[Doc: else in loops](https://docs.python.org/3/tutorial/controlflow.html#else-clauses-on-loops)
"""

# TODO
a = ... # Values: [1, 2, 3], [1, 3]
b = ...

# Do not touch!
assert (len(a) == 3 and b == 1) or (len(a) == 2 and b == -1)

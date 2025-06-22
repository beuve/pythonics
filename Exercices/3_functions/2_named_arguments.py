"""
# Arguments par defaut

Il est possible de definir des valeurs par defaut au arguments d'une fonction.
Il est egalement possible de nomer les atributs lors de l'appelle d'une fonction.
Cela permet de changer l'ordre des attributs, mais egalement de ne specifier que 
quelques valeurs, quelque soit l'ordre des attributs dans la definition de la fonction,
laissant les autres a leur valeur par defaut.

Modifiez `f` jusqu'a ne plus avoir d'erreur. Dans chaque assert, seulement une
des 3 valeurs change. Il est donc possible avec des valeurs par defaut judicieusement
choisis de ne specifier qu'une valeur par appele de fonction. 

[Syntax: function definition](https://docs.python.org/3.10/reference/compound_stmts.html#function-definitions)
[Doc: Default argument](https://docs.python.org/fr/3.13/tutorial/controlflow.html#default-argument-values)
[Doc: Named argument](https://docs.python.org/fr/3.13/tutorial/controlflow.html#keyword-arguments)
"""

# TODO
def f():
  ...

assert f()  == {"a":2, "b": 2, "c":3}
assert f() == {"a":1, "b": 0, "c":3}
assert f() == {"a":1, "b": 2, "c":1}

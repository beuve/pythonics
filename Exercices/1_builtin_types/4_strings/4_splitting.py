"""
# `Split` et `Join`
 
Python comporte des methodes simplifiant la séparation d'une chaine 
de charactère en sous chaines et inversement des sous chaines en une seul
chaine.

L'objectif est, pour chaque `assert`, d'appeler une méthode sur `text` ou
`items` afin d'obtenir le résultat attendu. 

[Doc: str.split](https://docs.python.org/3/library/stdtypes.html#str.split)  
[Doc: str.join](https://docs.python.org/3/library/stdtypes.html#str.join)
"""

# Do not touch!
text = "apple,banana,cherry"
items = ["red", "green", "blue"]

# TODO
assert text  == ["apple", "banana", "cherry"]
assert items == "red-green-blue"
assert text  == "apple-banana-cherry"

from connexion import recipes
import pprint

recipes.update_one({'title': 'chocolate milk'}, {'$set': {'author': 'George McFly'}})

print("\nShould be George McFly: ")
pprint.pprint(recipes.find_one({'author': 'George McFly'}))
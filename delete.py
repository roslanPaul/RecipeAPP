from connexion import recipes

myquery = { "author": "George McFly" }

recipes.delete_one(myquery)
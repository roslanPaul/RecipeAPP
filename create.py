from connexion import recipes


recipe = {'title': 'chocolate milk',
          'description': 'Yummy drink',
          'ingredients': [
              {'name': 'milk', 'quantity': 8, 'unit of measure': 'ounce'},
              {'name': 'chocolate syrup', 'quantity': 2, 'unit of measure': 'ounce'}
          ],
          'yield': {'quantity': 1, 'unit': 'glass'},
          'prep time': 0,
          'cook time': 0,
          'author': 'Biff Tannen',
          'uploaded_by': 'kenwalger',
          }

recipes.insert_one(recipe)
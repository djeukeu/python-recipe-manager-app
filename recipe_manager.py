import json

class RecipeManager():

    def __init__(self):
        self.recipes = self.load_recipes()

    # Load recipes from file
    def load_recipes(self):
        try:
            with open("recipes.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    # Save recipes to file
    def save_recipes(self) -> None:
        with open("recipes.json", "w") as file:
            json.dump(self.recipes, file)

    # Add a new recipe
    def add_recipe(self) -> None:
        name = input("Enter recipe name: ")
        ingredients = []
        print("Enter ingredients (leave blank to finish):")
        while True:
            ingredient = input(">> ")
            if not ingredient:
                break
            ingredients.append(ingredient)
        print("Enter instructions (leave blank to finish):")
        instructions = []
        while True:
            instruction = input(">> ")
            if not instruction:
                break
            instructions.append(instruction)
        self.recipes[name] = {"ingredients": ingredients, "instructions": instructions}
        self.save_recipes()
        print(f"Recipe '{name}' added successfully!")



# Delete a recipe
    def delete_recipe(self) -> None:
        name = input("Enter recipe title: ")
        if name not in self.recipes:
            print(f"Recipe '{name}' not found.")
            return
        del self.recipes[name]
        self.save_recipes()
        print(f"Recipe '{name}' deleted successfully!")
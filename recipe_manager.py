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

# View all recipes
    def view_recipes(self) -> None:
        if not self.recipes:
            print("No recipes found.")
            return
        print("Available recipes:")
        for name, recipe in self.recipes.items():
            print(f"- {name}")

    # Search for recipes
    def search_recipes(self) -> None:
        query = input("Enter search query: ")
        matches = [
            (name, recipe)
            for name, recipe in self.recipes.items()
            if query.lower() in name.lower()
            or any(query.lower() in ingredient.lower() for ingredient in recipe["ingredients"])
        ]
        if not matches:
            print(f"No recipes found for '{query}'.")
            return
        print(f"Recipes matching '{query}':")
        for name, recipe in matches:
            print(f"- {name}")

# Delete a recipe
    def delete_recipe(self) -> None:
        name = input("Enter recipe title: ")
        if name not in self.recipes:
            print(f"Recipe '{name}' not found.")
            return
        del self.recipes[name]
        self.save_recipes()
        print(f"Recipe '{name}' deleted successfully!")
from recipe_manager import RecipeManager

# Main program loop
def main() -> None:
    recipe_manager = RecipeManager()
    while True:
        print("\nRecipe Manager")
        print("1. Add recipe")
        print("2. View recipes")
        print("3. Search recipes")
        print("4. Edit recipe")
        print("5. Delete recipe")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            recipe_manager.add_recipe()
        if choice == "5":
            recipe_manager.delete_recipe()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
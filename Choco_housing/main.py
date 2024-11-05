import sqlite3

def add_seasonal_flavor(flavor_name, season):
    with sqlite3.connect("choco_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO SeasonalFlavors (flavor_name, season) VALUES (?, ?)", (flavor_name, season))
        connection.commit()

def Ingredient_inventory(ingredients_name, quantity):
    with sqlite3.connect("choco_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT OR REPLACE INTO Inventory (ingredients_name, quantity) VALUES (?, ?)", (ingredients_name, quantity))
        connection.commit()

def customer_suggestion(suggestion, allergy_information):
    with sqlite3.connect("choco_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO CustomerSuggestion (suggestion, allergy_information) VALUES (?, ?)", (suggestion, allergy_information))
        connection.commit()

if __name__ == "__main__":
    # Example usage:
    add_seasonal_flavor("Hot cocoa", "winter")
    add_seasonal_flavor("Mango Chili", "Summer")
    Ingredient_inventory("Cocoa", 120)
    Ingredient_inventory("Dried Mango Powder", 50)
    customer_suggestion("peanut-free options", "allergy to peanuts")

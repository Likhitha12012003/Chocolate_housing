import sqlite3

def create_tables():
    connection = sqlite3.connect("choco_house.db")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS SeasonalFlavors (
                        id INTEGER PRIMARY KEY,
                        flavor_name TEXT,
                        season TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Inventory (
                        id INTEGER PRIMARY KEY,
                        ingredients_name TEXT,
                        quantity INTEGER
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS CustomerSuggestion (
                        id INTEGER PRIMARY KEY,
                        suggestion TEXT,
                        allergy_information TEXT
                    )''')

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()

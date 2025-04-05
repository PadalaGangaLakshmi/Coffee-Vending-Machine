import psycopg2
from datetime import datetime

def connect_db():
    try:
        return psycopg2.connect(
            host="localhost",
            database="Pythondb", 
            user="postgres", 
            password="Neelu@4322"
        )
    except Exception as e:
        print("Error connecting to the database:", e)
        return None

def fetch_menu():
    conn = connect_db()
    if not conn:
        return {}
    
    cur = conn.cursor()
    cur.execute("SELECT Coffee_Type, Coffee_Price FROM Coffee_Price;")
    menu = {row[0].lower(): {"cost": float(row[1])} for row in cur.fetchall()}
    cur.close()
    conn.close()
    return menu

def fetch_resources():
    return {"water": 500, "milk": 300, "coffee": 100}

def store_transaction(coffee_type, amount_paid):
    conn = connect_db()
    if conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO Transactions (coffee_type, amount_paid, transaction_time) VALUES (%s, %s, %s)", 
                    (coffee_type, amount_paid, datetime.now()))
        conn.commit()
        cur.close()
        conn.close()

def fetch_transaction_history():
    conn = connect_db()
    if not conn:
        return []
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM Transactions ORDER BY transaction_time DESC LIMIT 10;")
    transactions = cur.fetchall()
    cur.close()
    conn.close()
    return transactions

class CoffeeMachine:
    RECIPE = {
        "espresso": {"water": 50, "milk": 0, "coffee": 18},
        "filtercoffee": {"water": 150, "milk": 50, "coffee": 24},
        "cappuccino": {"water": 200, "milk": 100, "coffee": 24},
    }

    def __init__(self, resources, money=0):
        self.resources = resources
        self.money = money

    def report(self):
        print("\n--- Available Resources ---")
        for item, amount in self.resources.items():
            print(f"{item.capitalize()}: {amount}")
        print(f"Money: {self.money:.2f}\n")

    def process_money(self, cost):
        try:
            total = sum(int(input(f"Enter {d} Rupee Notes: ")) * d for d in [1, 2, 5, 10, 20])
            print(f"Total inserted: {total} rupees")
            if total < cost:
                print("Not enough money. Money refunded.\n")
                return False
            print(f"Returning {total - cost} rupees.")
            self.money += cost
            return True
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return False

    def check_resources(self, drink_name):
        recipe = self.RECIPE.get(drink_name)
        if not recipe:
            print("Invalid selection.")
            return False

        for item, required in recipe.items():
            if self.resources[item] < required:
                print(f"Sorry, not enough {item}.\n")
                return False
        return True

    def make_coffee(self, drink_name, cost):
        if not self.check_resources(drink_name):
            return
        
        recipe = self.RECIPE[drink_name]
        for item, required in recipe.items():
            self.resources[item] -= required  

        print(f"\nHere is your {drink_name}. Enjoy!\n")
        store_transaction(drink_name, cost)

    def restock(self):
        self.resources = fetch_resources()
        print("Resources restocked successfully!\n")

def main():
    menu = fetch_menu()
    machine = CoffeeMachine(fetch_resources())

    while True:
        choice = input("What would you like? (espresso/filtercoffee/cappuccino/report/history/restock/off): ").lower().strip()
        if choice == "off":
            print("Turning off the machine.")
            break
        elif choice == "report":
            machine.report()
        elif choice == "history":
            transactions = fetch_transaction_history()
            print("\n--- Transaction History ---")
            print("\n".join(map(str, transactions)) if transactions else "No transactions found.")
        elif choice == "restock":
            machine.restock()
        elif choice in menu:
            if machine.check_resources(choice) and machine.process_money(menu[choice]["cost"]):
                machine.make_coffee(choice, menu[choice]["cost"])
        else:
            print("Invalid input. Please choose a valid option.\n")

if __name__ == "__main__":
    main()

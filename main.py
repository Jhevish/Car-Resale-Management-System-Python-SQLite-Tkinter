# import sqlite3

# connection = sqlite3.connect("carflip.db")

# cursor = connection.cursor()

# print("Database connected!")

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS cars (
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     make TEXT,
#     model TEXT,
#     year INTEGER,
#     mileage INTEGER,
#     purchase_price REAL,
#     status TEXT
# )
# """)

# connection.commit()

# print("Car Table created successfully!")

# cursor.execute("""
# INSERT INTO cars (make, model, year, mileage, purchase_price, status)
# VALUES ('BMW', '320d', 2018, 72000, 9500, 'In Stock')
# """)

# connection.commit()
# print("Car added!")
# cursor.execute("SELECT * FROM cars")
# cars = cursor.fetchall()
# print(cars)

# # # Delete all cars
# # cursor.execute("DELETE FROM cars")
# # # Reset AUTOINCREMENT back to 1
# # cursor.execute("DELETE FROM sqlite_sequence WHERE name='cars'")
# # connection.commit()
# # print("Cars deleted and ID reset!")


# # # Delete a specific car
# # cursor.execute("DELETE FROM cars WHERE car_id = 3")
# # connection.commit()


# TRIAL 2
# import sqlite3

# connection = sqlite3.connect("carflip.db")

# cursor = connection.cursor()

# print("Database connected!")

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS cars (
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     make TEXT,
#     model TEXT,
#     year INTEGER,
#     mileage INTEGER,
#     purchase_price REAL,
#     status TEXT
# )
# """)

# connection.commit()

# print("Car Table created successfully!")

# make = input("Enter car make: ")
# model = input("Enter car model: ")
# year = input("Enter car year: ")
# mileage = input("Enter car mileage: ")
# purchase_price = input("Enter purchase price: ")

# status = "In Stock"

# cursor.execute("""
# INSERT INTO cars (make, model, year, mileage, purchase_price, status)
# VALUES (?, ?, ?, ?, ?, ?)
# """, (make, model, year, mileage, purchase_price, status))

# connection.commit()

# print("Car added successfully!")

# cursor.execute("SELECT * FROM cars")

# cars = cursor.fetchall()

# print("\n================ CAR INVENTORY ================\n")

# for car in cars:
#     print(f"ID: {car[0]}")
#     print(f"Make: {car[1]}")
#     print(f"Model: {car[2]}")
#     print(f"Year: {car[3]}")
#     print(f"Mileage: {car[4]:,}")
#     print(f"Purchase Price: £{car[5]:,.2f}")
#     print(f"Status: {car[6]}")
#     print("-----------------------------------------------")


# ALL GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOD

# trial 3#

import sqlite3

connection = sqlite3.connect("carflip.db")

cursor = connection.cursor()

print("Database connected!")

cursor.execute("""
CREATE TABLE IF NOT EXISTS cars (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    make TEXT,
    model TEXT,
    year INTEGER,
    mileage INTEGER,
    purchase_price REAL,
    status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_id INTEGER,
    selling_price REAL,
    FOREIGN KEY (car_id) REFERENCES cars(car_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_id INTEGER,
    description TEXT,
    amount REAL,
    FOREIGN KEY (car_id) REFERENCES cars(car_id)
)
""")

# cursor.execute("""
# SELECT
#     cars.make,
#     cars.model,
#     SUM(expenses.amount)
# FROM cars
# JOIN expenses
# ON cars.car_id = expenses.car_id
# GROUP BY cars.car_id
# """)

# results = cursor.fetchall()

# print("\n================ TOTAL EXPENSES PER CAR ================\n")

# for row in results:
#     print(f"{row[0]} {row[1]}: £{row[2]:,.2f}")

connection.commit()

print("Car Table created successfully!")

while True:

    print()
    print("================ CARFLIP ================")
    print("1. Add a car")
    print("2. View inventory")
    print("3. Search by make")
    print("4. View cars in stock")
    print("5. Sell a car")
    print("6. View sales & profit")
    print("7. Add an expense")
    print("8. View expenses")
    print("9. View business stats")
    print("10. Edit a car")
    print("11. Delete a car")
    print("12. Exit")
    print("=========================================")

    choice = input("Choose an option: ")

    if choice == "1":
        make = input("Enter car make: ")
        model = input("Enter car model: ")

        try:
            year = int(input("Enter car year: "))
            mileage = int(input("Enter car mileage: "))
            purchase_price = float(input("Enter purchase price: "))

            status = "In Stock"

            cursor.execute("""
            INSERT INTO cars (make, model, year, mileage, purchase_price, status)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (make, model, year, mileage, purchase_price, status))

            connection.commit()

            print("Car added successfully!")

        except ValueError:
            print("Invalid input! Year, mileage and purchase price must be numbers.")

    elif choice == "2":
        cursor.execute("SELECT * FROM cars")

        cars = cursor.fetchall()

        print("\n================ CAR INVENTORY ================\n")

        for car in cars:
            print(f"ID: {car[0]}")
            print(f"Make: {car[1]}")
            print(f"Model: {car[2]}")
            print(f"Year: {car[3]}")
            print(f"Mileage: {car[4]:,}")
            print(f"Purchase Price: £{car[5]:,.2f}")
            print(f"Status: {car[6]}")
            print("-----------------------------------------------")

    elif choice == "3":
        search_make = input("Enter make to search: ")

        cursor.execute(
            "SELECT * FROM cars WHERE make = ?",
            (search_make,)
        )

        cars = cursor.fetchall()

        print("\n================ SEARCH RESULTS ================\n")

        for car in cars:
            print(f"ID: {car[0]}")
            print(f"Make: {car[1]}")
            print(f"Model: {car[2]}")
            print(f"Year: {car[3]}")
            print(f"Mileage: {car[4]:,}")
            print(f"Purchase Price: £{car[5]:,.2f}")
            print(f"Status: {car[6]}")
            print("-----------------------------------------------")

    elif choice == "4":
        cursor.execute("SELECT * FROM cars WHERE status = 'In Stock'")

        cars = cursor.fetchall()

        print("\n================ CARS IN STOCK ================\n")

        for car in cars:
            print(f"ID: {car[0]}")
            print(f"Make: {car[1]}")
            print(f"Model: {car[2]}")
            print(f"Year: {car[3]}")
            print(f"Mileage: {car[4]:,}")
            print(f"Purchase Price: £{car[5]:,.2f}")
            print(f"Status: {car[6]}")
            print("-----------------------------------------------")

    elif choice == "5":
        car_id = input("Enter the ID of the car to sell: ")

        cursor.execute(
            "SELECT * FROM cars WHERE car_id = ?",
            (car_id,)
        )

        car = cursor.fetchone()

        if car:
            if car[6] == "In Stock":
                print("Car is available to sell!")

                selling_price = input("Enter selling price: ")

                cursor.execute("""
                INSERT INTO sales (car_id, selling_price)
                VALUES (?, ?)
                """, (car_id, selling_price))

                cursor.execute("""
                UPDATE cars
                SET status = 'Sold'
                WHERE car_id = ?
                """, (car_id,))

                connection.commit()

                print("Sale recorded successfully!")

            else:
                print("This car has already been sold!")
        else:
            print("Car not found!")

    elif choice == "6":
        cursor.execute("""
        SELECT
            cars.make,
            cars.model,
            cars.purchase_price,
            sales.selling_price,
            COALESCE(SUM(expenses.amount), 0)
        FROM cars
        JOIN sales
        ON cars.car_id = sales.car_id
        LEFT JOIN expenses
        ON cars.car_id = expenses.car_id
        GROUP BY cars.car_id
        """)

        sales = cursor.fetchall()

        if not sales:
            print("\nNo sales recorded yet!")

        else:
            total_profit = 0

            print("\n================ SALES & PROFIT ================\n")

        for sale in sales:

            profit = sale[3] - sale[2] - sale[4]

            print(f"Make: {sale[0]}")
            print(f"Model: {sale[1]}")
            print(f"Purchase Price: £{sale[2]:,.2f}")
            print(f"Selling Price: £{sale[3]:,.2f}")
            print(f"Expenses: £{sale[4]:,.2f}")
            print(f"Profit: £{profit:,.2f}")
            print("-----------------------------------------------")

            total_profit = total_profit + profit

        print(f"\nTotal Profit: £{total_profit:,.2f}")

    elif choice == "7":
        car_id = input("Enter the car ID: ")

        cursor.execute(
            "SELECT * FROM cars WHERE car_id = ?",
            (car_id,)
        )

        car = cursor.fetchone()

        if car:
            description = input("Enter expense description: ")

            try:
                amount = float(input("Enter expense amount: "))

                cursor.execute("""
                INSERT INTO expenses (car_id, description, amount)
                VALUES (?, ?, ?)
                """, (car_id, description, amount))

                connection.commit()

                print("Expense added successfully!")

            except ValueError:
                print("Invalid amount! Please enter a number.")

    elif choice == "8":
        cursor.execute("""
        SELECT * FROM expenses
        """)

        expenses = cursor.fetchall()

        print("\n================ EXPENSES ================\n")

        for expense in expenses:
            print(f"Expense ID: {expense[0]}")
            print(f"Car ID: {expense[1]}")
            print(f"Description: {expense[2]}")
            print(f"Amount: £{expense[3]:,.2f}")
            print("-----------------------------------------------")

    elif choice == "9":

        # Total spent buying ALL cars
        cursor.execute("""
        SELECT SUM(purchase_price)
        FROM cars
        """)
        total_purchase = cursor.fetchone()[0]

        # Total money received from sales
        cursor.execute("""
        SELECT SUM(selling_price)
        FROM sales
        """)
        total_sales = cursor.fetchone()[0]

        # Total expenses across ALL cars
        cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
        """)
        total_expenses = cursor.fetchone()[0]

        # Purchase cost of SOLD cars only
        cursor.execute("""
        SELECT SUM(cars.purchase_price)
        FROM cars
        JOIN sales
        ON cars.car_id = sales.car_id
        """)
        sold_purchase_total = cursor.fetchone()[0]

        # Expenses belonging to SOLD cars only
        cursor.execute("""
        SELECT SUM(expenses.amount)
        FROM expenses
        JOIN sales
        ON expenses.car_id = sales.car_id
        """)
        sold_expenses = cursor.fetchone()[0]

        if sold_expenses is None:
            sold_expenses = 0

        # Calculate actual profit from sold cars
        overall_profit = total_sales - sold_purchase_total - sold_expenses

        cursor.execute("""
        SELECT SUM(purchase_price)
        FROM cars
        WHERE status = 'In Stock'
        """)

        stock_value = cursor.fetchone()[0]

        print("\n================ BUSINESS STATS ================\n")
        print(f"Total spent buying cars: £{total_purchase:,.2f}")
        print(f"Current stock value: £{stock_value:,.2f}")
        print(f"Total sales revenue: £{total_sales:,.2f}")
        print(f"Total expenses: £{total_expenses:,.2f}")
        print(f"Realised profit: £{overall_profit:,.2f}")

    elif choice == "10":

        car_id = input("Enter the ID of the car to edit: ")

        cursor.execute(
            "SELECT * FROM cars WHERE car_id = ?",
            (car_id,)
        )

        car = cursor.fetchone()

        if car:
            print(f"\nCar: {car[1]} {car[2]}")

            print("\nWhat do you want to edit?")
            print("1. Make")
            print("2. Model")
            print("3. Year")
            print("4. Mileage")
            print("5. Purchase price")

            edit_choice = input("Choose an option: ")

            if edit_choice == "1":

                new_make = input("Enter new make: ")

                cursor.execute("""
                UPDATE cars
                SET make = ?
                WHERE car_id = ?
                """, (new_make, car_id))

                connection.commit()

                print("Make updated successfully!")

            elif edit_choice == "2":

                new_model = input("Enter new model: ")

                cursor.execute("""
                UPDATE cars
                SET model = ?
                WHERE car_id = ?
                """, (new_model, car_id))

                connection.commit()

                print("Model updated successfully!")

            elif edit_choice == "3":

                try:
                    new_year = int(input("Enter new year: "))

                    cursor.execute("""
                    UPDATE cars
                    SET year = ?
                    WHERE car_id = ?
                    """, (new_year, car_id))

                    connection.commit()

                    print("Year updated successfully!")

                except ValueError:
                    print("Invalid year! Please enter a number.")

            elif edit_choice == "4":

                try:
                    new_mileage = int(input("Enter new mileage: "))

                    cursor.execute("""
                    UPDATE cars
                    SET mileage = ?
                    WHERE car_id = ?
                    """, (new_mileage, car_id))

                    connection.commit()

                    print("Mileage updated successfully!")

                except ValueError:
                    print("Invalid mileage! Please enter a number.")

            elif edit_choice == "5":

                try:
                    new_purchase_price = float(
                        input("Enter new purchase price: "))

                    cursor.execute("""
                    UPDATE cars
                    SET purchase_price = ?
                    WHERE car_id = ?
                    """, (new_purchase_price, car_id))

                    connection.commit()

                    print("Purchase price updated successfully!")

                except ValueError:
                    print("Invalid price! Please enter a number.")

            else:
                print("Invalid edit option!")

        else:
            print("Car not found!")

    elif choice == "11":

        car_id = input("Enter the ID of the car to delete: ")

        cursor.execute(
            "SELECT * FROM cars WHERE car_id = ?",
            (car_id,)
        )

        car = cursor.fetchone()

        if car:
            print(f"Car found: {car[1]} {car[2]}")

            cursor.execute(
                "SELECT * FROM sales WHERE car_id = ?",
                (car_id,)
            )

            sale = cursor.fetchone()

            cursor.execute(
                "SELECT * FROM expenses WHERE car_id = ?",
                (car_id,)
            )

            expense = cursor.fetchone()

            if sale or expense:
                print(
                    "This car cannot be deleted because it has sales or expense records.")

            else:
                confirm = input(
                    "Are you sure you want to delete this car? yes/no: ")

                if confirm.lower() == "yes":

                    cursor.execute("""
                    DELETE FROM cars
                    WHERE car_id = ?
                    """, (car_id,))

                    connection.commit()

                    print("Car deleted successfully!")

                else:
                    print("Delete cancelled.")

        else:
            print("Car not found!")

    elif choice == "12":
        print("Goodbye!")
        connection.close()
        break
    else:
        print("Invalid option! Please choose a number from 1 to 12.")

import tkinter as tk
from tkinter import messagebox
import sqlite3


# =========================================
# DATABASE CONNECTION
# =========================================

connection = sqlite3.connect("carflip.db")
cursor = connection.cursor()


# =========================================
# HELPER FUNCTION
# =========================================

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


def back_button():
    tk.Button(
        root,
        text="Back to Menu",
        width=20,
        command=main_menu
    ).pack(pady=15)


# =========================================
# MAIN MENU
# =========================================

def main_menu():
    clear_window()

    title = tk.Label(
        root,
        text="CARFLIP",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=20)

    buttons = [
        ("Add a Car", add_car_screen),
        ("View Inventory", view_inventory),
        ("Search by Make", search_car_screen),
        ("View Cars in Stock", view_stock),
        ("Sell a Car", sell_car_screen),
        ("View Sales & Profit", view_sales),
        ("Add Expense", add_expense_screen),
        ("View Expenses", view_expenses),
        ("Business Stats", business_stats),
        ("Edit a Car", edit_car_screen),
        ("Delete a Car", delete_car_screen)
    ]

    for text, command in buttons:

        button = tk.Button(
            root,
            text=text,
            width=25,
            height=2,
            command=command
        )

        button.pack(pady=4)

    tk.Button(
        root,
        text="Exit",
        width=25,
        height=2,
        command=close_program
    ).pack(pady=15)


# =========================================
# ADD CAR
# =========================================

def add_car_screen():
    clear_window()

    tk.Label(
        root,
        text="Add a Car",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(root, text="Make").pack()
    make_entry = tk.Entry(root)
    make_entry.pack(pady=5)

    tk.Label(root, text="Model").pack()
    model_entry = tk.Entry(root)
    model_entry.pack(pady=5)

    tk.Label(root, text="Year").pack()
    year_entry = tk.Entry(root)
    year_entry.pack(pady=5)

    tk.Label(root, text="Mileage").pack()
    mileage_entry = tk.Entry(root)
    mileage_entry.pack(pady=5)

    tk.Label(root, text="Purchase Price").pack()
    price_entry = tk.Entry(root)
    price_entry.pack(pady=5)

    def save_car():

        make = make_entry.get()
        model = model_entry.get()

        try:
            year = int(year_entry.get())
            mileage = int(mileage_entry.get())
            purchase_price = float(price_entry.get())

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Year, mileage and purchase price must be numbers."
            )
            return

        if make == "" or model == "":
            messagebox.showerror(
                "Missing Information",
                "Make and model cannot be empty."
            )
            return

        cursor.execute("""
        INSERT INTO cars (
            make,
            model,
            year,
            mileage,
            purchase_price,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            make,
            model,
            year,
            mileage,
            purchase_price,
            "In Stock"
        ))

        connection.commit()

        messagebox.showinfo(
            "Success",
            "Car added successfully!"
        )

        main_menu()

    tk.Button(
        root,
        text="Add Car",
        width=20,
        command=save_car
    ).pack(pady=15)

    back_button()


# =========================================
# VIEW INVENTORY
# =========================================

def view_inventory():
    clear_window()

    tk.Label(
        root,
        text="Car Inventory",
        font=("Arial", 20, "bold")
    ).pack(pady=15)

    cursor.execute("""
    SELECT *
    FROM cars
    """)

    cars = cursor.fetchall()

    if not cars:
        tk.Label(
            root,
            text="No cars found."
        ).pack()

    for car in cars:

        car_text = (
            f"ID: {car[0]}\n"
            f"{car[1]} {car[2]}\n"
            f"Year: {car[3]}\n"
            f"Mileage: {car[4]:,}\n"
            f"Purchase Price: £{car[5]:,.2f}\n"
            f"Status: {car[6]}"
        )

        tk.Label(
            root,
            text=car_text,
            justify="left",
            relief="groove",
            width=40,
            padx=10,
            pady=8
        ).pack(pady=5)

    back_button()


# =========================================
# SEARCH BY MAKE
# =========================================

def search_car_screen():
    clear_window()

    tk.Label(
        root,
        text="Search by Make",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    search_entry = tk.Entry(root)
    search_entry.pack(pady=10)

    def search():

        make = search_entry.get()

        cursor.execute("""
        SELECT *
        FROM cars
        WHERE make = ?
        """, (make,))

        cars = cursor.fetchall()

        clear_window()

        tk.Label(
            root,
            text=f"Search Results: {make}",
            font=("Arial", 18, "bold")
        ).pack(pady=15)

        if not cars:
            tk.Label(
                root,
                text="No cars found."
            ).pack()

        for car in cars:

            text = (
                f"ID: {car[0]}\n"
                f"{car[1]} {car[2]}\n"
                f"Year: {car[3]}\n"
                f"Mileage: {car[4]:,}\n"
                f"Price: £{car[5]:,.2f}\n"
                f"Status: {car[6]}"
            )

            tk.Label(
                root,
                text=text,
                justify="left",
                relief="groove",
                width=40,
                padx=10,
                pady=8
            ).pack(pady=5)

        back_button()

    tk.Button(
        root,
        text="Search",
        width=20,
        command=search
    ).pack(pady=10)

    back_button()


# =========================================
# VIEW STOCK
# =========================================

def view_stock():
    clear_window()

    tk.Label(
        root,
        text="Cars in Stock",
        font=("Arial", 20, "bold")
    ).pack(pady=15)

    cursor.execute("""
    SELECT *
    FROM cars
    WHERE status = 'In Stock'
    """)

    cars = cursor.fetchall()

    if not cars:
        tk.Label(
            root,
            text="No cars currently in stock."
        ).pack()

    for car in cars:

        text = (
            f"ID: {car[0]}\n"
            f"{car[1]} {car[2]}\n"
            f"Year: {car[3]}\n"
            f"Mileage: {car[4]:,}\n"
            f"Price: £{car[5]:,.2f}"
        )

        tk.Label(
            root,
            text=text,
            justify="left",
            relief="groove",
            width=40,
            padx=10,
            pady=8
        ).pack(pady=5)

    back_button()


# =========================================
# SELL CAR
# =========================================

def sell_car_screen():
    clear_window()

    tk.Label(
        root,
        text="Sell a Car",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(root, text="Car ID").pack()

    car_id_entry = tk.Entry(root)
    car_id_entry.pack(pady=5)

    tk.Label(root, text="Selling Price").pack()

    selling_price_entry = tk.Entry(root)
    selling_price_entry.pack(pady=5)

    def sell():

        car_id = car_id_entry.get()

        cursor.execute("""
        SELECT *
        FROM cars
        WHERE car_id = ?
        """, (car_id,))

        car = cursor.fetchone()

        if not car:
            messagebox.showerror(
                "Error",
                "Car not found."
            )
            return

        if car[6] != "In Stock":
            messagebox.showerror(
                "Error",
                "This car has already been sold."
            )
            return

        try:
            selling_price = float(
                selling_price_entry.get()
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Price",
                "Selling price must be a number."
            )
            return

        cursor.execute("""
        INSERT INTO sales (
            car_id,
            selling_price
        )
        VALUES (?, ?)
        """, (
            car_id,
            selling_price
        ))

        cursor.execute("""
        UPDATE cars
        SET status = 'Sold'
        WHERE car_id = ?
        """, (car_id,))

        connection.commit()

        messagebox.showinfo(
            "Success",
            "Sale recorded successfully!"
        )

        main_menu()

    tk.Button(
        root,
        text="Sell Car",
        width=20,
        command=sell
    ).pack(pady=15)

    back_button()


# =========================================
# VIEW SALES AND PROFIT
# =========================================

def view_sales():
    clear_window()

    tk.Label(
        root,
        text="Sales & Profit",
        font=("Arial", 20, "bold")
    ).pack(pady=15)

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

    total_profit = 0

    if not sales:
        tk.Label(
            root,
            text="No sales recorded."
        ).pack()

    for sale in sales:

        profit = (
            sale[3]
            - sale[2]
            - sale[4]
        )

        total_profit = (
            total_profit
            + profit
        )

        text = (
            f"{sale[0]} {sale[1]}\n"
            f"Purchase: £{sale[2]:,.2f}\n"
            f"Selling: £{sale[3]:,.2f}\n"
            f"Expenses: £{sale[4]:,.2f}\n"
            f"Profit: £{profit:,.2f}"
        )

        tk.Label(
            root,
            text=text,
            justify="left",
            relief="groove",
            width=40,
            padx=10,
            pady=8
        ).pack(pady=5)

    tk.Label(
        root,
        text=f"Total Profit: £{total_profit:,.2f}",
        font=("Arial", 14, "bold")
    ).pack(pady=15)

    back_button()


# =========================================
# ADD EXPENSE
# =========================================

def add_expense_screen():
    clear_window()

    tk.Label(
        root,
        text="Add Expense",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(root, text="Car ID").pack()

    car_id_entry = tk.Entry(root)
    car_id_entry.pack(pady=5)

    tk.Label(root, text="Description").pack()

    description_entry = tk.Entry(root)
    description_entry.pack(pady=5)

    tk.Label(root, text="Amount").pack()

    amount_entry = tk.Entry(root)
    amount_entry.pack(pady=5)

    def save_expense():

        car_id = car_id_entry.get()

        cursor.execute("""
        SELECT *
        FROM cars
        WHERE car_id = ?
        """, (car_id,))

        car = cursor.fetchone()

        if not car:
            messagebox.showerror(
                "Error",
                "Car not found."
            )
            return

        description = description_entry.get()

        try:
            amount = float(
                amount_entry.get()
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Amount",
                "Expense amount must be a number."
            )
            return

        cursor.execute("""
        INSERT INTO expenses (
            car_id,
            description,
            amount
        )
        VALUES (?, ?, ?)
        """, (
            car_id,
            description,
            amount
        ))

        connection.commit()

        messagebox.showinfo(
            "Success",
            "Expense added successfully!"
        )

        main_menu()

    tk.Button(
        root,
        text="Add Expense",
        width=20,
        command=save_expense
    ).pack(pady=15)

    back_button()


# =========================================
# VIEW EXPENSES
# =========================================

def view_expenses():
    clear_window()

    tk.Label(
        root,
        text="Expenses",
        font=("Arial", 20, "bold")
    ).pack(pady=15)

    cursor.execute("""
    SELECT *
    FROM expenses
    """)

    expenses = cursor.fetchall()

    if not expenses:
        tk.Label(
            root,
            text="No expenses recorded."
        ).pack()

    for expense in expenses:

        text = (
            f"Expense ID: {expense[0]}\n"
            f"Car ID: {expense[1]}\n"
            f"Description: {expense[2]}\n"
            f"Amount: £{expense[3]:,.2f}"
        )

        tk.Label(
            root,
            text=text,
            justify="left",
            relief="groove",
            width=40,
            padx=10,
            pady=8
        ).pack(pady=5)

    back_button()


# =========================================
# BUSINESS STATS
# =========================================

def business_stats():
    clear_window()

    tk.Label(
        root,
        text="Business Stats",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    cursor.execute("""
    SELECT SUM(purchase_price)
    FROM cars
    """)

    total_purchase = cursor.fetchone()[0] or 0

    cursor.execute("""
    SELECT SUM(purchase_price)
    FROM cars
    WHERE status = 'In Stock'
    """)

    stock_value = cursor.fetchone()[0] or 0

    cursor.execute("""
    SELECT SUM(selling_price)
    FROM sales
    """)

    total_sales = cursor.fetchone()[0] or 0

    cursor.execute("""
    SELECT SUM(amount)
    FROM expenses
    """)

    total_expenses = cursor.fetchone()[0] or 0

    cursor.execute("""
    SELECT SUM(cars.purchase_price)
    FROM cars
    JOIN sales
    ON cars.car_id = sales.car_id
    """)

    sold_purchase_total = cursor.fetchone()[0] or 0

    cursor.execute("""
    SELECT SUM(expenses.amount)
    FROM expenses
    JOIN sales
    ON expenses.car_id = sales.car_id
    """)

    sold_expenses = cursor.fetchone()[0] or 0

    realised_profit = (
        total_sales
        - sold_purchase_total
        - sold_expenses
    )

    stats_text = (
        f"Total spent buying cars:\n"
        f"£{total_purchase:,.2f}\n\n"

        f"Current stock value:\n"
        f"£{stock_value:,.2f}\n\n"

        f"Total sales revenue:\n"
        f"£{total_sales:,.2f}\n\n"

        f"Total expenses:\n"
        f"£{total_expenses:,.2f}\n\n"

        f"Realised profit:\n"
        f"£{realised_profit:,.2f}"
    )

    tk.Label(
        root,
        text=stats_text,
        font=("Arial", 13),
        justify="center"
    ).pack(pady=20)

    back_button()


# =========================================
# EDIT CAR
# =========================================

def edit_car_screen():
    clear_window()

    tk.Label(
        root,
        text="Edit a Car",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(root, text="Car ID").pack()

    car_id_entry = tk.Entry(root)
    car_id_entry.pack(pady=5)

    tk.Label(root, text="New Make").pack()
    make_entry = tk.Entry(root)
    make_entry.pack(pady=5)

    tk.Label(root, text="New Model").pack()
    model_entry = tk.Entry(root)
    model_entry.pack(pady=5)

    tk.Label(root, text="New Year").pack()
    year_entry = tk.Entry(root)
    year_entry.pack(pady=5)

    tk.Label(root, text="New Mileage").pack()
    mileage_entry = tk.Entry(root)
    mileage_entry.pack(pady=5)

    tk.Label(root, text="New Purchase Price").pack()
    price_entry = tk.Entry(root)
    price_entry.pack(pady=5)

    def update_car():

        car_id = car_id_entry.get()

        cursor.execute("""
        SELECT *
        FROM cars
        WHERE car_id = ?
        """, (car_id,))

        car = cursor.fetchone()

        if not car:
            messagebox.showerror(
                "Error",
                "Car not found."
            )
            return

        make = make_entry.get()
        model = model_entry.get()
        year = year_entry.get()
        mileage = mileage_entry.get()
        price = price_entry.get()

        if make != "":
            cursor.execute("""
            UPDATE cars
            SET make = ?
            WHERE car_id = ?
            """, (
                make,
                car_id
            ))

        if model != "":
            cursor.execute("""
            UPDATE cars
            SET model = ?
            WHERE car_id = ?
            """, (
                model,
                car_id
            ))

        if year != "":

            try:
                year = int(year)

            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Year must be a number."
                )
                return

            cursor.execute("""
            UPDATE cars
            SET year = ?
            WHERE car_id = ?
            """, (
                year,
                car_id
            ))

        if mileage != "":

            try:
                mileage = int(mileage)

            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Mileage must be a number."
                )
                return

            cursor.execute("""
            UPDATE cars
            SET mileage = ?
            WHERE car_id = ?
            """, (
                mileage,
                car_id
            ))

        if price != "":

            try:
                price = float(price)

            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Price must be a number."
                )
                return

            cursor.execute("""
            UPDATE cars
            SET purchase_price = ?
            WHERE car_id = ?
            """, (
                price,
                car_id
            ))

        connection.commit()

        messagebox.showinfo(
            "Success",
            "Car updated successfully!"
        )

        main_menu()

    tk.Button(
        root,
        text="Update Car",
        width=20,
        command=update_car
    ).pack(pady=15)

    tk.Label(
        root,
        text="Leave fields blank if you do not want to change them."
    ).pack()

    back_button()


# =========================================
# DELETE CAR
# =========================================

def delete_car_screen():
    clear_window()

    tk.Label(
        root,
        text="Delete a Car",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(root, text="Car ID").pack()

    car_id_entry = tk.Entry(root)
    car_id_entry.pack(pady=10)

    def delete_car():

        car_id = car_id_entry.get()

        cursor.execute("""
        SELECT *
        FROM cars
        WHERE car_id = ?
        """, (car_id,))

        car = cursor.fetchone()

        if not car:
            messagebox.showerror(
                "Error",
                "Car not found."
            )
            return

        cursor.execute("""
        SELECT *
        FROM sales
        WHERE car_id = ?
        """, (car_id,))

        sale = cursor.fetchone()

        cursor.execute("""
        SELECT *
        FROM expenses
        WHERE car_id = ?
        """, (car_id,))

        expense = cursor.fetchone()

        if sale or expense:
            messagebox.showerror(
                "Cannot Delete",
                "This car has sales or expense records."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Delete {car[1]} {car[2]}?"
        )

        if confirm:

            cursor.execute("""
            DELETE FROM cars
            WHERE car_id = ?
            """, (car_id,))

            connection.commit()

            messagebox.showinfo(
                "Success",
                "Car deleted successfully!"
            )

            main_menu()

    tk.Button(
        root,
        text="Delete Car",
        width=20,
        command=delete_car
    ).pack(pady=15)

    back_button()


# =========================================
# CLOSE PROGRAM
# =========================================

def close_program():
    connection.close()
    root.destroy()


# =========================================
# CREATE WINDOW
# =========================================

root = tk.Tk()

root.title("CarFlip")

root.geometry("600x750")

root.protocol(
    "WM_DELETE_WINDOW",
    close_program
)

main_menu()

root.mainloop()

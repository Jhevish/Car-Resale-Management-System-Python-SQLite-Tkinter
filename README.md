Car Resale Management System

A desktop car resale management application built with Python, SQLite and Tkinter. The system manages vehicle inventory, sales, expenses and profit calculations through a graphical user interface.

The project was built to practise database design, SQL operations and integrating a relational SQLite database with a Python application.

Features
Add vehicles to inventory
View and search vehicle records
Track vehicles as In Stock or Sold
Record vehicle sales
Record expenses associated with individual vehicles
Calculate profit for sold vehicles
View total expenses per vehicle
Display business statistics
Edit existing vehicle information
Manage data through a Tkinter graphical interface
Technologies
Python
SQLite
SQL
Tkinter
Git / GitHub
Database Structure

The application uses an SQLite relational database containing three main tables:

Cars

Stores vehicle information including:

Make
Model
Year
Mileage
Purchase price
Vehicle status
Sales

Stores completed vehicle sales and links each sale to a vehicle using car_id.

Expenses

Stores costs associated with individual vehicles, such as repairs, servicing or preparation costs.

The tables are connected using primary keys and foreign keys.

CARS
car_id (PK)
    │
    ├──────────────┐
    │              │
    ▼              ▼
SALES          EXPENSES
car_id (FK)    car_id (FK)
SQL Functionality

The application uses SQL operations including:

SELECT
INSERT
UPDATE
DELETE
WHERE
JOIN
GROUP BY
SUM()
ORDER BY

For example, vehicle and sales records can be joined through their shared car_id to calculate the profit made on a vehicle.

SELECT
    cars.make,
    cars.model,
    cars.purchase_price,
    sales.selling_price,
    sales.selling_price - cars.purchase_price AS profit
FROM sales
JOIN cars
ON sales.car_id = cars.car_id;
Project Structure
CarFlip/
│
├── main.py
├── ui.py
├── carflip.db
└── README.md

main.py contains the application's database operations and core functionality.

ui.py contains the Tkinter graphical user interface.

carflip.db is the SQLite database used to store vehicle, sales and expense records.

Running the Project

Make sure Python is installed, then clone the repository and run:

python ui.py

The application uses Python's built-in sqlite3 and tkinter modules, so no external database server is required.

What I Learned

This project helped me develop practical experience with:

Designing and working with relational databases
Connecting Python applications to SQLite
Writing SQL queries for data retrieval and manipulation
Using primary and foreign keys to create relationships between tables
Using SQL joins and aggregate functions for business calculations
Building a desktop GUI with Tkinter
Structuring a Python project across multiple files
Using Git and GitHub for version control

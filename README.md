SQLite Database Updater

Overview

The SQLite Database Updater is a Python script designed to update an SQLite database using data from an Excel file. 
The script reads the Excel file into a pandas DataFrame, processes the data, and updates the database table.

Features:

Reads data from an Excel file.
Processes the data and ensures column names are clean.
Updates an SQLite database, replacing the existing table if it exists.
Prints a confirmation message with the current date and time upon successful update.

Requirements:

Python 3.x
pandas library
SQLAlchemy library

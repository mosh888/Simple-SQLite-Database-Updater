import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

def update_database():
    # Database connection string for SQLite
    db_file = "path_to_your_database.db"  # Update this path to your database file
    engine = create_engine(f"sqlite:///{db_file}")

    # Read the Excel file
    input_file = "path_to_your_excel_file.xlsx"  # Update this path to your Excel file
    df = pd.read_excel(input_file)

    # Fix the column names if necessary
    df.columns = [col.strip() for col in df.columns]

    # Save the DataFrame to the SQLite database
    df.to_sql('Tracker', engine, if_exists='replace', index=False)  # The table name is 'Tracker'

    # Get the current date and time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Database table 'Tracker' updated successfully at {current_time}")

# Run the update_database function manually
update_database()

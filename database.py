import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("chat_app.db")
cursor = conn.cursor()

# Create the chat_history table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT,
        text_input TEXT,
        message TEXT
    )
""")

# Commit the changes and close the database connection
conn.commit()
conn.close()

def export_chat_data_to_csv():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("chat_app.db")
        cursor = conn.cursor()

        # Execute a SQL query to retrieve the chat data
        cursor.execute("SELECT user_email, text_input AS prompt, message AS result FROM chat_history")

        # Fetch all rows of data
        chat_data = cursor.fetchall()

        # Define the name of the CSV file
        csv_filename = "chat_data.csv"

        # Write the data to a CSV file
        with open(csv_filename, "w", newline="") as csv_file:
            # Create a CSV writer
            csv_writer = csv.writer(csv_file)

            # Write the header row with the new column names
            csv_writer.writerow(["user_email", "prompt", "result"])

            # Write the chat data
            csv_writer.writerows(chat_data)

        # Close the database connection
        conn.close()
        
        return {"message": "Data exported to CSV successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

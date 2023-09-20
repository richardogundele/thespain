
from pymongo import MongoClient
import sqlite3, json

history = {"richie@gmail.com":{ "hello":"how can i help you", "what is life": "life is good", "how can i stop lieing": "learn to stand for yourself and be a man of integrity"},
           "bola@gmail.com": {"how can you help me": "I can provide info on art", "what is a script": "a script is what i just mentioned"}}



connection = sqlite3.connect("chat_history.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_history (
        email TEXT PRIMARY KEY,
        chat_history JSON
    )
""")

for email, chat_data in history.items():
    cursor.execute("INSERT INTO chat_history (email, chat_history) VALUES (?, ?)",
                   (email, json.dumps(chat_data)))
# Commit the changes to the database.
connection.commit()

cursor.close()
connection.close()
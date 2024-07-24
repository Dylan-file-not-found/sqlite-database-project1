import sqlite3
import panda as pd
# Provide the correct path to your SQLite database file
df = pd.read.csv('data.csv')

df.columns = df.columns.str.strip()
connection = sqlite3.connect('SqliteDBproject.db')
df.to_sql('United_State',connection ,if_exists = "replace")
connection.close()

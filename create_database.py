import sqlite3

db_file = r"data\weather.db"
sql_file = r"sql\init.sql"

def create_db():
    with open(sql_file, 'r') as f:
        sql_script = f.read()

    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_script)

    print(">>>   Database created")
    conn.close()
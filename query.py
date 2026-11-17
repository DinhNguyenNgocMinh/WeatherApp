import sqlite3

sql_file = r"sql\read_all.sql"
db_file = r"data\weather.db"

def selectall():
    with open(sql_file, 'r', encoding='Utf-8') as f:
        sql_script = f.read()

    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_script)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    conn.close()

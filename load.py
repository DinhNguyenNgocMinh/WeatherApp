from transform import get_temperature
import sqlite3

db_file = r"data\weather.db"
sql_file = r"sql\insert_data.sql"
truncate_file = r"sql\truncate.sql"

def load():

    df = get_temperature()
    df = list(df.itertuples(index=False, name=None))

    with open(sql_file, 'r') as f:
        sql_script = f.read()

    with open(truncate_file, 'r') as t:
        truncate_script = t.read()

    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(truncate_script)
        cursor.executemany(sql_script, df)

    print(f'>>>   Write {len(df)} lines successfully into "{db_file}"')
    conn.commit()
    conn.close()
import create_database
import load
import query

if __name__ == "__main__":
    try:
        create_database.create_db()
        load.load()
        if input(" ________________________________\n|                                |\n| PRESS [ENTER] TO SHOW ALL DATA |\n| <SELECT * FROM bronze_weather> |\n|________________________________|\n\n") == '':
            query.selectall()
        print("\n>>> Done ETL!")
    except Exception as e:
        print(e)


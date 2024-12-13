
import psycopg2

# try-catch로 잡아서
try:
    db = psycopg2.connect(host='localhost', dbname='postgres', user='admin', password='1234', port=5432)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM items ORDER BY embedding <-> '[1,1,1]' LIMIT 1;")
    result = cursor.fetchall()

    if result:
        print(result)
    else:
        print("No data found.")
except psycopg2.Error as e:
    print(f"Database error: {e}")
finally:
    if db:
        db.close()

db.close()

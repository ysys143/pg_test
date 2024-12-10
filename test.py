import psycopg2
import numpy as np

# 연결
conn = psycopg2.connect(host='localhost', dbname='postgres', user='admin', password='1234', port=5432)
cursor = conn.cursor()

# 결과 확인
cursor.execute("SELECT * FROM vectors;")
results = cursor.fetchall()

for row in results:
    print(f"ID: {row[0]}, Vector: {row[1]}")
print(len(results))

# 연결 종료
cursor.close()
conn.close()
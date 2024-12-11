import psycopg2
import numpy as np

# 연결
#conn = psycopg2.connect(host='localhost', dbname='postgres', user='admin', password='1234', port=5432)
conn = psycopg2.connect(host='192.168.0.47', dbname='postgres', user='postgres', password='postgres1016', port=55432)
cursor = conn.cursor()

# 결과 확인
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
results = cursor.fetchall()

for row in results:
    print("Connection Succeed")
    print(f"ID: {row[0]}, Vector: {row[1]}")
print(len(results))

# 연결 종료
cursor.close()
conn.close()
import psycopg2

# 데이터베이스 연결
db = psycopg2.connect(host='localhost', dbname='postgres',user='admin',password='1234',port=5432) # 연결객체

cursor = db.cursor() # 작업객체

cursor.execute("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, num integer, data varchar);") # 테이블 생성
cursor.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def")) # 데이터 삽입
cursor.execute("select * from test;") # 쿼리 실행

print(cursor.fetchall()) # 모든 행을 가져와 출력합니다. cursor.fetchone(), cursor.fetchone(3)

db.commit()
db.close()


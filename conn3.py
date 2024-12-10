import psycopg2
import numpy as np

conn = psycopg2.connect(host='localhost', dbname='postgres', user='admin', password='1234', port=5432)

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS vectors (id bigserial PRIMARY KEY, embedding vector(5));")

# 벡터 생성
example_vectors = np.random.randn(10,5)

# 벡터 삽입
for vec in example_vectors:
    # 벡터 데이터를 삽입 (PostgreSQL의 vector 타입은 문자열 형태로 저장)
    cursor.execute(
        "INSERT INTO vectors (embedding) VALUES (%s)", 
        (vec.tolist(),)  # numpy 배열을 Python 리스트로 변환
    )

# 대량 삽입
vector_data = [(str(vec.tolist()),) for vec in example_vectors] # 벡터 데이터를 문자열로 변환

cursor.executemany(
    "INSERT INTO vectors (embedding) VALUES (%s)",
    vector_data
)

# 커밋
conn.commit()

# 삽입 확인
cursor.execute("SELECT * FROM vectors;")
results = cursor.fetchall()

def show(rows):
    for row in rows:
        print(f"ID: {row[0]}, Vector: {row[1]}")

print('\nAll Rows:')
show(results)

# 벡터 검색
test_vec = np.random.randn(1,5)
str_test_vec = test_vec.squeeze().tolist()

cursor.execute("SELECT * FROM vectors ORDER BY embedding <-> '{}' LIMIT 5".format(str_test_vec))
print('\nRetrieved Rows:')
results = cursor.fetchall()
show(results)

# 연결 종료
cursor.close()
conn.close()
import textwrap
from typing import List

import psycopg2

class VectorDB:

    _conn = None

    def __init__(self, host="localhost", port=5432, database="postgres", user="admin", password="1234"):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self._conn = None

    # DB에 연결
    def connect(self):
        conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password,
        )
        cursor = conn.cursor()
        cursor.execute("SET TIMEZONE TO 'Asia/Seoul'")
        cursor.execute(f"SET search_path TO 'public'")
        cursor.close()

        self._conn = conn

    # 연결 종료
    def close(self):
        if self._conn is not None:
            self._conn.close()
            self._conn = None

    # 쿼리 실행
    def execute_query(self, query: str):
        self.execute_queries([query])

    # 다중 쿼리 실행
    def execute_queries(self, queries: List[str]):
        queries = [textwrap.dedent(query) for query in queries]

        conn = self.get_conn()
        for query in queries:
            if query.strip():
                cursor = conn.cursor()
                cursor.execute(query)
                conn.commit()
                cursor.close()
                
    # 쿼리 실행결과를 반환
    def fetch_query(self, query: str):
        query = textwrap.dedent(query)

        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result

    # 실행계획 및 성능 분석
    def explain_analyze_query(self, query: str):
        query = textwrap.dedent(f"EXPLAIN ANALYZE {query}")

        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall() 
        cursor.close()

        return result

    # 현재 연결객체 반환
    def get_conn(self):
        self.connect()
        return self._conn
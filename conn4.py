from extension.pgvec import VectorDB

connect_config = {'host':'192.168.0.47', 'database':'postgres', 'user':'postgres', 'password':'postgres1016', 'port':55432}

vector = VectorDB(**connect_config)

# pgVector 생성
vector = VectorDB()

query = """
        SELECT * from items;
        """

vector.fetch_query(query)

vector.explain_analyze_query(query)

vector.get_conn()

vector.close()


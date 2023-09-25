import pyodbc


class MSSQLWrapper:

    def __init__(self, server, database, username, password, trust_cert):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.trust_cert = trust_cert
        self.connection = pyodbc.connect(f"DRIVER={{ODBC Driver 18 for SQL Server}};"
                                         f"SERVER={self.server};"
                                         f"DATABASE={self.database};"
                                         f"UID={self.username};"
                                         f"PWD={self.password};"
                                         f"TrustServerCertificate={self.trust_cert}")

    def execute_query(self, query, order_by, params=None, page_size=1000, page=1):
        offset = (page - 1) * page_size
        paging_query = f"{query} ORDER BY {order_by} OFFSET {offset} ROWS FETCH NEXT {page_size} ROWS ONLY"
        cursor = self.connection.cursor()
        if params is not None:
            cursor.execute(paging_query, params)
        else:
            cursor.execute(paging_query)
        rows = cursor.fetchall()
        return rows

    def count(self, query, params=None):
        cursor = self.connection.cursor()
        if params is not None:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        row = cursor.fetchone()
        count = row[0]
        return count

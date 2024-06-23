import psycopg2

class Database:
    def __init__(self, dbname, user, password, host):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
        )
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id SERIAL PRIMARY KEY,
            input JSONB,
            prediction JSONB
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS batch_predictions (
            id SERIAL PRIMARY KEY,
            input JSONB,
            prediction JSONB
        );
        """)

        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    db = Database(dbname='estimations', user='user', password='password', host='db')
    db.create_tables()
    db.close()


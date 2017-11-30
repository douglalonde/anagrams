import sqlite3
import os

SQLITE_DB_PATH = 'database.db'


class DBUtils:
    
    def __init__(self):
        self.conn = sqlite3.connect(SQLITE_DB_PATH)
        
    def create_db(self):
        try:
            curs = self.conn.cursor()
            curs.execute(
                "CREATE TABLE files ( blob_name TEXT, file_name TEXT, subject TEXT, serial TEXT, date TEXT, tags TEXT )")
            curs.execute(
                "CREATE UNIQUE INDEX fileindex ON files (file_name,subject,serial,date) ")
            self.conn.commit()
        except Exception as e:
            print(str(e))
            print('Failed to open a connection to sqlite db')
    
    def write_data(self, write_files):
        c = []
        for f in write_files:
            c.append((f['blob_name'], f['file_name'], f['subject'], f['serial'], f['date'], f['tags']))
        
        # @todo: should use self.conn
        conn = self.sqlite_get_conn()
        conn.executemany(
            """INSERT INTO files (blob_name, file_name, subject, serial, date, tags ) VALUES (?,?,?,?,?,?) """,
            c)
        conn.commit()
    
    def get_data(self):
        # @todo: should use self.conn
        conn = self.sqlite_get_conn()
        curs = conn.cursor()
        curs.execute("""SELECT blob_name, file_name, subject, serial, date, tags from files limit 10""")
        res = curs.fetchall()
        for i in res:
            yield ({'blob_name': i[0], 'file_name': i[1], 'date': i[4], 'subject': i[2], 'serial': i[3], 'tags': i[5]})
    
    def sqlite_get_conn(self):
        if os.path.exists(SQLITE_DB_PATH):
            try:
                conn = sqlite3.connect(SQLITE_DB_PATH)
                return conn
            except:
                print("DB seems to be here, but I cannot connect")
        else:
            self.create_db()
            try:
                conn = sqlite3.connect(SQLITE_DB_PATH)
                return conn
            except:
                print("DB seems to be here, but I cannot connect")
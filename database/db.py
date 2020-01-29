import sqlite3
from sqlite3 import Error
import os.path

class DB:
    connection = None
    cursor = None
    
    def connect(self):
        try:
            self.connection = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mjl.db"))
        except Error as e:
            print(e)

    def close(self):
        if self.connection:
            self.connection.close()

    def query(self, query):
        self.connect()
        
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        self.cursor.close()
        self.connection.commit()

        self.close()

    def one(self, query):
        self.connect()

        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        
        data = self.cursor.fetchone()

        self.cursor.close()
        self.connection.commit()

        self.close()

        return data

    def all(self, query):
        self.connect()

        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        
        data = self.cursor.fetchall()

        self.cursor.close()
        self.connection.commit()

        self.close()

        return data
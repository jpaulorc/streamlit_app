import sqlite3
from pathlib import Path
from sqlite3.dbapi2 import Cursor
import streamlit as st

class Database:
    def __init__(self, data_base_path: str) -> None:
        self.data_base_path = Path(data_base_path)
        self.__connection = self.create_connection()
        
    def create_connection(self):
        con = None
        try:
            con = sqlite3.connect(self.data_base_path)
            print("Connection Successfully Stablished")
        except sqlite3.Error as error:
            print(error)
        return con

    def execute_sql(self, sql_query, values=None) -> bool:
        if self.__connection:
            try:
                cursor = self.__connection.cursor()
                if values:
                    print(f"Executing Query: {sql_query}")
                    print(f"Values:  {values}")
                                        
                    cursor.execute(sql_query, values)
                    self.__connection.commit()
                    return True                    
            except sqlite3.Error as error:
                print(error)
                return False
        else:
            print("No connection was created")       
            return False
        

    def __del__(self):
        if self.__connection:
            print("Closing Database Connection...")
            self.__connection.close()
        else:
            print("No connection opened to be closed")
    
            
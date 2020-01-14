import psycopg2
from model.connection import *
class Display():
    """class for all print of the forum"""

    def __init__(self):
        self.choice=None
        self.choice=connection()


    def display_message(self):
        """method for display message and information of author """
        self.choice = connection()
        self.choice.initialize_connection()
        self.choice.cursor.execute("SELECT * FROM message;")
        view = self.choice.cursor.fetchall()
        print(view)
        self.choice.close_connection()

    def write_message(self):
        """method for add an message ina table with
        author and date and time indication"""
        self.choice = connection()
        self.choice.initialize_connection()
        self.choice.cursor.execute("INSERT INTO message(content, publishing_data, author) VALUES (content, publishing_data, author);")
        self.choice.connection.commit()
        self.choice.close_connection()

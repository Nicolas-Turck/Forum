import psycopg2
from model.connection import *
class Display():
    """class for all print of the forum"""

    def __init__(self):
        self.choice=None
        self.choice=connection()


    def display_message(self):
        """method for display message and information of author """

        self.choice.initialize_connection()
        self.choice.cursor.execute("SELECT * FROM message;")
        view = self.choice.cursor.fetchall()
        self.choice.close_connection()
        return view

    def write_message(self, content, aut):
        """method for add an message ina table with
        author and date and time indication"""
        #self.choice = connection()
        self.choice.initialize_connection()
        self.choice.cursor.execute("INSERT INTO message(content, publishing_date, author) VALUES (%s, NOW(), %s);",(content,aut))
        self.choice.connection.commit()
        self.choice.close_connection()

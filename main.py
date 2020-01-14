import os
from model.connection import *
from view.display import *

test = connection()
test.initialize_connection()
test.close_connection()
#show_message=Display()
#show_message=show_message.display_message()
user_choice = ""

while user_choice != "v" or user_choice != "w" or user_choice != "q":
    user_choice=input("choice (v)view, (w)write or (q)quit:")
    choice = Display()


    if user_choice == "v":
        choice.display_message()



    if user_choice == "w":
        choice.write_message()



    if user_choice == "q":
        exit()

import os
from model.connection import *
from model.display import *
from view.view import *

if __name__=='__main__':
    show = View()
    show.show_message()
    user_choice = ""

    while user_choice not in ["v", "w", "q"]:
        user_choice=input("choice (v)view, (w)write or (q)quit:")
        choice = Display()
        if user_choice == "v":
            show.show_message()

        if user_choice == "w":
            aut= input("enter your name:")
            content= input("enter your message:")
            choice.write_message(aut, content)

        if user_choice == "q":
            print("good bye")
            exit()

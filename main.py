import sqlite3
from show import *
from store import *
from database import *

class Password:
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    show_data(website, username, password)

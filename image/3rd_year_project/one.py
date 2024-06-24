from tkinter import *
from tkinter import ttk
import re
import pyodbc


conn = pyodbc.connect(
                        "Driver={SQL server};"
                        "Server=DESKTOP-SCH7GJR\SQLEXPRESS;"
                        "Database=project;"
                        "Trusted_Connection=yes;"

                      )
cursor = conn.cursor()
print('conn created')
cursor.execute("truncate table sell_id")
cursor.execute("drop table sell_id")
cursor.execute("select *from sell_id")
data = cursor.fetchall()
print('sell id table truncate')
print(data)



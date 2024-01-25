# insert, update, delete
import pyodbc as odbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-CUHVHGM\SQLEXPRESS'
DATABASE_NAME = 'Employee'
connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

try:
    con = odbc.connect(connection_string)  # generates the connection between ms sql server and python env.

    curs = con.cursor()  # create cursor
    curs.execute("select * from caldata")  # execute query through cursor

    for row in curs:
        for cell in row:
            print(cell, end=' ')
        print()

    con.close()

except:
    print("Connection Unsuccessful")
print("Finished....")



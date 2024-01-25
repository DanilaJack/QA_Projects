# insert, update, delete

insert_query = "Insert into student values(104, 'Karl')"
update_query = "Update student set sname='Jonny' where sid=104"
delete_query = "Delete from student where sid=104"

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
    curs.execute(delete_query)  # execute query through cursor
    con.commit()  # commit transaction

    con.close()

except:
    print("Connection Unsuccessful")
print("Finished....")



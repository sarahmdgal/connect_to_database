import sqlite3
connection = sqlite3.connect("company.db")

print(connection)
print(dir(connection))

sql_command = """
# CREATE TABLE employee (
#     staff_no int primary key,
#     fname varchar(20),
#     lname varchar(20),
#     gender char(1),
#     joining date,
#     birth_date date
# );
# """

cursor = connection.cursor()
# cursor.execute(sql_command)

insert_command = """INSERT INTO employee(staff_no, fname, lname, gender, birth_date)
VALUES(NULL, "Sarah", "Rubin", "F", "1776-07-04"),
      (NULL, "Frank", "Schiller", "M", "1955-08-17");"""
cursor.execute(insert_command)

select_command = """SELECT * FROM employee"""

cursor.execute(select_command)
results = cursor.fetchall()

for employee in results:
    print(employee)
connection.close()

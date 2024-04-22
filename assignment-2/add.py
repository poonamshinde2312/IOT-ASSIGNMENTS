import mysql.connector
import dbconn
def add_function():
    conn=dbconn.get_connection()

    empid = int(input("Enter the id: "))
    name = input("Enter the name: ")
    department=input("Enter the department: ")
    email = input("enter the eamil address: ")
    salary = int(input(" enter the salary: "))
    dateofjoining=input(" dateofjoining: ")

    query = f"insert into employees values({empid},'{name}','{department}','{email}',{salary},'{dateofjoining}');"

    cursor = conn.cursor()

    cursor.execute(query)

    conn.commit()

    cursor.close()

    conn.close()


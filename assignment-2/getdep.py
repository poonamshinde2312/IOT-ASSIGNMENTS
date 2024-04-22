# import mysql connector
import dbconn

def getdep_employees(department):
    conn=dbconn.get_connection()
    query = f"select * from employees where department=%s"
    val=(department,)

    cursor = conn.cursor()
    cursor.execute(query,val)

    records = cursor.fetchall()     
    print(records)

    cursor.close()
    conn.close()
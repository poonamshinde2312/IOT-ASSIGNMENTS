#import mysql.connector
import dbconn
def delete_employees(empid):
    conn=dbconn.get_connection()

    query = f"delete from employees where empid=%s"
    val=(empid,)

    cursor=conn.cursor()

    cursor.execute(query,val)

    conn.commit()

    cursor.close()
    conn.close()



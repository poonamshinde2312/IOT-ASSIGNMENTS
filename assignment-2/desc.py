# import mysql connector
import dbconn

def desc_employees():
    conn=dbconn.get_connection()
    query = f"select * from employees order by salary DESC;"

    cursor = conn.cursor()
    cursor.execute(query)

    records = cursor.fetchall()     
    print(f"highest:{records[0]}")
    print(f"lowest: {records[len(records)-1]}")

    cursor.close()
    conn.close()
# import mysql connector
import dbconn

def retrive_employees():

    conn=dbconn.get_connection()
    query = "select * from persons;"


    cursor = conn.cursor()
    cursor.execute(query)

    records = cursor.fetchall()     #   returns list of tuples
    print(records)

    cursor.close()
    conn.close()
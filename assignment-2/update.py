import dbconn

def update_employees(empid,salary):
    conn=dbconn.get_connection()

    query=f"update employees SET salary = %s where empid=%s;"

    val= (salary,empid)

    cursor=conn.cursor()

    cursor.execute(query,val)

    conn.commit()

    cursor.close()
    conn.close()

# emploeeid=int(input("enter which employeeid you want update"))
# salary=input("how much salary you allocate")
# update_person(emploeeid,salary)

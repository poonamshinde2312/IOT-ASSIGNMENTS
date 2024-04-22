import dbconn
from add import add_function
from delete import delete_employees
from update import update_employees
from retrive import retrive_employees
from getdep import getdep_employees
from desc import desc_employees

print(" 1.create  2.update  3.delete  4.retrive  5.getdep empl  6.desc order ")
choice= int(input("entr your choice: "))
match choice:
    case 1:
        add_function()
    case 2:
        empid=int(input("enter which employeeid you want update"))
        salary=input("how much salary you allocate")
        update_employees(empid,salary)
    case 3:
        empid=int(input("Enter employee id: "))
        delete_employees(empid)
    case 4:
        retrive_employees()
    case 5:
        department=input("Enter employee department: ")
        getdep_employees(department)
    case 6:
        desc_employees()
        
       


        

#Program 8
import sqlite3

def printData(res):
    print("Name".ljust(15),"USN".ljust(15),"Branch".ljust(15),"Email".ljust(15))
    for row in res :
        print(row[0].ljust(15),row[1].ljust(15),row[2].ljust(15),row[3].ljust(15))
    print("------------------")
#end of function
    
conn = sqlite3.connect('studentdb.db')
cur = conn.cursor()
print("---Connected to database successfully---")
#creating table
query = '''create table if not exists student(name varchar(30), usn char(10) primary key, branch char(3), email varchar(20));'''
cur.execute(query)
print("---Table created successfully---")
#Inserting student information
query = '''insert into student values (?,?,?,?);'''
lst = [('Shehyaaz','1BM17CS094','CSE','shehyaaz.cs17@bmsce.ac.in'),('Riyanchhi','1BM17CS076','CSE','riyanchhi.cs17@bmsce.ac.in')]
cur.executemany(query,lst)
print("---Data inserted successfully---")
#Displaying student information
print("Student information :")
query = '''select * from student'''
res = cur.execute(query)
printData(res)
#query and retrieve data of specific student
usn = input("Enter usn of student :")
query = '''select * from student where usn = (?);'''
res = cur.execute(query,[usn])
printData(res)
#update student information
usn, email = input("Enter usn and new email :").split()
query = '''update student set email = (?) where usn = (?);'''
cur.execute(query,(email,usn))
print("---Email updated successfully---")
query = '''select * from student;'''
res = cur.execute(query)
printData(res)
#delete a particular student
usn = input("Enter usn of student to delete :")
query = '''delete from student where usn = (?);'''
cur.execute(query,[usn])
print("---Data deleted successfully---")
query = '''select * from student;'''
res = cur.execute(query)
printData(res)
#end of program

'''
OUTPUT :
---Connected to database successfully---
---Table created successfully---
---Data inserted successfully---
Student information :
Name            USN             Branch          Email          
Shehyaaz        1BM17CS094      CSE             shehyaaz.cs17@bmsce.ac.in
Riyanchhi       1BM17CS076      CSE             riyanchhi.cs17@bmsce.ac.in
------------------
Enter usn of student :1BM17CS076
Name            USN             Branch          Email          
Riyanchhi       1BM17CS076      CSE             riyanchhi.cs17@bmsce.ac.in
------------------
Enter usn and new email :1BM17CS094 isknayazi2@gmail.com
---Email updated successfully---
Name            USN             Branch          Email          
Shehyaaz        1BM17CS094      CSE             isknayazi2@gmail.com
Riyanchhi       1BM17CS076      CSE             riyanchhi.cs17@bmsce.ac.in
------------------
Enter usn of student to delete :1BM17CS094
---Data deleted successfully---
Name            USN             Branch          Email          
Riyanchhi       1BM17CS076      CSE             riyanchhi.cs17@bmsce.ac.in
------------------
'''

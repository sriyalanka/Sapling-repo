import mysql.connector as sql
conn = sql.connect(host = 'localhost',
                   user = 'root',   
                   password = 'root123',
                   database = 'test7')
if conn.is_connected():
    print("successfully connected")
cl=conn.cursor()
print()

#Method of creating a table
query='''create table Employee 
        ( 
         Employee_name varchar(32) NOT NULL , 
         Age varchar(10), 
         Address varchar(100), 
         Phone_no varchar(10), 
         Email_ID varchar(32),
         ID_number varchar(10) NOT NULL PRIMARY KEY
         )'''
cl.execute(query)
print("Table created")
print()

while True:
    print("\n 1.Insert\n 2.Delete\n 3.Search\n 4.Display All Records\n 5.Update\n")
    a=int(input("Enter your choice (1-5)"))  
    
    if a==1:
        a=input("Enter the name = ")
        b=input("Enter your age = ")
        c=input("Enter your address = ")
        d=input("Enter your phone number = ")
        e=input("Enter your email id = ")
        f=input("Enter your id number = ")
        query = '''insert into Employee(Employee_name,age,Address,Phone_no,Email_ID,ID_number) values ('{}',{},'{}','{}','{}','{}')'''.format(a,b,c,d,e,f)
        print(query)
        cl.execute(query)
        conn.commit()
        print("Data inserted")
        print()

    if a==2:
        delete_record = input("Please type the Id number : ")
        query = '''delete from employee where ID_number=''' + delete_record
        print(query)
        cl.execute(query)
        conn.commit()
        print("Data Deleted")
        print()
        

        
    if a==3:
        search_record=input("Enter the ID number for searching the record : ")
        query='''select * from employee where ID_number =''' + search_record
        print(query)
        cl.execute(query)
        records=cl.fetchall()
        print('--------------------------------------------------------------------------------------------------')
        print('|Employee_name\t|age\t|Address\t|Phone_no\t|Email_ID\t\t|ID_number\t|')
        print('--------------------------------------------------------------------------------------------------')
        for i in records:
            print('|{}\t\t|{}\t|{}\t|{}\t|{}\t|{}\t|'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
            print('--------------------------------------------------------------------------------------------------')
        print()
        

    if a==4:
        query='''select * from employee'''
        print(query)
        cl.execute(query)
        records=cl.fetchall()
        print('--------------------------------------------------------------------------------------------------')
        print('|Employee_name\t|age\t|Address\t|Phone_no\t|Email_ID\t\t|ID_number\t|')
        print('--------------------------------------------------------------------------------------------------')
        for i in records:
            print('|{}\t\t|{}\t|{}\t|{}\t|{}\t|{}\t|'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
            print('--------------------------------------------------------------------------------------------------')
        print()
        
    if a==5:
        print("\n UPDATE CHOICES : \n")
        print("\n 1.To update 'age' \n 2.To update 'Employee_name' \n 3.To update 'Address' \n 4.To update 'Phone_No' \n 5.To update 'Email_ID' \n")
        k=int(input("Enter your choice (1-5)"))
        if k==1:
            value=input("Enter the age value which has to be updated")
            Id_number=input("Enter Id number of the updating record")
            query = '''update employee set age='''+"'"+value+"'"+' where ID_number='+"'"+Id_number+"'"
        if k==2:
            value=input("Enter the Employee_name value which has to be updated")
            Id_number=input("Enter Id number of the updating record")
            query = '''update employee set Employee_name='''+"'"+value+"'"+' where ID_number='+"'"+Id_number+"'"
        if k==3:
            value=input("Enter the Address value which has to be updated")
            Id_number=input("Enter Id number of the updating record")
            query = '''update employee set Address='''+"'"+value+"'"+' where ID_number='+"'"+Id_number+"'"
        if k==4:
            value=input("Enter the Phone_no value which has to be updated")
            Id_number=input("Enter Id number of the updating record")
            query = '''update employee set Phone_no='''+"'"+value+"'"+' where ID_number='+"'"+Id_number+"'"
        if k==5:
            value=input("Enter the Email_ID value which has to be updated")
            Id_number=input("Enter Id number of the updating record")
            query = '''update employee set Email_ID='''+"'"+value+"'"+' where ID_number='+"'"+Id_number+"'"
        print(query)
        cl.execute(query)
        conn.commit()
        print("Data updated")
        print()
else:
    print("INVALID CHOICE")

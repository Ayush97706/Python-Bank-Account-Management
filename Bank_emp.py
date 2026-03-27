import mysql.connector

connect=mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    database='Bank_emp'
    
)

cursor=connect.cursor()

def add_cus():
    acc_no = int(input("Enter Your acc num : "))
    name = input("Enter your name : ")
    balance = int(input("Enter your Balance : "))
    acc_type = input("Enter Acc type : ")

    query="insert into emp (acc_no,name,balance,acc_type ) values(%s,%s,%s,%s)"
    values=(acc_no,name,balance,acc_type)

    try:
        cursor.execute(query,values)
        connect.commit()
        print("Add customer successfully")

    except mysql.connector.IntegrityError:
        print("Customer already excist !")

# add_cus()  

def view_list():
    cursor.execute("Select * from emp ")
    rows = cursor.fetchall()
    if rows:
        print("Customer Record : ")
        for row in rows :
            print(f"acc_no : {row[0]},name : {row[1]},balance : {row[2]},acc_type : {row[3]}")

    else: 
        print("No Record Found ")

# view_list()    

def update_customer():
    acc_no=int(input("Enter acc num which you have to update : "))
    cursor.execute("Select * from emp where acc_no = %s ",(acc_no,))
    if cursor.fetchone():
        name=input("Enter new name : ")
        balance=int(input("Enter new Balance :"))
        acc_type=input("Enter new Acc Type : ")

        query = "update emp set name = %s, balance = %s , acc_type = %s where acc_no = %s " 
        values=(name,balance,acc_type,acc_no)

        cursor.execute(query,values)
        connect.commit()
        print("Update Successfull ")

    else :
        print("Record Not Found ")    

# update_customer()      

def delete_rec():
    acc_no=int(input("Enter a Acc Number you want to delete : "))
    cursor.execute("select * from emp where acc_no = %s ",(acc_no,)) 
    if cursor.fetchone():
        cursor.execute("delete from emp where acc_no = %s ",(acc_no,)) 
        connect.commit()
        print("Acc delete successfully...")

    else :
        print("Record not found ") 

# delete_rec()    

def deposite():
    acc_no=int(input("Enter a Account number You want to deposite : "))
    cursor.execute("Select * from emp where acc_no = %s ",(acc_no,))
    row=cursor.fetchone()
    if row:
        amount=int(input("Enter amount you want to deposit : "))
        new_balance = row[0]+amount
        cursor.execute("Update emp set balance = %s where acc_no = %s ",(new_balance,amount))
        connect.commit()
        print(f"{amount} Deposite successfully! New Balance : {new_balance}")

    else : 
        print("Record Not Found ! ")    

# deposite()        

def withdraw():
    acc_no=int(input("Enter Acc number for withdraw money : "))
    cursor.execute("Select * from emp where acc_no = %s",(acc_no,))
    row=cursor.fetchone()

    if row:
        amount=int(input("Enter amount you want to withdraw : "))

        if amount>row[0]:
            print("Insufficiant Balance ! ")

        else :
            new_balance=row[0] - amount

        cursor.execute("Update emp set balance = %s where acc_no = %s ",(new_balance,amount))    
        connect.commit()
        print(f" {amount} Withdraw Successfully ! new balance : {new_balance} ")

    else : 
        print("Record not found : ")  

# withdraw()          

def search():
    acc_no=int(input("Enter a Acc number : "))
    cursor.execute("Select * from emp where acc_no = %s ",(acc_no,))
    row=cursor.fetchone()

    if row :
        print ("\n**** Customer Details****\n")
        print(f"Account number : {row[0]}")
        print(f"Name : {row[1]}")
        print(f"Balance : {row[2]}")
        print(f"Acc type : {row[3]}")

    else : 
        print("Record not found ! ")   

# search()  

def menu():
    while True:
        print("Bank Account Management System ")    
        print("1. Add customer ")   
        print("2. View list ")
        print("3. Update Customer ")
        print("4. delete customer account ")
        print("5. deposite")
        print("6. withdraw ")
        print("7. Search Account Details")
        print("8. Exit  ")

        choice=input("Enter your choice : ")
        if choice == '1':
            add_cus()
        elif choice == '2':
            view_list()    
        elif choice == '3':
            update_customer()    
        elif choice == '4':
            delete_rec()    
        elif choice == '5':
            deposite()
        elif choice == '6':
            withdraw()  
        elif choice == '7':
            search()       
        elif choice == '8':
            print("Exiting ..")    
            break
        else :
            print("Invalid Choice ") 

menu()            













# FOR MAKING ALTERATIONS IN THE TABLE
# ALTERATIONS LIKE VIEW,DELETE,APPEND TABLE


import mysql.connector

pswrd = input("Enter Password of root User : ")
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=pswrd,
    database="PensionManagement")

cursor = mydb.cursor()

D = True
while D:

    change = input("""WHAT OPERATIONS FROM THE FOLLOWING WOULD YOU LIKE TO PERFORM:
           FOR VIEWING TABLE DATA PRESS -> 1
           FOR DELETING ANY ENTRY FROM TABLE DATA PRESS -> 2
           FOR ADDING NEW PERSON IN TABLE DATA PRESS -> 3
           :""")

    if int(change) == 1:
        cursor.execute("SELECT * FROM PENSIONDATA;")
        vw = cursor.fetchall()
        for i in vw:
            print(i)
    elif int(change) == 2:
        N = input('NAME OF THE PERSON YOU WANT TO REMOVE FROM LIST:')
        mys = "DELETE FROM PENSIONDATA WHERE NAME = %s"
        cursor.execute(mys, (N,))
        mydb.commit()
    elif int(change) == 3:
        sql = "INSERT INTO PENSIONDATA(account_number, dob, name, pension)  VALUES(%s, %s, %s, %s)"
        NAME = input("NAME OF THE PERSON YOU WANT TO ADD IN TABLE:")
        BANK_ACCOUNT = input("THEIR BANK ACCOUNT NUMBER :")
        dob = input('DATE OF BIRTH ("YYYY/MM/DD" FORMAT):')
        PENSION = int(input("AMOUNT OF THEIR PENSION:"))
        new = (BANK_ACCOUNT, dob, NAME, PENSION)
        cursor.execute(sql, new)
        mydb.commit()
    else:
        print("not defined")
    print("DO YOU WANT TO CONTINUE?(Y/N) -> ")
    option = input()
    if option == 'y' or option == "Y":
        D = True
    else:
        D = False

print("""
THANK YOU!!! FOR USING OUR PLATFORM, I HOPE YOU LIKED IT. WE ARE WILLING TO WORK WITH YOU AGAIN, HAVE A GOOD DAY!!!""")

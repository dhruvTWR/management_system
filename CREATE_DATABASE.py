import random
import mysql.connector

bank_numb = []
dob_lis = []
final_name_lis = []
data = []


def createdata(numb_t):
    def accountnumber():
        bankname = ["sbi", "pnb", "ubi", "hdc", "inb"]
        bankcode = {"sbi": 1000, "pnb": 1003,
                    "ubi": 2002, "hdc": 1045, "inb": 1004}
        for i in range(0, numb_t):
            selected = bankname[random.randint(0, len(bankname) - 1)]
            banknumber = selected + str(bankcode[selected]) + str(random.randint(1, 999)).zfill(
                3) + str(random.randint(1, 100)).zfill(3) + str(random.randint(1, 100)).zfill(2) + "\n"
            bank_numb.append(banknumber)

    def dob():
        for i in range(0, numb_t):
            dd = random.randint(1, 27)
            mm = random.randint(1, 12)
            yyyy = random.randint(1945, 1961)
            dob_lis.append(str(yyyy).zfill(4) + "-" +
                           str(mm).zfill(2) + "-" + str(dd).zfill(2) + "\n")

    def generate_names():
        n = open("name.txt", "r")
        sn = open("surnames.txt", "r")
        n_data = n.readlines()
        sn_data = sn.readlines()
        for i in range(0, numb_t):
            name = n_data[random.randint(
                0, len(n_data) - 1)][0:-1] + " " + sn_data[random.randint(0, len(sn_data) - 1)]
            final_name_lis.append(name)
        n.close()
        sn.close()

    def getpension(date):
        least_pen = 1000
        per_yr_inc = 50
        current_yr = date[:4]
        y_range = 2022 - int(current_yr) - 60
        pension = least_pen + y_range * per_yr_inc
        return pension

    def assembeldata():
        accountnumber()
        dob()
        generate_names()
        master_data = []
        for i in range(0, numb_t):
            master_data.append((bank_numb[i].rstrip(), dob_lis[i].rstrip(
            ), final_name_lis[i].rstrip(), getpension(dob_lis[i].rstrip())))
        return master_data

    dt = assembeldata()
    return dt


def createdatabase(dt):
    pswrd = input("Enter Password of root User : ")
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password=pswrd,
            database="PensionManagement")
        cursor = mydb.cursor()
    except:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password=pswrd)
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE PensionManagement")
    try:
        cursor.execute("drop TABLE PensionData")
    except:
        pass
    cursor.execute(
        "create TABLE PensionData(account_number varchar(64), dob DATE, name varchar(64), pension int)")
    mydb.commit()
    command = "insert into PensionData(account_number, dob, name, pension) values (%s, %s, %s, %s)"
    for i in dt:
        cursor.execute(command, (i[0], i[1], i[2], i[3]))
        mydb.commit()


numberofentries = int(input("Enter Number Of Entries You Want To produce : "))
data1 = createdata(numberofentries)
createdatabase(data1)

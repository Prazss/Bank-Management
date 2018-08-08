from databaseConn import *
from functions import * 
from datetime import *
from db_spare_functions import *
from db_sign_in import *

def addressChange(cid):
    
    print('Fill the following details below')
    
    addr_line1 = changeAddressLine1()
    addr_line2 = changeAddressLine2()
    city = changeCity()
    state = changeState()
    pincode = changePincode()
    
    choice = raw_input('Check your details properly.....Is there something you want to change or do you wish to proceed ? (Y for Yes and N for No) : ')
    
    if(choice == 'Y' or choice == 'y'):
    
        print('1.First line of Address\t\t2.Second line of Address\t3.City')
        print('4.State\t\t\t\t5.Pincode')
    
        loop = 1
        while (loop != 0):
            choose = input('Enter the number of the field you wish to change or zero if you wish to leave = ')
            if(choose == 1):
                address_line1 = changeAddressLine1()
            elif(choose == 2):
                address_line2 = changeAddressLine2()
            elif(choose == 3):
                city = changeCity()
            elif(choose == 4):
                state = changeState()
            elif(choose == 5):
                pincode = changePincode()
            elif(choose == 0):
                loop = 0
            else:
                print('Wrong Choice......Try again!!!')
         
     
    else:
        print('Ok !!!')
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    cur.execute("update CUSTOMER set Address_line1='%s',Address_line2='%s',City='%s',State='%s',Pincode='%s' where Cust_id='%s';" % \
                (addr_line1,addr_line2,city,state,pincode,cid))
                
    conn.commit()
    
    print('Your address has been changed!\n')
    
def depositMoney(cid):
    
    amount = input('Enter the amount you want to deposit = ')
    
    day = str(date.today())
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    cur.execute("insert into DEPOSIT values(default,'%s','%s','%s');" % (cid,amount,day))
    
    conn.commit()
    
    cur.execute("call addMoney('%s','%s');" % (cid,amount))
    
    conn.commit()
    
    print('Your money has been deposited into your account!')
    print('Deposit Reference Number is D%05d' % depositID())
    showBalance(cid)
    
def withdrawMoney(cid):
    
    amount = input('Enter the amount you want to withdraw = ')
    
    if(amount>checkBalance(cid)):
        print("Sorry, you don't have sufficient balance to withdraw!!!!\n")
        showBalance(cid)
    else:
    
        day = str(date.today())
    
        conn = connectToMySQL()
        cur = conn.cursor()
    
        cur.execute("insert into WITHDRAWAL values(default,'%s','%s','%s');" % (cid,amount,day))
    
        conn.commit()
    
        cur.execute("call removeMoney('%s','%s');" % (cid,amount))
    
        conn.commit()
    
        print('Successful withdrawal!!')
        print('Withdrawal Reference Number is W%05d' % withdrawalID())  
        showBalance(cid)
        
def transferMoney(cid):
    
    amount = input("Enter the amount you want to transfer = ")
    
    if(amount>checkBalance(cid)):
        print("Sorry, you don't have sufficient balance to withdraw!!!!")
        showBalance(cid)
        
    else:
        
        loop = 0
        while(loop==0):
            rid = input("Enter the Account Number to whom you want to transfer the money = ")
            
            if userCheck(rid)!=0:
                loop = 1
                day = str(date.today())
    
                conn = connectToMySQL()
                cur = conn.cursor()
    
                cur.execute("insert into TRANSFER values(default,'%s','%s','%s','%s');" % (cid,rid,amount,day))
    
                conn.commit()
    
                cur.execute("call transMoney('%s','%s','%s');" % (cid,rid,amount))
    
                conn.commit()
    
                print('Successful transfer!!')
                print('Transfer Reference Number is T%05d' % transferID())
                showBalance(cid)
            
            else:
                
                print("Wrong Account Number!!!!Such Account Number doesn't exist!!!")
                
def accountClosure(cid):
    
    choice = raw_input("Are you sure you want to close the account ?? (Y for Yes and N for No) : ")
    
    if(choice == 'Y' or choice == 'y'):
        
        day = str(date.today())
        conn = connectToMySQL()
        cur = conn.cursor()
        
        print("As you wish !!! Your account is closed now.")
        print("Your balance amount Rs.%.2f can be retrieved from the nearest branch." % checkBalance(cid))
        print("Goodbye!!!")
        
        cur.execute("update ACCOUNT set Status='CLOSE',Status_date='%s' where Acc_no='%s';" % (day,cid))
        
        conn.commit()
    
    return choice
    
def printStatement(cid):
    
    start_date = raw_input("Enter the start-date in yyyy-mm-dd format : ")
    end_date = raw_input("Enter the end-date in yyyy-mm-dd format : ")
    
    print("\nDeposits ----")
    depositStatement(cid, start_date, end_date)
    print("\nWithdrawals ----")
    withdrawalStatement(cid, start_date, end_date)
    print("\nTransfers ----")
    transferFromStatement(cid, start_date, end_date)
    transferToStatement(cid, start_date, end_date)
    
    
    
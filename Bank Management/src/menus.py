from databaseConn import *
from db_sign_in import *
from db_sign_up import *
from datetime import date
from functions import *
from db_options_sub_menu import *
from db_admin_functions import *
from curses.ascii import isdigit

class Customer(object):
    def __init__(self,first_name=None,last_name=None,dob=None,address_line1=None,address_line2=None,city=None,state=None,pincode=0,profession=None,contact=None,email=None,branch_name=None,password=None):
        self.first_name=first_name
        self.last_name=last_name
        self.dob=dob
        self.address_line1=address_line1
        self.address_line2=address_line2
        self.city=city
        self.state=state
        self.pincode=pincode
        self.profession=profession
        self.contact=contact
        self.email=email
        self.branch_name=branch_name
        self.password=password
        
        
def menu():
    print('\n************MENU************\n')
    print('1.Sign Up')
    print('2.Sign In')
    print('3.Admin Login')
    print('4.Quit\n')
    print('==============================================================================================')
    
    return input ("Choose your option: ")

def sign_in_menu():
    print('Login with your details --- ')
    count=0
    while count < 3:
        cid = raw_input('Customer ID : ')
        
        if userCheck(cid)!=0:
            
            if blockCheck(cid)!=1:
            
                pswd = raw_input('Password : ')
        
                if pswd==loginAccess(cid, pswd):
                    print('Access granted.')
                    count = 0
                    welcomePrint(cid)
                    sub_menu(cid)

                    break
                else:
                    count += 1
        
                    if(count<3):
                        print('Access denied. Try again.')
                        
                    else:
                        blockAccount(cid)
                        print("Your account is blocked!!! Visit the nearest branch for revival of the account.")
                            
            else:
                
                print("Your account has been blocked!!! Visit the nearest branch for revival of the account.")
                break
    
        else:
            print("Invalid Customer ID\n")
    

def sign_up_menu():
    
    print('To sign up, you have to provide your details to the bank ----\n\n')
    
    customer = Customer()
    
    customer.first_name = raw_input('First Name\t\t: ')
    
    customer.last_name = raw_input('Last Name\t\t: ')
    
    customer.dob = raw_input('Date Of Birth (In yyyy-mm-dd format)\t: ')
    
    customer.address_line1 = raw_input('First line of Address\t: ')
    
    customer.address_line2 = raw_input('Second line of Address\t: ')
    
    customer.city = raw_input('City\t\t\t: ')
    
    customer.state = raw_input('State\t\t\t: ')
    
    customer.pincode = raw_input('Pincode\t\t\t: ')
    
    if(checkPincode(customer.pincode)!=0):
            print('Pincode not appropriate!! Enter again....')
            customer.pincode = changePincode()
    
    customer.profession = raw_input('Profession\t\t: ')
    
    customer.contact = raw_input('Contact No.\t\t: ')
    if(checkContact(customer.contact)!=0):
        print('Contact number not appropriate!! Enter again....')
        customer.contact = changeContact()
        
    customer.email = raw_input('Email ID\t\t: ')
    if(checkEmail(customer.email)==0):
        print('Email ID inappropriate!! Enter again....')
        customer.email = changeEmail()
    
    customer.branch_name = raw_input('Branch Name\t\t: ')
    if(checkBranch(customer.branch_name)==0):
        print('Such Branch does not exist!! Enter it again.')
        customer.branch_name = changeBranchName()
    
    customer.password = raw_input('Password\t\t: ')
    
    choice = raw_input('Check your details properly.....Is there something you want to change or do you wish to proceed ? (Y for Yes and N for No) : ')
    
    if(choice == 'Y' or choice == 'y'):
    
        print('1.First Name\t\t\t2.Last Name\t\t\t3.Date Of Birth')
        print('4.First line of Address\t\t5.Second line of Address\t6.City')
        print('7.State\t\t\t\t8.Pincode\t\t\t9.Profession')
        print('10.Contact\t\t\t11.Email\t\t\t12.Branch Name')
        print('13.Password\n\n')
    
        loop = 1
        while (loop != 0):
            choose = input('Enter the number of the field you wish to change or zero if you wish to leave = ')
            if(choose == 1):
                customer.first_name = changeFirstName()
            elif(choose == 2):
                customer.last_name = changeLastName()
            elif(choose == 3):
                customer.dob = changeDOB()
            elif(choose == 4):
                customer.address_line1 = changeAddressLine1()
            elif(choose == 5):
                customer.address_line2 = changeAddressLine2()
            elif(choose == 6):
                customer.city = changeCity()
            elif(choose == 7):
                customer.state = changeState()
            elif(choose == 8):
                customer.pincode = changePincode()
            elif(choose == 9):
                customer.profession = changeProfession()
            elif(choose == 10):
                customer.contact = changeContact()
            elif(choose == 11):
                customer.email = changeEmail()
            elif(choose == 12):
                customer.branch_name = changeBranchName()
            elif(choose == 13):
                customer.password = changePassword()
            elif(choose == 0):
                loop = 0
            else:
                print('Wrong Choice......Try again!!!')
     
    else:
        print('Ok %s!!' % customer.first_name)         
    
    if(checkExistCust(customer.contact, customer.email)!=0):
        print('You have already created an account !!!')
        
    else:
        done = addCustomer(customer.first_name,customer.last_name,customer.dob,customer.address_line1,customer.address_line2,customer.city,customer.state,customer.pincode,customer.profession,customer.contact,customer.email,customer.branch_name)
        if(done != 0):
            cid = getCustID(customer.contact,customer.email)
            welcomePrint(cid)
            print('Your Customer ID is %s.' % cid)
        
            addLogin(cid,customer.password)
        
            print('Account Details ---\n\n')
        
            print('Account No.\t\t: %s' % cid)
            doo = str(date.today())
            print('Date Of Opening\t\t: %s' % doo)
            typeacc = raw_input('Type(Current or Savings): ')
            
            di = 0
            while di==0 :
                balance = raw_input('Balance\t\t\t: ');
                if(typeacc=="Current" and int(balance)<5000):
                    print("Hello")
                    print("For Current account, balance should Rs.5,000.00!!!!")
                else:
                    di=1
            
            createAcc = addAccount(cid, doo, typeacc, balance)
        
            if(createAcc != 0):
                print('Account created. Enjoy banking.\n')
                sub_menu(cid)

def sub_menu_display():
    
    print('\n************MENU************\n')
    print('1.Address Change')
    print('2.Money Deposit')
    print('3.Money Withdrawal')
    print('4.Print Statement')
    print('5.Transfer Money')
    print('6.Account Closure')
    print('7.Logout\n')
    print('==============================================================================================')
    
    return input ("Choose your option: ")

def sub_menu(cid):

    loop = 1
    choice = 0
    while loop == 1:
        choice = sub_menu_display()
        if choice == 1:
            addressChange(cid)
        elif choice == 2:
            depositMoney(cid)
        elif choice == 3:
            withdrawMoney(cid)
        elif choice == 4:
            printStatement(cid)
        elif choice == 5:
            transferMoney(cid)
        elif choice == 6:
            isClosed = accountClosure(cid)
            if(isClosed=='Y' or isClosed=='y'):
                loop = 0
        elif choice == 7:
            loop = 0
            print("Good day to you!!!")
        else:
            print('Wrong Choice......Try again!!!')
            
        
def admin_menu_display():
    
    print('Login with your details --- ')
    count=1
    while count > 0:
        adminid = raw_input('Admin ID : ')
        
        if adminCheck(adminid)!=0:
            
            pswd = raw_input('Password : ')
        
            if (pswd==loginAdmin(adminid,pswd)):
                print('Access granted.')
                count = 0
                admin_menu(adminid)
                
            else:
                count += 1
                print('Access denied. Try again.')
                            
            
        else:
            print("Invalid Admin ID\n")
    
def admin_menu(adminid):
    
    print('\n************MENU************\n')
    print('1.Closed Account History')
    print('2.Logout\n')
    print('==============================================================================================')
    
    choice = input ("Choose your option: ")

    if choice == 1:
        closedAccount(adminid)
    elif choice == 2:
        print("Goodbye Admin!!!!")
    else:
        print('Wrong Choice......Try again!!!')
    
    return
    
    
    
    
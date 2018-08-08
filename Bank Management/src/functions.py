from db_sign_up import *

def changeFirstName():
    
    first_name = raw_input('First Name : ')
    return first_name
    
def changeLastName():
    
    last_name = raw_input('Last Name : ')
    return last_name
    
def changeDOB():
    
    dob = raw_input('Date Of Birth (In yyyy-mm-dd format : ')
    return dob
    
def changeAddressLine1():
    
    addr_line1 = raw_input('First line of Address : ')
    return addr_line1
    
def changeAddressLine2():
    
    addr_line2 = raw_input('Second line of Address : ')
    return addr_line2
    
def changeCity():
    
    city = raw_input('City : ')
    return city
    
def changeState():
    
    state = raw_input('State : ')
    return state
    
def changePincode():
    
    pincode = raw_input('Pincode : ')
    if(checkPincode(pincode)!=0):
        print('Pincode not appropriate!! Enter again....')
        pincode = changePincode()
    
    return pincode
    
def changeContact():
    
    contact = raw_input('Contact : ')
    if(checkContact(contact)!=0):
        print('Contact number not appropriate!! Enter again')
        contact = changeContact()

    return contact

def changeProfession():
    
    profession = raw_input('Profession : ')
    return profession
    
def changeEmail():
    
    email = raw_input('Email ID : ')
    if(checkEmail(email)==0):
        print('Email ID inappropriate!! Enter again....')
        email = changeEmail()
        
    return email

def changeBranchName():
    
    branch_name = raw_input('Branch Name : ')
        
    r = checkBranch(branch_name)
        
    if(r==0):
        print('Such Branch does not exist!! Enter it again.')
        branch_name = changeBranchName()
    
    return branch_name
        
def changePassword():
    
    pswd = raw_input('Password : ')
    return pswd

def checkContact(contact):
    
    r = 0
    if(len(contact)>10 or len(contact)<10):
        r = 1
    return r

def checkPincode(pincode):
    
    r = 0
    if(len(pincode)!=6):
        r = 1
        
    return r

def checkEmail(email):
    
    r = 0
    if '@' in email and '.' in email:
        r = 1
        
    return r
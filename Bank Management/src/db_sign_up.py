from databaseConn import *

def addCustomer(first_name,last_name,dob,addr_line1,addr_line2,city,state,pincode,profession,contact,email,branch_name):
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    r = cur.execute("insert into CUSTOMER values(default, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" \
                % (first_name,last_name,dob,addr_line1,addr_line2,city,state,pincode,profession,branch_name,contact,email))
    
    conn.commit()
    
    return r

def getCustID(contact,email):
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    cur.execute("select Cust_id from CUSTOMER where Contact='%s' and Email='%s';" % (contact,email))
    
    rs = cur.fetchone()
    
    return rs[0]

def addLogin(cid,pswd):
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    cur.execute("insert into LOGIN values('%s', '%s', 'NO');" % (cid,pswd))
    
    conn.commit()
  
def addAccount(cid,doo,typeacc,balance):
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    r = cur.execute("insert into ACCOUNT values('%s', '%s', '%s', '%s', 'OPEN', NULL);" % (cid,typeacc,doo,balance))
    
    conn.commit()
  
    return r

def checkBranch(branch_name):
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    cur.execute("select count(*) from BRANCH where Branch_name = '%s';" % branch_name)
    
    r = cur.fetchone()
    
    return r[0]

def checkExistCust(contact,email):
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    cur.execute("select Count(Cust_id) from CUSTOMER where Contact = '%s' and Email = '%s';" % (contact,email))
    
    r = cur.fetchone()
        
    return r[0]
    
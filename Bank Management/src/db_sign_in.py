from databaseConn import *

def userCheck(cid):

    conn = connectToMySQL()
    cur = conn.cursor()

    rs = cur.execute("select * from LOGIN where Cust_id = '%s';" % cid)

    return rs

def blockCheck(cid):
    
    block = 0
    conn = connectToMySQL()
    cur = conn.cursor()
    cur.execute("select Block from LOGIN where Cust_id = '%s';" % cid)
    
    rs = cur.fetchone()
    
    if(rs[0] == "YES"):
        block = 1
    
    return block

def loginAccess(cid,pswd):
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    cur.execute("select Password from LOGIN where Cust_id = '%s';" % cid)
    
    dbpswd = cur.fetchone()
    
    return dbpswd[0]

def welcomePrint(cid):
    
    conn = connectToMySQL()
    cur = conn.cursor()
    cur.execute("select First_name,Last_name from CUSTOMER where Cust_id = '%s';" % cid)
    
    result = cur.fetchone()
    
    print('Welcome %s %s. ' % (result[0],result[1]))
    
def blockAccount(cid):
    
    conn = connectToMySQL()
    cur = conn.cursor()

    cur.execute("update LOGIN set Block='YES' where Cust_id = '%s';" % cid)
    
    conn.commit()
    
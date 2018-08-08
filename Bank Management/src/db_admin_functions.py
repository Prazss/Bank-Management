from databaseConn import *

def adminCheck(adminid):

    conn = connectToMySQL()
    cur = conn.cursor()

    rs = cur.execute("select * from ADMIN where ID = '%s';" % adminid)

    return rs

def loginAdmin(adminid, pswd):
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    cur.execute("select Password from ADMIN where ID = '%s';" % adminid)
    
    dbpswd = cur.fetchone()
    
    return dbpswd[0]

def closedAccount(adminid):
    
    conn = connectToMySQL()
    curo = conn.cursor()
    
    curo.execute("select Branch_name from ADMIN where ID='%s';" % adminid)
    
    res = curo.fetchone()
    
    print("Following are the closed accounts of %s Branch with dates ----- \n" % res[0])
    print("Account No.\tDate of closure\n")
    
    cur = conn.cursor()
    
    cur.execute("select a.Acc_no,a.Status_date \
                from ACCOUNT a,CUSTOMER c \
                where a.Acc_no=c.Cust_id and a.Status='CLOSE' and c.Branch_name='%s';" \
                % res[0])
    
    for r in cur.fetchall():
        print("%d\t\t%s" % (int(r[0]),r[1]))
        
    conn.close()
    
    
    
    
    
from databaseConn import *

def checkBalance(cid):
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    cur.execute("select Balance from ACCOUNT where Acc_no='%s';" % cid)
    
    r = cur.fetchone()
    
    return float(r[0])
    

def showBalance(cid):

    amount = checkBalance(cid)
    
    print('Your account has Rs.%.2f' % amount)
    
    if(amount<5000):
        print("Your account doesn't have the minimal balance.......Please make sure you keep it!!!")
        
def depositID():
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    cur.execute("select Max(Dep_id) from DEPOSIT;")
    
    r = cur.fetchone()
    
    return int(r[0])

def withdrawalID():
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    cur.execute("select Max(With_id) from WITHDRAWAL;")
    
    r = cur.fetchone()
    
    return int(r[0])    

def transferID():
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    cur.execute("select Max(Trans_id) from TRANSFER;")
    
    r = cur.fetchone()
    
    return int(r[0])

def depositStatement(cid,start_date,end_date):
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    cur.execute("select * from DEPOSIT where Acc_no='%s' and Date between '%s' and '%s' order by Date DESC;" % (cid,start_date,end_date))
    
    if(countStatements(1,cid,start_date,end_date)==0):
        print('No Deposits')
    else:
        for r in cur.fetchall():
            print("Deposited Rs.%.2f on %s. Reference No. = D%05d" % (float(r[2]),r[3],int(r[0])))
        
    conn.close()
              
def withdrawalStatement(cid,start_date,end_date):
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    cur.execute("select * from WITHDRAWAL where Acc_no='%s' and Date between '%s' and '%s' order by Date DESC;" % (cid,start_date,end_date))
    
    if(countStatements(2,cid,start_date,end_date)==0):
        print('No Withdrawals')
    else:
        for r in cur.fetchall():
            print("Withdrawn Rs.%.2f on %s. Reference No. = W%05d" % (float(r[2]),r[3],int(r[0])))
            
    conn.close()    
        
def transferFromStatement(cid,start_date,end_date):
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    cur.execute("select * from TRANSFER where From_acc_no='%s' and Date between '%s' and '%s' order by Date DESC;" % (cid,start_date,end_date))
    
    if(countStatements(3,cid,start_date,end_date)==0):
        print('No Money Transfers to other accounts')
    else:
        for r in cur.fetchall():
            print("Transfered Rs.%.2f to Account No. %s on %s. Reference no. = T%05d" % (float(r[3]),r[2],r[4],int(r[0])))
        
    conn.close()        
    
def transferToStatement(cid,start_date,end_date):
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    cur.execute("select * from TRANSFER where To_acc_no='%s' and Date between '%s' and '%s' order by Date DESC;" % (cid,start_date,end_date))
    
    if(countStatements(4,cid,start_date,end_date)==0):
        print('No Money Transfers from other accounts')
    else:
        for r in cur.fetchall():
            print("Received Rs.%.2f from Account No. %s on %s. Reference no. = T%05d" % (float(r[3]),r[1],r[4],int(r[0])))
        
    conn.close()        

def countStatements(num,cid,start_date,end_date):
    
    conn = connectToMySQL()
    cur = conn.cursor()
    
    if(num==1):
        cur.execute("select count(*) from DEPOSIT where Acc_no='%s' and Date between '%s' and '%s' order by Date DESC;" % (cid,start_date,end_date))
    elif(num==2):
        cur.execute("select count(*) from WITHDRAWAL where Acc_no='%s' and Date between '%s' and '%s' order by Date DESC;" % (cid,start_date,end_date))
    elif(num==3):
        cur.execute("select count(*) from TRANSFER where From_acc_no='%s' and Date between '%s' and '%s' order by Date DESC;" % (cid,start_date,end_date))
    elif(num==4):
        cur.execute("select count(*) from TRANSFER where To_acc_no='%s' and Date between '%s' and '%s' order by Date DESC;" % (cid,start_date,end_date))
        
    r = cur.fetchone()
    
    return int(r[0])
        
        
        
        
        
    
    
    
    
    
    
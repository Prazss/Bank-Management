import MySQLdb

def connectToMySQL():
    conn = MySQLdb.connect(host="localhost",   
                           user="root",        
                           passwd="prazss21",  
                           db="BANK")        

    
    return conn
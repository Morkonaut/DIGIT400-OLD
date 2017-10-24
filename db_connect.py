import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                          user = "root",
                          passwd = "password", #put your password here
                          db = "demo")
    c = conn.cursor()
    
    return c, conn
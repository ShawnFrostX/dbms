import mysql.connector
    
try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='balesolie'
    )
    print('CONNECTED TO DATABASE\n')
except:
    print('error')

cursor = con.cursor()

def db_selector():
    cursor.execute('use oar')
    con.commit()

def querytaker(query):
    cursor.execute(query)
    con.commit()

def querysender(query):
    cursor.execute(query)
    res = cursor.fetchall()
    return res


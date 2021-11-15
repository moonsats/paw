import pymysql
from dotenv import load_dotenv
import os

def dbcon(db_name="sats"): 
    load_dotenv()
    user_id = os.environ.get("USER_ID")
    user_pw = os.environ.get("USER_PW")
    mysql_id = os.environ.get("MYSQL_ID")
    mysql_pw = os.environ.get("MYSQL_PW")

    return pymysql.connect(
        host=f'{user_id}.mysql.pythonanywhere-services.com', 
        user=mysql_id, 
        password=mysql_pw, 
        db=f'{user_id}${db_name}', 
        charset='utf8'
    )

def create_table(db_name="sats"): 
    try: 
        db = dbcon(db_name=db_name) 
        c = db.cursor() 
        c.execute("CREATE TABLE student (num varchar(50), name varchar(50))") 
        db.commit() 
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close() 
        
def insert_data(num, name): 
    try: 
        db = dbcon() 
        c = db.cursor() 
        setdata = (num, name) 
        c.execute("INSERT INTO student VALUES (%s, %s)", setdata) 
        db.commit() 
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close() 

def select_all(): 
    ret = list() 
    try: 
        db = dbcon() 
        c = db.cursor() 
        c.execute('SELECT * FROM student') 
        ret = c.fetchall() # for row in c.execute('SELECT * FROM student'): # ret.append(row) 
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close() 
    
    return ret 

def select_num(num): 
    ret = () 
    try: 
        db = dbcon() 
        c = db.cursor() 
        setdata = (num,) 
        c.execute('SELECT * FROM student WHERE num = %s', setdata) 
        ret = c.fetchone() 
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close() 
    return ret


create_table() 
insert_data('20201234', '파이썬') 
ret = select_all() 
print(ret)

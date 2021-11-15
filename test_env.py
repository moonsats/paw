from dotenv import load_dotenv
import os

load_dotenv()

user_id = os.environ.get("USER_ID")
user_pw = os.environ.get("USER_PW")
mysql_id = os.environ.get("MYSQL_ID")
mysql_pw = os.environ.get("MYSQL_PW")

print(user_id, user_pw, mysql_id, mysql_pw)
import psycopg2
from pprint import pprint

conn = psycopg2.connect(
   database="lesson",
   user='postgres', 
   password='aeb1205sql', 
   host='localhost', 
   port= '5432'
)
cursor = conn.cursor()

cursor.execute("""SELECT * FROM users ORDER BY id""")
# users_list = cursor.fetchall()
# pprint(cursor.fetchall())

def user(users):
    for i in users:
        # print(i)
        for key, value in i.items():
            print(f"{key}: {value}")
        print('')

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    k =  [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]
    # pprint(k)
    user_info = user(users=k)
    return user_info
dictfetchall(cursor)

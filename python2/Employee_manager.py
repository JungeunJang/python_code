import os
import cx_Oracle
import time

DB_ID = "scott"
DB_PWD = "1234"
DB_URL = "localhost/work3"

def get_conn():
    os.putenv("NLS_LANG", "UTF8")
    conn = cx_Oracle.connect(DB_ID, DB_PWD, DB_URL)
    return conn

def get_all_rows(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM EMPLOYEE")
    for row in cursor:
        print(row)
    cursor.close()

def get_rows_key(conn, id):
    cursor = conn.cursor()
    str_sql= "SELECT * FROM EMPLOYEE WHERE ID =:id "
    cursor.execute(str_sql, {'id': id})
    row = cursor.fetchall()
    print(row)
    cursor.close()

def insert_row(conn, id, name, email):
    cursor = conn.cursor()
    str_sql= "INSERT INTO EMPLOYEE VALUES(:id, :name, :email)"
    cursor.execute(str_sql, {'id': id, 'name': name, 'email': email})
    conn.commit()
    cursor.close()

def update_row(conn, id, name, email):
    cursor = conn.cursor()
    str_sql= "UPDATA EMPLOYEE SET name =:name, email =:email WHERE id=:id"
    cursor.execute(str_sql, {'id': id, 'name': name, 'email': email})
    conn.commit()
    cursor.close()

def dalete_row(conn, id):
    cursor = conn.cursor()
    str_sql= "DELECT FROM EMPLOYEE WHERE id =: id"
    cursor.execute(str_sql, {'id': id})
    conn.commit()
    cursor.close()

while True:
    print("############EMPLOYEEE###########")
    print("# 1. 전체")
    print("# 2. 검색")
    print("# 3. 추가")
    print("# 4. 수정")
    print("# 5. 삭제")
    print("# 6.종료")
    print("################################")
    num = input("번호를 입력해주세요. [1~6]")

    if num == '1':
        conn =  get_conn()
        get_all_rows(conn)
        conn.close()
    elif num == '2':
        id = int(input("사원번호를 입력해주세요."))
        conn =  get_conn()
        get_rows_key(conn, id)
        conn.close()
    elif num == '3':
        id = int(input("사원번호를 입력해주세요."))
        name = input("이름을 입력해주세요")
        email = input("이메일을 입력해주세요.")
        conn =  get_conn()
        insert_row(conn, id, name, email)
        conn.close()
    elif num == '4':
        id = int(input("사원번호를 입력해주세요."))
        name = input("이름을 입력해주세요")
        email = input("이메일을 입력해주세요.")
        conn =  get_conn()
        update_row(conn, id, name, email)
        conn.close()
    elif num == '5':
        pass 
    elif num == '6':
        pass 
    else:
        os.system("cls")


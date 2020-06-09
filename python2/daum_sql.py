import os
import cx_Oracle
import time
import requests
from bs4 import BeautifulSoup

DB_ID = "scott"
DB_PWD = "1234"
DB_URL = "localhost/work3"

def get_conn():
    os.putenv("NLS_LANG", ".UTF8")
    conn = cx_Oracle.connect(DB_ID, DB_PWD, DB_URL)
#   print(conn.version)
    return conn

# def get_all_rows(conn):
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM MOVIES_RANKS")
#     for row in cursor:
#         print(row)
#     cursor.close()

def insert_row(conn, no, title, link):
    cursor = conn.cursor()
    str_sql = "INSERT INTO MOVIES_RANKS VALUES(:no, :title, :link)"
    cursor.execute(str_sql, {'no':no,'title':title, 'link':link})
    conn.commit()
    cursor.close()
    
#다음 무비에서 영화 순위 끌어오기
URL = "http://ticket2.movie.daum.net/Movie/MovieRankList.aspx"


res = requests.get(URL)
soup = BeautifulSoup(res.content, 'lxml')
rankings = soup.find_all('strong', class_="tit_join")

def get_row_count(conn):
    cursor = conn.cursor
    str_sql = "select nvl(max(no),1) from movies_ranks"
    cursor.execute(str_sql)
    row = cursor.fetchone()
#    print(row)
    cursor.close()
    return row[0]

conn = get_conn()
no = get_row_count(conn)
if no == 1:
    pass 
else:
    no = no + 1
    
for movie in rankings:
    m = movie.find('a')
    title = m.get_text().strip()
    link = m['href']
    conn = get_conn()
    insert_row(conn, no, title, link )
    no += 1

conn.close()
print("successed")
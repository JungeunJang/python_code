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

def get_all_rows(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MOVIES_RANKS")
    for row in cursor:
        print(row)
    cursor.close()


def insert_row(conn, title, link):
    cursor = conn.cursor()
    str_sql = "INSERT INTO MOVIES_RANKS(TITLE, LINK) VALUES(:title, :link)"
    cursor.execute(str_sql, {'title':title, 'link':link})
    conn.commit()
    cursor.close()

#다음 무비에서 영화 순위 끌어오기
URL = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"

res = requests.get(URL)
soup = BeautifulSoup(res.content, 'lxml')
rankings = soup.find_all('table', class_="list_ranking")
movies = rankings[0].find_all('div', class_="tit3")

#count = 1
for movie in movies:
#   count += 1
    m = movie.find('a')
    title = m.get_text().strip()
    link = m['href']
    conn = get_conn()
    insert_row(conn, title, link )

print("successed")
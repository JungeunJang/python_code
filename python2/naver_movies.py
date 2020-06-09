import requests
from bs4 import BeautifulSoup

#다음 무비에서 영화 순위 끌어오기
res = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
soup = BeautifulSoup(res.content, 'lxml')

rankings = soup.find_all('table', class_="list_ranking")
#movies = rankings[0].find_all('div', class_="tit3")
#print(movies)

for movie in rankings:
    m = movie.find('a')
    print(m.get_text(), m['href'])
       #print(movie)
#print(len(rankings))



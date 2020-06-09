import requests
from bs4 import BeautifulSoup

#다음 무비에서 영화 순위 끌어오기
res = requests.get("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx")
soup = BeautifulSoup(res.content, 'lxml')
#print(soup)
rankings = soup.find_all('strong', class_="tit_join")
print(rankings)
for movie in rankings:
    m = movie.find('a')
    print(m.get_text().strip(), m['href'])
       #print(movie)
#print(len(rankings))

from bs4 import BeautifulSoup
import requests
nyt = requests.get("https://www.nytimes.com")
nyt_txt = nyt.text
soup = BeautifulSoup(nyt_txt, 'html.parser')
tag = soup.find_all('h3', {"class" : "indicate-hover css-1n70gp3"})
for i in tag:
    print(i.getText())
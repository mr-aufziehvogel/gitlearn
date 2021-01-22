from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

page = "https://www.transfermarkt.de/holstein-kiel/startseite/verein/269"
pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

player_names = pageSoup.find_all("span", class_="hide-for-small")
global player_list
player_list = []


for _ in player_names:
    player_list.append(_.a.get_text(separator="\n"))

print(', '.join(player_list))
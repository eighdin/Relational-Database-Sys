import bs4
import requests

url = "https://hurstathletics.com/sports/mens-ice-hockey/roster"
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

players = soup.find('ul', attrs={'class':"sidearm-roster-players"})
player_list = players.find_all('li', attrs={"class":"sidearm-roster-player"}) # type: ignore

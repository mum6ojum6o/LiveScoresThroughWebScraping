#Beautiful Soup Intro

import urllib.request as urllib2
from bs4 import BeautifulSoup


def extractMatchDetails(htmlstring):
	#print(htmlstring)
	score=""
	home = htmlstring.find('div',attrs={'class':'football-match__team--home'}).find('div',attrs={'class':'football-team__name'}).find('span')
	#print(home.text.strip())
	score=score+home.text.strip()
	home_score = htmlstring.find('div',attrs={'class':'football-match__team--home'}).find('div',attrs={'class':'football-team__score'})
	score=score+" "+home_score.text.strip()
	away = htmlstring.find('div',attrs={'class':'football-match__team--away'}).find('div',attrs={'class':'football-team__name'}).find('span')
	
	away_score = htmlstring.find('div',attrs={'class':'football-match__team--away'}).find('div',attrs={'class':'football-team__score'})
	score=score+" "+away_score.text.strip()+" "+away.text.strip()
	print(score)

guardian_live = 'https://www.theguardian.com/football/live'
page = urllib2.urlopen(guardian_live)
#print(type(page))
soup = BeautifulSoup(page, 'html.parser')
#print(type(soup))
#list_live_matches = soup.find_all("tr")
list_live_matches = soup.find_all('div', attrs={'class':'football-table__container'})
#print( type(list_live_matches))
current_live_games=[]
i=0
print("Courtesy \'The Guardian\'")
print("-----------------------------------------------")
#extractMatchDetails(list_live_matches[2])
#while i<len(list_live_matches):
#	#print(list_live_matches[i])
#	extractMatchDetails(list_live_matches[i])
#	print("-----------------------------------------------")
#	i+=1
while i<len(list_live_matches):
	competitionType = list_live_matches[i].find('caption').text.strip()
	print("************************************************************")
	print(competitionType)
	print("************************************************************")
	current_live_games = list_live_matches[i].find_all("tr")
	j=1
	while j<len(current_live_games):
		extractMatchDetails(current_live_games[j])
		print("-----------------------------------------------")
		j+=1
	#print(list_live_matches[i])
	print()

	i+=1



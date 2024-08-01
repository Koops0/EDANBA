from bs4 import BeautifulSoup
import requests, csv

#Part 1: Scrape player names and salaries
#url = requests.get('https://hoopshype.com/salaries/players/2023-2024/')
#soup = BeautifulSoup(url.text, 'html.parser')
#players = soup.find_all('td', class_='name')
#players.pop(0)
#
#file = open('nba_players_salaries.csv', 'w', newline='')
#writer = csv.writer(file)
#writer.writerow(['Player', 'Salary'])
#
#for player in players:
#    name = player.text
#    salary = player.find_next('td').text
#
#    #clean up names and salaries, additional spacing, salaries from "$47,607,350" to 47607350
#    name = name.strip()
#
#    salary = salary.strip()
#    salary = salary.replace('$', '')
#    salary = salary.replace(',', '')
#    salary = int(salary)
#
#    writer.writerow([name, salary])
#
#
##Part 2: Scrape everything else
#url = requests.get('https://www.basketball-reference.com/leagues/NBA_2024_advanced.html')
#soup = BeautifulSoup(url.text, 'html.parser')
#
##Go through csv, match player to stats
#
## Get all rows for players
#rows = soup.find_all('tr', class_='full_table')
#
## Write to csv
#with open('nba_stats.csv', 'w', newline='', encoding='utf-8') as file:
#    writer = csv.writer(file)
#
#    # Write headers
#    headers = ['Player', 'Position', 'Age', 'Team', 'Games', 'Minutes Played', 'PER', 'TS%', '3PAr', 'FTr', 'ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS', 'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP']
#    writer.writerow(headers)
#
#    # Write player stats
#    for row in rows:
#        cols = row.find_all('td')
#        player_stats = [col.text.strip() for col in cols]
#        writer.writerow(player_stats)

#Part 3: Link Both CSVs after tweaking both CSVs
# Read both csv files
players = []
with open('nba_players_salaries.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        players.append(row)

stats = []
with open('nba_stats.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        stats.append(row)

# Match player names and salaries with stats
for i in range(1, len(players)):
    for j in range(1, len(stats)):
        if players[i][0] == stats[j][0]:
            players[i].extend(stats[j][1:])

# Write to new csv
with open('nba_salaries.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for player in players:
        writer.writerow(player)

# Close file
file.close()

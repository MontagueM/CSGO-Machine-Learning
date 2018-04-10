from requests import get
from bs4 import BeautifulSoup

print("This program is designed to pull the stats of players from HLTV. In order for this program to work please ensure"
      " all lines except from the first 2 are clear as these lines are for the player names.")
to_continue = input("\nIs this done y/n: ").lower()
if to_continue != "y":
    quit()
number_of_points = int(input("\nHow many data points for each person: "))
# Url for HLTV player list
url = "https://www.hltv.org/stats/players"

# Getting the raw html
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
# print(html_soup)
# Finding the specific cell row
containers = html_soup.find_all('td', class_='playerCol')

# Adding all the player names in HLTV to a big array
player_list = []
container_list = []
for i in range(len(containers)):
    player_list.append(containers[i].text.lower())
    container_list.append(containers[i])

f = open("data.txt", 'r')
file = f.readlines()
player0_name = file[0].lower().strip()
player1_name = file[1].lower().strip()

# Player0
q = open("data.txt", 'a')
if player0_name in player_list:
    # Finding index of player in the array
    index = player_list.index(player0_name)

    # Creating the URLs for the web scraper
    player0_url = "https://hltv.org" + container_list[index].a['href']
    player0_url_matches = player0_url[:31] + "matches" + player0_url[30:]

    player0_response = get(player0_url_matches)
    html_soup_0 = BeautifulSoup(player0_response.text, 'html.parser')

    containers_0 = html_soup_0.find_all('td', class_='statsCenterText')
    if len(containers_0) > number_of_points:
        limit = number_of_points
    else:
        limit = len(containers_0)

    for i in range(limit):
        # Splitting the KD array into kills and deaths
        kd_array = containers_0[i].text.split(" - ")
        if i == 0:  # This is needed as the first line needs to be on a new line
            kd = "\n" + kd_array[0] + " " + kd_array[1] + " 0\n"
        else:
            kd = kd_array[0] + " " + kd_array[1] + " 0\n"
        print(kd)
        q.write(kd)
else:
    print("The first player name cannot be found. Please check the name and retry.")
    quit()
# Player1
if player1_name in player_list:
    index = player_list.index(player1_name)

    player1_url = "https://hltv.org" + container_list[index].a['href']
    player1_url_matches = player1_url[:31] + "matches" + player1_url[30:]

    player1_response = get(player1_url_matches)
    html_soup_1 = BeautifulSoup(player1_response.text, 'html.parser')

    containers_1 = html_soup_1.find_all('td', class_='statsCenterText')
    if len(containers_1) > number_of_points:
        limit = number_of_points
    else:
        limit = len(containers_1)

    for i in range(limit):
        kd_array = containers_1[i].text.split(" - ")
        if i == limit-1:
            kd = kd_array[0] + " " + kd_array[1] + " 1"
        else:
            kd = kd_array[0] + " " + kd_array[1] + " 1\n"
        print(kd)
        q.write(kd)
else:
    print("The first player name cannot be found. Please check the name and retry.")
    quit()

print("\nDone.")
q.close()
f.close()

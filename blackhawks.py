# Mobin Anandwala
# Date created: 2/14/2020
# Purpose: To pull statistics about the current blackhawks season and store it in a csv file using the NHL API
# Idea taken from the NHL Raspberry Pi scoreboard found on  howchoo and this github:  NHL-LED-SCOREBOARD
# API Documentation found here: https://gitlab.com/dword4/nhlapi from google search nhl api

import csv
import requests
base_url = 'http://statsapi.web.nhl.com/api/v1'

# Get the teams from the API
team_url = base_url + '/teams'
response = requests.get(team_url)
results = response.json()
teams = results['teams']
# print(teams)

# Search for the blackhawks in the teams dictionary and save it to a dictionary called blackhawks
for i in range(len(teams)):
    if teams[i]['name'] == 'Chicago Blackhawks':
        blackhawks = teams[i]

# print(blackhawks)
team_id = blackhawks['id']

# Get stats for this season (2019-2020)
blackhawks_url = base_url + '/teams/' + str(team_id) + '/stats'
hawks_stats = requests.get(blackhawks_url)
hawks_response = hawks_stats.json()
# print(hawks_response)
# print(type(hawks_response))
 
hawks_stats = hawks_response['stats'] # this is a of dictionaries
# print(hawks_stats)
# print(type(hawks_stats))
# print(hawks_stats[0]) # 1st entry is what we need under the type statsSingleSeason
# print(type(hawks_stats[0]))

hawks1920stats = hawks_stats[0]['splits']
print(hawks1920stats)

file = open('blackhawks.csv','w')
team_stats = csv.writer(file)
team_stats.writerow(hawks1920stats)
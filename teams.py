#Output the possible team pairing home and away for Skyefift footbal league having 4 teams
# A team cant play against itself
teams=['Dragons','Wolves','Pandas','Unicorns']
for home_team in teams:
	for away_team in teams:
		if home_team!=away_team:
			print(home_team + "VS" + away_team)


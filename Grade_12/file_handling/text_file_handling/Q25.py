with open('Team1.txt', 'r') as team1, open('Team2.txt', 'r') as team2, open('FinalTeam.txt', 'w') as final:
    team1_names = team1.readlines()
    team2_names = team2.readlines()

    for t1, t2 in zip(team1_names, team2_names):
        final.write(t1.strip() + '\n')
        final.write(t2.strip() + '\n')

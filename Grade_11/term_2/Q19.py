team_records = {}  # Dictionary to store team records

while True:
    team_name = input("Enter a team name (or 'exit' to stop): ")
    
    if team_name.lower() == 'exit':
        break

    try:
        wins = int(input(f"Enter the number of wins for {team_name}: "))
        losses = int(input(f"Enter the number of losses for {team_name}: "))

        team_records[team_name] = [wins, losses]
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# a. Print the winning percentage for a given team
selected_team = input("Enter a team name to check its winning percentage: ")
if selected_team in team_records:
    wins, losses = team_records[selected_team]
    winning_percentage = (wins / (wins + losses)) * 100 if wins + losses != 0 else 0
    print(f"{selected_team}'s Winning Percentage: {winning_percentage:.2f}%")
else:
    print(f"Team '{selected_team}' not found.")

# b. Create a list of the number of wins for each team
wins_list = [team_records[team][0] for team in team_records]

# c. Create a list of teams with only winning records
winning_teams = [team for team, record in team_records.items() if record[1] == 0]

# Displaying the results
print("\nList of Wins for Each Team:", wins_list)
print("Teams with Only Winning Records:", winning_teams)

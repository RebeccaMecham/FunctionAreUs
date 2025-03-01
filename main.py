# Initialize dictionary
import random
import sys

dictTeams = {}
master_list_teams = ["placeholder", "BYU", "ASU", "Iowa State", "Colorado", "Baylor", "TCU", "Texas Tech", "Kansas State", "West Virginia", "Kansas", "Cincinnati", "Houston", "Utah", "Arizona", "UCF", "Oklahoma State"]
# Initialize win/loss record

#function that outputs welcome message
def welcomeMessage () :
    name = input ("Enter your name: ")
    print (f"\nHi {name}, welcome to the game!")
    print (f"\nThis game will gather information about a home team and how many games they played. \nThen, it will randomly generate scores for each game and give you the win/loss ratio. ")
    return name

# create menu options for enduser
# returns user select input
def menu(player):
    print(f"\n{player}, choose an option:")
    print("1. Simulate BIG 12 Women's Soccer Conference")
    print("2. Quit")

    choice = input("Enter your choice (1 or 2): ")
    if (choice.isdigit() and 0 < int(choice) < 3):
        return int(choice)
    else:
        print("\nInvalid choice. Please choose from menu options.")
        return menu(player)

# prints list of teams for user to select from
def printTeams():
    count = 1
    for i in range(1, len(master_list_teams)):
        print(f"{i}. {master_list_teams[i]}")

# gets and validates user input for chosen team from printed list
def get_team():
    i = input("\nEnter a team number from the list above: ")
    if (i.isdigit() and 0 < int(i) < 17):
        return int(i)
    else:
        print("\nInvalid choice. Please choose a team number listed above.")
        return get_team()

# returns the corresponding team from the team list that matches the user input
def pickTeam(gameNum = 0, home = True):
    if home:
        print("\nPick the home team from the following list:")
        printTeams()

        hName = master_list_teams.pop(get_team())
        print(f"You picked {hName}.")
        return hName
    else:
        print(f"\nPick the away team for game #{gameNum} from the following list:")
        printTeams()
        aName = master_list_teams.pop(get_team())
        print(f"You picked {aName}.")
        return aName

# generates game scores and outcomes using random class
def scores(inpGames) :
    wins = 0
    losses = 0
    # Simulating games
    for iCount in range(inpGames):
        homeScore = random.randint(0, 7)  # Random score for home team
        awayScore = random.randint(0, 7)  # Random score for away team

    # Confirming that the scores are not the same
        while homeScore == awayScore:
            homeScore = random.randint(0, 7)
            awayScore = random.randint(0, 7)

    # Storing the scores
        sTeamName = list(dictTeams.keys())[iCount]  # Get the current away team name
        dictTeams[sTeamName].append((homeScore, awayScore))  # Store the scores

        # Update win/loss record
        if homeScore > awayScore:
            wins += 1
        else:
            losses += 1
    return [wins, losses]

# prints out scores collected 
def outputScores(homeTeam, inpGames, winloss) :
    wins, losses = winloss
    # print hometeam and results
    print(f"\n{homeTeam}'s conference standing for BIG 12 women's soccer:")
    

    for team, games in dictTeams.items():
        print(f"\tOpponent: {team}")

        for game in games:
            homeScore, awayScore = game
            result = "Win" if homeScore > awayScore else "Loss"
            # print scores and result
            print(f"\t\t{homeTeam} Score: {homeScore}, Opponent Score: {awayScore}, Result: {result}")

    # Displaying final season record
    print(f"Final season record: {wins} - {losses}")

    # Calculate the win percentage

    winPercentage = wins / inpGames * 100

    # Print final message based on the win percentage
    if winPercentage >= 75:
        finalMessage = f"{homeTeam} qualified for the NCAA Women's Soccer Tournament!"
    elif winPercentage >= 50:
        finalMessage = f"{homeTeam} had a good season!"
    else:
        finalMessage = f"{homeTeam} needs to practice!"

    print(f"\n{finalMessage}\n\n----------------\nEnter your name to play again or quit\n")

# main function to run logic between welcomeMessage, menu, pickTeam, scores, and outputScores.
def main() :
    global master_list_teams, dictTeams  # Ensure we modify the global list
    master_list_teams = ["placeholder", "BYU", "ASU", "Iowa State", "Colorado", "Baylor", "TCU", 
                         "Texas Tech", "Kansas State", "West Virginia", "Kansas", "Cincinnati", 
                         "Houston", "Utah", "Arizona", "UCF", "Oklahoma State"]  # Reset list
    dictTeams = {}

    sName = welcomeMessage()
    if menu(sName) == 1:
        # Get user inputs
        homeTeam = pickTeam()
        inpGames = 0
        valid_input = False
        while not valid_input:
            try:
                inpGames = int(input(f"\nEnter the number of games {homeTeam} will play this season: "))
                if inpGames <= 0:
                    print("Please enter a positive number.")
                elif inpGames > 16 :
                    print("You can only play 16 games or less.")
                else:
                    valid_input = True
            except ValueError:
                print("Please enter a valid number.")

        # Collecting away team names
        for iCount in range(inpGames):
            sTeamName = pickTeam(iCount + 1, False)

            # Initialize list
            dictTeams[sTeamName] = []  

        win_loss_ratio = scores(inpGames)

        outputScores(homeTeam, inpGames, win_loss_ratio)
        main()
    else:
        print("Goodbye!\n\n")
        sys.exit()

main()
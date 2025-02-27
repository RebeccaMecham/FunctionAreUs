#Rebecca Mecham, code from class assignment
#Collect a Dictionary of how the Season went for your team
import random

#function to calculate scores, and make sure that there isn't a tie
def scores():
    score1 = random.randrange(0,6)
    score2 = random.randrange(0,6)
    while(score1 == score2):
        score1 = random.randrange(0,6)
    if score1 > score2:
        outcome = "Won"
    else:
        outcome = "Lost"
    return(score1, score2, outcome)

def welcomeMessage () :
    name = input ("Enter your name: ")
    print (f"{name}, welcome to the game!")
    print (f"This game will gather information about a home team and how many games they played. Then it will randomly generate scores for each game and give you the win/loss ratio. ")
    return name

#Creates a dictionary for season outcomes
seasonOutCome = {}

#Gather input for how much data will be collected
homeTeam = input("Enter the name of your team (Home Team): ")
gameCnt = int(input(f"\nEnter the number of games {homeTeam} will play: "))
print("\n")
#See who was played, and calculate a score for each game
games = {}
for game in range(gameCnt):
    opponent = input(f"Enter the name of the opposing team for game {game + 1}: ")
    score = scores()
    games[opponent]=score

#Input team scores into the dictionary
seasonOutCome[homeTeam] = games
wins = 0
totalGames = 0
print("\n")

#Print out how each game went
for team, games in seasonOutCome.items():
    for game,score in games.items(): # Loop through games
        print(f"{team} {score[2]} against {game}, {score[0]}:{score[1]}")
    if score[2] == "Won":
        wins +=1
    totalGames += 1

winPercent = wins/totalGames
print(f"\n{homeTeam}'s Final Season Record: {wins}:{totalGames}\n")
if winPercent > .75:
    print("Qualified for the NCAA Women's Soccer Tournament!")
elif winPercent > .5:
    print("You had a good season.")
else:
    print("Your team needs to practice!\n")
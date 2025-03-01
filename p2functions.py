#Rebecca Mecham, Blake Rogers code from class assignment
#Collect a Dictionary of how the Season went for your team
import random

#function that outputs welcome message
def welcomeMessage () :
    name = input ("Enter your name: ")
    print (f"{name}, welcome to the game!")
    print (f"This game will gather information about a home team and how many games they played. Then it will randomly generate scores for each game and give you the win/loss ratio. ")
    return name

#print out players options, and return which choice they made

def menu(player, home = None):
    print(f"\n{player}, choose an option:")
    print("1. Pick Home Team")
    print("2. Pick Opponent")
    print("3. Print Scores")
    print("4. Quit")

    choice = int(input("Enter your choice: "))
    return choice

def pickTeam(home = None)
    #Have user pick a team from list, if you have already picked home team, exclude from options to pick
    return team_name

def scores():
    #function to calculate scores, and make sure that there isn't a tie
    score1 = random.randrange(0,6)
    score2 = random.randrange(0,6)
    while(score1 == score2):
        score1 = random.randrange(0,6)
    if score1 > score2:
        outcome = "Won"
    else:
        outcome = "Lost"
    return(score1, score2, outcome)

def outputScore(finalScore)
    #Calculate and print out results from the games played.

#Creates a dictionary for season outcomes
seasonOutCome = {}

name = welcomeMessage()
run = TRUE
while run:
    choice = menu(name)
    #Based on what they pick, either pick home team, pick opponent, print out team scores or quit
    if choice = 1 #pickhometeam
        home = pickTeam()
        games = {}
    elif choice = 2 #playgame
        away = pickTeam(home)
        score = scores()
        games[opponent]=score
    elif choice = 3 #printScores
        seasonOutCome[homeTeam] = games
        outputScores(seasonOutCome)
    elif choice = 4 #quit
        run = False
    else:
        print("Invalid choice. Please choose a number between 1 and 4.")



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


#Everything below here is what I would put in the output scores function
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
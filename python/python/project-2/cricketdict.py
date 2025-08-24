players={}
n=int(input("Enter number of players: "))
for i in range(n):
    name=input("Enter player name: ")
    score=int(input("Enter player score: "))
    players[name]=score
print("*****************")
search=input("Enter player name to search: ")
if search in players:
    print("player : ", search)
    print("score : ", players[search])
else:
    print("Player not found")
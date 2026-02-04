"""https://www.codewars.com/kata/582e0e592029ea10530009ce"""

def duck_duck_goose(players, goose):
    player_amount = len(players)
    goose = goose % len(players)
    
    return players[goose - 1].name


    
    
    
        
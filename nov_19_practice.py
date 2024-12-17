def test_rps(player1, player2):
    if player1 == player2:
        return("tie")
    if player1 == "rock" and player2 == "paper":
        return("player2 won")
        
    if player1 == "scissors"  and player2 == "rock":
        return("player2 won")

    if player1 == ("paper") and player2 == ("scissors"):
        return("player2 won")
    else:
        return("player1 won")
        

        
print(test_rps("scissors","paper"))

def rps_but_worse(player1, player2):
    if player1 == player2:
        return("tie")
    if player1 == "rock" or "spock" and player2 == "paper":
        return("player2 won")
        
    if player1 == "scissors" or "lizard"  and player2 == "rock":
        return("player2 won")

    if player1 == "paper" or "lizard" and player2 == ("scissors"):
        return("player2 won")

    if player1 == "rock" or "scissors" and player2 == ("spock"):
        return("player2 won")

    if player1 == "paper" or "spock" and player2 == ("lizard"):
        return("player2 won")

    else:
        return("player1 won")

print(rps_but_worse("spock", "paper"))    


def player_choice(ptype):
    if ptype == "c":
        p_choice = r.choice("rock","paper","scissors")
    else:
        p_choice = input("enter rock, paper, or scissors: ")
    return p_choice
player1 = player_choice("h")
player2 = player_choice("c")

test_rps(player1,player2)
outcome = test_rps(player1,player2)
print(outcome) 

    

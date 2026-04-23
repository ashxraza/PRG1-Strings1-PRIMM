# CHALLENGE 3 ------------------------------------------------------------------
# Write a simple text analyser. Given a string of text, return a dictionary
# with these three keys:
#   "words"            →  total word count
#   "characters"       →  total character count (excluding spaces)
#   "avg_word_length"  →  average word length (rounded to 1 decimal place)
#
# Example:
#   analyse_text("I love Python")
#   →  {"words": 3, "characters": 11, "avg_word_length": 3.7}


player1 = "rock"
player2 = "scissors"

player_1_moves = {
    "rock": ["scissors"]
}

if player1 == player2:
    print("draw")

if player2 in player_1_moves[player1]:
    print("P1 wins")
else:
    print("P2 wins")

    # elif player1 == "scissors" and player2 == "paper" :
    #     return "player1"
    # elif player1 == "paper" and player2 == "rock":
    #     return "player1"
    # elif player1 == "rock" and player2 == "scissors":
    #     return "player1"
    # elif player1 == "rock" and player2 == "lizard" :
    #      return "player1"
    # elif player1 == "scissors" and player2 == "lizard" :
    #      return "player1"
    # elif player1 == "lizard" and player2 == "paper" :
    #      return "player1"
    # elif player1 == "spock" and player2 == "rock" :
    #      return "player1"
    # elif player1 == "spock" and player2 == "scissors" :
    #      return "player1"
    # elif player1 == "lizard" and player2 == "spock" :
    #      return "player1"
    # elif player1 == "paper" and player2 == "spock" :
    #      return "player1"
    # else:
    #      return "player2"
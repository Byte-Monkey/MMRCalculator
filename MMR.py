opponent_rating = int(input("Opponent Rating: "))
player_rating = int(input("Player Rating: "))
score = int(input("Score: "))
opponent_score = int(input("Opponent Score: "))
expected_score = 1/(1+10**((opponent_rating-player_rating)/280))
opponent_expected_score = 1/(1+10**((player_rating-opponent_rating)/280))

output = player_rating + 32 * (score - expected_score)
second_output = player_rating + 32 * (opponent_score - opponent_expected_score)

print("Player new MMR:", output)
print("Opponent new MMR:", second_output)

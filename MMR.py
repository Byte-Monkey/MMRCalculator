def check(score):
    if score > 2000:
        return 2000
    elif score < -15:
        return -15
    else:
        return score


def calculate():
    player_rating = int(input("Player Rating: "))
    opponent_rating = int(input("Opponent Rating: "))
    score = int(input("Player Score: "))
    opponent_score = int(input("Opponent Score: "))

    expected_score = round(1 / (1 + 10 ** ((opponent_rating - player_rating) / 280)), 1)
    opponent_expected_score = round(1 / (1 + 10 ** ((player_rating - opponent_rating) / 280)), 1)

    output = player_rating + (32 * (score - expected_score))
    second_output = opponent_rating + (32 * (opponent_score - opponent_expected_score))

    print("\nPlayer new MMR:", check(output))
    print("Opponent new MMR:", check(second_output))


calculate()

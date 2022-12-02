# 1 for Rock, 2 for Paper, and 3 for Scissors
# The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors

with open("strategy_guide.txt") as f:
    games = f.readlines()
games = [line.strip() for line in games]

win_loss_score = {
    "X": 0,  # need to lose
    "Y": 3,  # need to draw
    "Z": 6,  # need to win
}

moves_to_pick = {
    "A": {          # opponent picks Rock
        0: 3,       # I need to lose, so I pick Scissors
        3: 1,       # I need to draw, so I pick Rock
        6: 2,       # I need to win, so I pick Paper
    },
    "B": {          # opponent picks Paper
        0: 1,       # I need to lose, so I pick Rock
        3: 2,       # I need to draw, so I pick Paper
        6: 3,       # I need to win, so I pick Scissors
    },
    "C": {          # opponent picks Scissors
        0: 2,       # I need to lose, so I pick Paper
        3: 3,       # I need to draw, so I pick Scissors
        6: 1,       # I need to win, so I pick Rock
    }
}

total_points = 0
for game in games:
    outcome_score = win_loss_score[game[-1]]
    total_points += outcome_score
    total_points += moves_to_pick[game[0]][outcome_score]

print(f"Total points I get = {total_points}")


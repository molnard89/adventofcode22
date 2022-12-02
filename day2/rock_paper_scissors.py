with open("strategy_guide.txt") as f:
    games = f.readlines()

score_for_shape = {
    'X': 1,  # rock
    'Y': 2,  # paper
    'Z': 3,  # scissor
}

losses = ['A Z', 'B X', 'C Y']
victories = ['A Y', 'B Z', 'C X']
draws = ['A X', 'B Y', 'C Z']

games = [line.strip() for line in games]

total_points = 0
for game in games:
    total_points += score_for_shape[game[-1]]

    if game in victories:
        total_points += 6
    elif game in draws:
        total_points += 3


print(f"Total points I get = {total_points}")
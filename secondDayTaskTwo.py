file_path = "Data/inputSecond"

#A, rock, 1
#B, Paper, 2
#C, scissor, 3
#X, lose, 0
#Y, draw, 3,
#Z, win, 6

strategy_map = {
    'AX': 3, #rock + lose(scissor)
    'AY': 4, #rock + draw(rock) 
    'AZ': 8, #rock + win(paper)
    'BX': 1, #paper + lose(rock)
    'BY': 5, #paper + draw(paper)
    'BZ': 9, #paper + win(scissor)
    'CX': 2, #scissor + lose(paper)
    'CY': 6, #scissor + draw(scissor)
    'CZ': 7, #scissor + win(rock)
}


def get_score():
    with open(file_path) as f:
        contents = f.readlines()

    sum_score = 0
    for elem in contents:
        #elem[0] gegner, elem[2] eigene strategie
        temp_strategie =  elem[0] + elem[2]
        sum_score += strategy_map[temp_strategie]

    return sum_score

print(get_score())
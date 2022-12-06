file_path = "Data/inputSecond"

#A, X: rock, 1
#B, Y: Paper, 2
#C, Z: scissor, 3
strategy_map = {
    'AX': 4, #rock + rock
    'AY': 8, #rock + paper 
    'AZ': 3, #rock + scissor
    'BX': 1, #paper + rock
    'BY': 5, #paper + paper
    'BZ': 9, #paper + scissor
    'CX': 7, #scissor + rock
    'CY': 2, #scissor + paper
    'CZ': 6, #scissor + scissor
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
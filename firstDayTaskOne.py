
file_path = "Data/input"

def calc_calories():
    temp_max = 0
    max = 0

    with open(file_path) as f:
        contents = f.readlines()

    for elem in contents:
        if elem != '\n':
            value = int(elem.strip('\n'))
            temp_max += value
        else:
            if temp_max >= max:
                max = temp_max
            temp_max = 0

    return max


max_calories = calc_calories()
print(max_calories)
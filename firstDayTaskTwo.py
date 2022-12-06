file_path = "Data/input"

def calc_test_max3():
    temp_max = 0
    max_top = 0
    max_second = 0
    max_third = 0

    with open(file_path) as f:
        contents = f.readlines()
    

    for elem in contents:
        if elem == '\n':
            if temp_max > max_top:
                max_third = max_second
                max_second = max_top
                max_top = temp_max
            if temp_max < max_top and temp_max > max_second:
                max_third = max_second
                max_second = temp_max
            if temp_max < max_second and temp_max > max_third:
                max_third = temp_max
            temp_max = 0
        else:
            value = int(elem.strip('\n'))
            temp_max += value
        
    return max_top + max_second + max_third

    
print(calc_test_max3())

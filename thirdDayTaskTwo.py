file_path = "Data/inputThird"

priorities = ['#', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]


def backpack_check():

    with open(file_path) as f:
        contents = f.readlines()

    prio_sum = 0
    check_str = 0
    temp_cont = [elem.strip() for elem in contents]
    len_contents = len(temp_cont)
    

    while len_contents > 0:
        temp_group = temp_cont[:3]
        
        for char in temp_group[0]:
            if char in temp_group[1] and char in temp_group[2]:
                check_str = priorities.index(char)

        prio_sum += check_str
        temp_cont = temp_cont[3:]
        len_contents -= 3
        
    
    return prio_sum

print(backpack_check())
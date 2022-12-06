file_path = "Data/inputThird"

priorities = ['#', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]


def backpack_check():

    with open(file_path) as f:
        contents = f.readlines()

    prio_sum = 0
    check_str = 0
    for elem in contents:
        split_len = int(len(elem)/2)

        compartmentOne = elem[:split_len]
        compartmentTwo = elem[split_len:]
        
        for char in compartmentOne:
            if char in compartmentTwo:
                check_str = priorities.index(char)
                
        prio_sum += check_str

    return prio_sum

print(backpack_check())
def sort_algorithm(l):
    length = len(l)
    unsorted_elements = length
    num_switches = 0
    sorted_list = l.copy()
    while 0 < unsorted_elements:
        for i in range(0, unsorted_elements - 1):
            
            j = i + 1
            switch = sorted_list[i] > sorted_list[j]
            if(switch):
                copy = sorted_list[i]
                sorted_list[i] = sorted_list[j]
                sorted_list[j] = copy
                num_switches += 1
        unsorted_elements -=1
    return sorted_list
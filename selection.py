def switch(i, j, list):
    copy = list[i]
    list[i] = list[j]
    list[j] = copy
    

def sort_algorithm(l):
   
    length = len(l)
    unsorted_elements = length
    num_switches = 0
    sorted_list = l.copy()
    
    while 0 < unsorted_elements:
        for i in range(0, unsorted_elements - 1):
            
            j = i + 1
            if(sorted_list[i] > sorted_list[j]):
                switch(i, j, sorted_list)
        unsorted_elements -=1
        
    return sorted_list
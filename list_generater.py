import random
import sys




def generate(len, lower_bound = -sys.maxsize, upper_bound = sys.maxsize):
    
    if(lower_bound > upper_bound):
        print("---- ERROR ----")
        print("Lower bound > Upper bound not alllowed")
        print("Lower bound = ", lower_bound, "\nUpper bound = ", upper_bound)
        return
    
    
    list = []
    i = 0
    while i < len:
        num = random.randint(lower_bound, upper_bound)
        list.append(num)
        i += 1
    return list

def generate_lists(n, len= 0, lower_bound = 0, upper_bound = 0):
    
    lists = {}
    sorted_lists = {}
    i = 0
    while i < n:
        if(lower_bound == 0): # If bounds not specified
                lower_bound = random.randint(-sys.maxsize, upper_bound -1) # Generate random bounds
        if(upper_bound == 0):
                upper_bound = random.randint(lower_bound + 1, sys.maxsize)
        if( len == 0): # If length not specified 
            len = random.randint(10, 200) # Generate random length
            
        list = generate(len,lower_bound, upper_bound)
        sorted_list = sorted(list)
        sorted_lists[i] = sorted_list
        lists[i] = list
        i += 1
    return lists, sorted_lists
    

    
    
    
    

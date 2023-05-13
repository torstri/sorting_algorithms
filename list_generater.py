import random
import sys




def generate_random_list(len, lower_bound = -sys.maxsize, upper_bound = sys.maxsize):
    
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

def generate_random_lists(n, len= 0, lower_bound = 0, upper_bound = 0):
    
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
            
        list = generate_random_list(len,lower_bound, upper_bound)
        sorted_list = sorted(list)
        sorted_lists[i] = sorted_list
        lists[i] = list
        i += 1
    return lists
    
def generate_ascending_list(lower_bound = 0, upper_bound = 0):
    list = []
    for i in range(lower_bound, upper_bound + 1):
        list.append(i)
    return list

def generate_ascending_lists(n):
    lists = {}
    i = 0
    for num in range(0, n):
        lower_bound = random.randrange(-10, -1)
        upper_bound = random.randrange(0, 10)
        list = generate_ascending_list(lower_bound, upper_bound)
        lists[num] = list
        i += 1
    return lists
            
def generate_descending_list(lower_bound = 0, upper_bound = 0):
    list = []
    
    i = upper_bound
    while i >= lower_bound:
        list.append(i)
        i -= 1
    return list

def generate_descending_lists(n):
    lists = {}
    for num in range(0, n):
        lower_bound = random.randrange(-10, -1)
        upper_bound = random.randrange(0, 10)
        list = generate_descending_list(lower_bound, upper_bound)
        lists[num] = list
    return lists
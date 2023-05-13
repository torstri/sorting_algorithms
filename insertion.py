
import list_generater

def switch(i, j, list):
    copy = list[i]
    list[i] = list[j]
    list[j] = copy
    

def sort_algorithm(l):
    length = len(l)
    list = l.copy()
    
    i = 0
    sorted_length = 1
    while sorted_length < length:
        # print("####### First #######")
        # print("Original list = ", l)
        # print("Current List = ", list   )
        # print("i =", i)
        
        j = i + 1
        
        # print("List[i] = ", list[i])
        # print("j =", j)
        # print("List[j] =", list[j])
        k = i
        m = j
        while list[k] > list[m]:
            # print("######### Second ###########")
            # print("Switching L[i] =", list[k], "with", list[m], "= List[j]")
            switch(k, m, list)
            # print("Updated list =", list)
            if k > 0:
                m = k
                k -= 1
            
        
        sorted_length += 1
        # print("Sorted length =", sorted_length)
        i += 1   
            
            
    return list

# l = list_generater.generate_random_list(5, 1, 12)
# print("Before call",l)
# li = sorting_algorithm(l)
# print("After call",li)
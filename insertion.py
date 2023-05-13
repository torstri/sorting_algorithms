
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
    
    while i < length - 1:
        j = i + 1
        k = i
        m = j
        
        while list[k] > list[m]:
            switch(k, m, list)
            if k > 0:
                m = k
                k -= 1
        
        sorted_length += 1
        i += 1
    return list
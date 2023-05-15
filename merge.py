import list_generater

def merge(list1, list2):
    sorted_list =[]
    for elem in list1:
        for elem2 in list2:
            if elem2 < elem:
                sorted_list.append(elem2)
            else:
                sorted_list.append(elem)
                break
    return sorted_list
        

def divide(i: int,j: int, l):
    mid = int((i + j) /2)
    if i >=j :
        print("Base case l =", l[i])
        return l
    
    return merge(divide(i,mid, l), divide(mid + 1, j,l))
    
    
def merge_sort(list, left, right):
    if right > left:
        mid = (right + left - 1)/2
        merge_sort(list, left, mid)
        merge_sort(list, mid + 1, right)
        merge(list, left, mid, right)
        

def sorting_algorithm(list):
    length = len(list)
    if length > 1:
        
        mid = length//2
        Left = list[:mid]
        Right = list[mid:]
        
        sorting_algorithm(Left)
        sorting_algorithm(Right)
        
        l = r = k = 0
        while l < len(Left) and r < len(Right):
            if Left[l] <= Right[r]:
                list[k] = Left[l]
                l += 1
            else:
                list[k] = Right[r]
                r += 1
            k += 1
            
        while l < len(Left):
                list[k] = Left[l]
                l += 1
                k += 1
    
        while r < len(Right):
                list[k] = Right[r]
                r += 1
                k += 1
    print("Sorted list =", list)

    
    
    
l = list_generater.generate_ascending_list(1,5)
print("Original list = ", l)
sorting_algorithm(l)
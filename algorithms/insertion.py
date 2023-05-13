
def switch(i, j, list):
    copy = list[i]
    list[i] = list[j]
    list[j] = copy
    

def sorting_algorithm(l):
    length = len(l)
    list = l.copy()
    for i in range(length):
        print("####### First #######")
        print("List = ", list   )
        print("i =", i)
        first = list[i]
        print("List[i] = ", first)
        j = i + 1
        print("j =", j)
        second = list[j]
        print("List[j] =", second)
        if first > second:
            print("Switching L[i] =", first, "with", second, "= List[j]")
            switch(i, j, list)
            while i >= 0:
                i -=1
                
            
    return list

l = [5, 6, 7, 2, 1]
print("Before call",l)
li = sorting_algorithm(l)
print("After call",li)
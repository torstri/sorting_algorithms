

import list_generater
from algorithms import selection
import sys

def create_tests():
    lists ={}
    lists["random"] = list_generater.generate_random_lists(1, 100, -sys.maxsize, sys.maxsize)
    lists["descending"] = list_generater.generate_descending_lists(1)
    lists["ascending"] = list_generater.generate_ascending_lists(2)
    
    for key in lists["ascending"]:
        l = lists["ascending"].get(key)
        sorted_list = sorted(l)
        assert selection.sort_algorithm(l) == sorted_list, "Ascending"
        
    for key in lists["descending"]:
        l = lists["descending"].get(key)
        sorted_list = sorted(l)
        assert selection.sort_algorithm(l) == sorted_list, "Descending"
        
    for key in lists["random"]:
        l = lists["random"].get(key)
        sorted_list = sorted(l)
        assert selection.sort_algorithm(l) == sorted_list, "Random failed"
    
    
    print("Everything passed")

create_tests()
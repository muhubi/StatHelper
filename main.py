import numpy

class StatHelper:
    test_file = open("input_data.txt")
    
    data_test_file = test_file.read()
    
    data_test_list = data_test_file.split("\n")
    test_file.close()
    
    data_test_list.sort()
    print(data_test_list)
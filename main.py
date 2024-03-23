import numpy

class StatHelper:
    test_file = open("test_input_data.txt")
    
    data_test_file = test_file.read()
    
    data_test_list = data_test_file.split("\n")
    print(data_test_list)
    test_file.close()
    
import numpy

class StatHelper:
    #opens the file
    input_file = open("input_data.txt")
    #reads the file
    data_input_file = input_file.read()
    #makes a list of the data from the file
    data_input_list = data_input_file.split("\n")
    #closes the file to save resources
    input_file.close()
    
    #sorts the list
    data_input_list.sort()
    #prints the sorted list
    print(data_input_list)
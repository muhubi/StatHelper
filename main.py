import numpy as np

class stathelper_file_import:
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
    # print(data_input_list)
    
    #converts the sorted list into floats
    data_input_list_float = [float(i) for i in data_input_list]
    #prints the sorted float list
    # print(data_input_list_float)
    
    #uses NumPy to analyze the list
    min_input_list = np.min(data_input_list_float)
    max_input_list = np.max(data_input_list_float)
    median_input_list = np.median(data_input_list_float)
    mean_input_list = np.mean(data_input_list_float)
    stdev_input_list = np.std(data_input_list_float)

    
    #prints the sorted float list
    print("Here is the list in order: " + str(data_input_list_float))
    print()
    
    #prints the analyses
    print("min, max: " + str(min_input_list) + ", " + str(max_input_list))
    print("media: " + str(median_input_list))
    print("mean: " + str(mean_input_list))
    print("std: " + str(stdev_input_list))
    
# Function: read_data
# Purpose: The function should open the file, and read its contents into a list of list of floats, where the outer list corresponds to the lines
#          of the file, and the inner lists correspond to the columns (that is, convert the strings of each line to a list of two numeric values,
#          and append them to an outer list).
# Arguments: filename
# Returns: list
def read_data(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    outer_list_of_floats = []
    for i in range(len(lines)):
        list_of_two_numeric_values = [float(x) for x in lines[i].split()]
        outer_list_of_floats.append(list_of_two_numeric_values)
    input.close()
    return outer_list_of_floats

# Function: calc_averages 
# Purpose: calculates the average value for each column by iterating over the rows.
# Arguments:  list of list of floats
# Returns: the two values of the two averages

def  calc_averages(list_of_floats):
    col1_average = 0
    col2_average = 0
    n = len(list_of_floats)
    for i in range(n):
        col1_average += list_of_floats[i][0]
        col2_average += list_of_floats[i][1]
    col1_average /= n
    col2_average /= n
    return col1_average, col2_average   


# Function: transpose_data 
# Purpose: turns the list of lists around so that it becomes a list of columns, rather than a list of rows.
# Arguments:  list of lists
# Returns: list of lists

def transpose_data(list_of_lists):
    first_col = []
    second_col = []
    outer_list = []
    for i in range(len(list_of_lists)):
        first_col.append(list_of_lists[i][0])
        second_col.append(list_of_lists[i][1])
    outer_list.append(first_col)
    outer_list.append(second_col)
    return outer_list


list_of_rows = read_data('experimental_results.txt')     

averages = calc_averages(list_of_rows)

list_of_columns = transpose_data(list_of_rows)
print(list_of_columns)
print(len(list_of_columns))
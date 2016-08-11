#
#   @author      : SRvSaha
#   Filename     : find_numbers.py
#   Timestamp    : 19:17 10-August-2016 (Wednesday)
#   Description  : write a function named find_numbers, which will take a list of int, and str, and float
#
def find_numbers(my_list):
    output_list = []
    for item in my_list:
        if type(item) == int:
            output_list.append(item)
    return output_list
# For testing
a = [1,2,3.4,5.6,'Saurav',"Kushal",9]
print(find_numbers(a))

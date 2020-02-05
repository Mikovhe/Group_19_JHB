from group_19_support_func import *

def function_1(data):
    sorted_list = my_sort(data)

    #mean = my_mean(data)
    median = my_median(data)
    maximum = sorted_list[-1]
    minimum = sorted_list[0]
    #std_dev = my_std(data)
    #variance  = std_dev**0.5

    result_dict = {"mean":'missing','median':median,'maximum':maximum,'minimum':minimum,'standard deviation':'missing','variance':'missing'}

    return result_dict

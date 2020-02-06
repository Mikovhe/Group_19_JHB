from group_19_support_func import *

def function_1(data):
    sorted_list = my_sort(data)

    mean = my_mean(data)
    median = my_median(data)
    maximum = sorted_list[-1]
    minimum = sorted_list[0]
    variance  = my_var(data)
    std_dev = variance**0.5

    result_dict = {"mean":round(mean,2),'median':round(median,2),
                    'maximum':round(maximum,2),'minimum':round(minimum,2),
                    'standard deviation':round(std_dev,2),'variance':round(variance,2)}

    return result_dict

def my_sort(data):
    '''
        Sorts items in a list by comparing consecutive numbers,
        if number at index i is smaller than number at i-1,
        the function switches those numbers.

    '''

    sorting = True
    while sorting:
        data_copy = tuple(data)
        for i in range(1,len(data)):
            j = i-1

            if data[i]<data[j]:
                data = switch(data,i,j)

        if data_copy == tuple(data):
            sorting =False

    return(data)


def my_sum(numlist):
  total=0
  for num in numlist:
    total+=num
  return total


def my_len(data):
    count = 0
    for item in data:
        count += 1
    return count

def my_median(num_list):
    s_list = my_sort(num_list)
    if my_len(s_list)%2 == 1:
        ind = int(my_len(s_list)/2)
        return s_list[ind]

    else:
        ind = int(my_len(s_list)/2)
        return (s_list[ind]+s_list[ind-1])/2


def switch(data,ind1,ind2):
    '''
        takes in a list and indices and switch places
        of values at those indices

    '''    
    #store the values to memory
    value_ind1 = data[ind1]
    value_ind2 = data[ind2]

    #assign values to new position
    data[ind1] = value_ind2
    data[ind2] = value_ind1

    return data


def my_mean(my_list):
    '''
    the function takes in a list of numeric values
    then returns the mean of the  list.
    '''
    return(my_sum(my_list)/my_len(my_list))


def my_var(nums):
    '''
    This function calculates the variance of the values in the list: nums
    Remember to replace the sum and len functions with our own functions
    '''
    mean=my_mean(nums)
    varnums=[(num-mean)**2 for num in nums]
    varvalue=my_sum(varnums)/(my_len(nums)-1)
    return varvalue

    
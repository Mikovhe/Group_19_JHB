def my_sort_func(data):
    sorted_list = []
    
    while len(data)>0:
        num = data[0]    
        for num2 in data:
            if num2 < num:
                num = num2

        sorted_list.append(num)
        data.remove(num)
   
    return sorted_list

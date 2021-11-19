def find_outlier(integers):
    even = [i for i in integers if i % 2 == 0]
    odd = [i for i in integers if i % 2 != 0]
    if len(even) == 1: return even[0]
    else: return odd[0]
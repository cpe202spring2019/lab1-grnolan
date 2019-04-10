
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list == None or len(int_list) == 0:
        raise ValueError
    else:
        max_num = int_list[0]
        for num in int_list:
            if num > max_num:
                max_num = num
        return max_num


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError
    if int_list == []:
        return []
    if len(int_list) == 1:
        return int_list
    elif len(int_list) > 1:
        return int_list[-1:] + reverse_rec(int_list[:-1])
 

def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list == None:
        raise ValueError
    else:
        if not low < high:
            return None
        mid = (low + high) // 2
        if target == int_list[mid]:
            return mid
        if target > int_list[mid]:
            return bin_search(target, mid + 1, high, int_list)
        if target < int_list[mid]:
            return bin_search(target, low, mid - 1, int_list)
  

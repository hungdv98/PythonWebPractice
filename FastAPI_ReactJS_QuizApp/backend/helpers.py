def check_not_passed(list1, list2):
    """
        returns True if list1 different from list2
    """
    return any(x !=y for x,y in zip(list1, list2))

def get_numb_diff_pair(list1, list2):
    """
        returns number of wrong answers
    """
    return len([(x, y) for x, y in zip(list1, list2) if x != y])

def get_time_format():
    import time 
    return time.strftime("%Y%m%d-%H:%M:%S")
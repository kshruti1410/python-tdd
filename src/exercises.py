def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    """
    return input_list[::-1]

def count_digits(number):
    """
    Return count of digits
    """
    count = 0
    for i in str(number):
        if i.isdigit():
            count+=1
        else:
            continue
    return count

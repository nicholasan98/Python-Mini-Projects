import random
import time

# This will prove that binary search is faster than naive search

# naive search: loops through the entire list and checks if the target is equal to the value
# if yes, return index
# if no, then return -1

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# binary search uses divide and conquer
# we will leverage the fact taht our list is SORTED
def binary_search(l, target, low = None, high = None):
    # example l = [1, 3, 5, 10, 12] should return 3
    
    # these two are both ifs as we want to check BOTH statement, an elif would check one or the other
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2  # 2

    # the logic behind these if else statements is basically;
    # take the halfway point, if halfway is the target, return target
    # if the value is higher or lower, recurse into the half that is higher/lower
    # then keep sorting by half the list
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)
    
if __name__ == '__main__':
    # l = [1, 3, 5, 10, 12]
    # target = 10
    # print(naive_search(l, target))
    # print(binary_search(l, target))


    # This next part in main essentially made it's own list of sorted values and checked
    length = 10000
    # build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print('Naive search time: ', (end - start)/length, ' seconds')

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print('Binary search time: ', (end - start)/length, ' seconds')
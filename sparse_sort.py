# %% 


def sparse_sort(arr):
    '''
    Orders the value > 0 in `arr` while keeping 
    the zeros in the same index

    Input:
        - `arr` (list) : a list of values 

    Complexity:
        - Temporal : O(n^2)
        - Spatial : O(n)
    '''

    for i in range(len(arr)):
        # If the number in the array is 0 we go to the next
        # index
        if arr[i] == 0:
            i += 1
            continue
        for j in range(i, len(arr)):
            tmp = 0
            # We skip the case in which j is equal to i
            # since it is an useless comparison between the
            # same element
            if j == i:
                continue
            # If the number in j is greater than the one in i
            # I swap them
            if arr[j] > arr[i]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
    
    return arr

numbers = [0.9, 0, 0, 0, 0.1, 0, 0, 0.7, 0, 0, 0.4]
ordinary = [i for i in range(1,10)]

print(sparse_sort(numbers))
print(sparse_sort(ordinary))
# %%

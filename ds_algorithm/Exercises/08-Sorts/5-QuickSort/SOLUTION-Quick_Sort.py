def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)  
        quick_sort_helper(my_list, pivot_index+1, right)       
    return my_list
    

def quick_sort(my_list):
    quick_sort_helper(my_list, 0, len(my_list)-1)


# New method
def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i
 


my_list = [4,6,1,7,3,2,5]

#quick_sort(my_list)
quicksort(my_list, 0, len(my_list)-1)
print(my_list)



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7]
 """
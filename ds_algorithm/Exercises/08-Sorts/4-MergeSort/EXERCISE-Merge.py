
## WRITE MERGE FUNCTION HERE ##
#                             #
#                             #
#                             #
#                             #
############################### 
def merge(array1, array2):
    sorted_array = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            sorted_array.append(array1[i])
            i += 1
        else:
            sorted_array.append(array2[j])
            j += 1

    # Append any remaining elements from either array
    sorted_array.extend(array1[i:])
    sorted_array.extend(array2[j:])
    return sorted_array


# MERGE REQUIRES TWO SORTED LISTS:
print(merge([1,2,7,8], [3,4,5,6]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8]
 """
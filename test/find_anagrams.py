# WRITE GROUP_ANAGRAMS FUNCTION HERE #
#                                    #
#                                    #
#                                    #
#                                    #
######################################
def group_anagrams(words_list):
    #import pdb; pdb.set_trace()
    sorted_strings = []
    if not words_list:
        return []
    for i in words_list:
        if sorted([le for le in i]) not in sorted_strings:
            sorted_strings.append(sorted(list(i)))
    
    word_mapping = {}
    #pdb.set_trace()
    for k in sorted_strings:
        w_list = []
        for j in words_list:
            if sorted([j0 for j0 in j]) == k:
                w_list.append(j)
        word_mapping["".join(k)] = w_list
    
    return word_mapping.values()
    



print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""

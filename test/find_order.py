#!/usr/bin/env python3
import sys

e_list = sys.argv[1]
a_list = sys.argv[2]

print(e_list)
print(a_list)

len_a = len(a_list)
new_index = []
if len(list(set(e_list)-set(a_list))) > 0:
    new_elements = list(set(e_list)-set(a_list))
    print("add new items", new_elements)

new_index = [e_list.index(i) for i in new_elements]
print("New items index: ", new_index)


#min_index = e_list.index(new_elements[0])
#for i in new_elements:
#    if e_list.index(i) > min_index:


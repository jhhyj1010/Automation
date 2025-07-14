#!/usr/bin/env python3
import re
print("This is a program for handling filter in 1Source web")
dict_input = {'filter[organization_id][eq]': '1', 'filter[languages][like]': '%1source%', 'page_size': '25', 'page_number': '1'}

rule =r'\[(\w+)\]'
rc = re.compile(rule)
for k,v in dict_input.items():
    if k.startswith('filter'):
        col, op = rc.findall(re.sub(r'filter', '', k))
        if col == 'languages':
            print(f"column is {col}, operator is {op}, param is {v}")


#!/usr/bin/env/python3
import subprocess
import json
import pdb
pdb.set_trace()
json_file = '/home/huiji/test/param.json'
with open(json_file, 'r', encoding='utf8') as file:
    print(file)
    params = json.load(file)

newIpRange = '10.0.0.0/12'
params['parameters']['ipAddressOrRange'] = newIpRange

with open(json_file, 'w', encoding='utf8') as file:
    json.dump(params, file)
print("jesson")

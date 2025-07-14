#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

base_file = sys.argv[1]
output_file = sys.argv[2]

with open(base_file, 'r') as f:
    lines = f.readlines()

with open(output_file, 'r') as f:
    output_lines = f.readlines()

COUNT = len(lines)
CORRECT = 0
for i in range(len(lines)):
    if lines[i].strip() == output_lines[i].strip():
        CORRECT += 1
    else:
        print("Incorrect X - Expected: ", lines[i].strip(), "| Got: ", output_lines[i].strip())

print("Correctness: ", CORRECT, "/", COUNT)
print("Accuracy: ", CORRECT / COUNT * 100, "%")

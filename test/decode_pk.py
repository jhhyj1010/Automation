#!/usr/bin/env python
import base64
import sys

pk = sys.argv[1]
print("Key before decoding is: \n", pk)
decoded_key = base64.b64decode(pk)
print("Key after decoding is:\n", decoded_key)

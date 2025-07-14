#!/usr/bin/env sh

# get file name from envrionment variable
if [ -z "$FILE_NAME" ]; then
    output_file=${FILE_NAME}
else
    if [ -f "result.txt" ]; then
        mv result.txt result_$(date +%Y-%m-%d_%H-%M-%S).txt
    fi
    output_file="result.txt"
fi

# open file for writing
if [ -f "$output_file" ]; then
    rm $output_file
fi
# create file
touch $output_file

# get user
echo "User: $(whoami | awk '{print $1}')" > $output_file
echo "Current folder: $(pwd | awk '{print $1}')" >> $output_file
# calculate total size of current folder
echo "Total size of current folder: $(du -sh Shell_Question | awk '{print $1}' | tail -1)" >> $output_file
echo "All 404 Errors:" >> $output_file
echo "The total lines of code 404 are $(grep -wr "404" access.log | wc -l )" >> $output_file
echo "The IP list of code 404 are:" >> $output_file

grep -wr "404" access.log | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' >> $output_file
spec_ip=$(grep -wr "404" access.log | grep -Eo '10.110.120.110')   
if [ -n "$spec_ip" ]; then
    echo "10.110.120.110 is in IP list" >> $output_file
else
    echo "10.110.120.110 is not in IP list" >> $output_file
fi

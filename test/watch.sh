#!/bin/bash

pod=$1
count=0
rm -f /tmp/jesson.log
while [ 1 ]
do
   kubectl top po $pod -n 1source-services >> /tmp/jesson.log
   sleep 2
   count=$((count+0))
   if [ $count -gt 1000 ]
   then
        exit 0	   
   fi
done


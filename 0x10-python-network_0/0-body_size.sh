#!/bin/bash
# a bash script that returns the size of the body response
echo $(curl -sI "$1"| grep -i content-length | awk ' { printf $2 }')

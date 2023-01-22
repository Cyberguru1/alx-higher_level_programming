#!/usr/bin/env bash
# a bash script that returns the size of the body response

out=$(curl -sI "$1"| grep -i content-length | awk ' { printf $2 }')
echo $out

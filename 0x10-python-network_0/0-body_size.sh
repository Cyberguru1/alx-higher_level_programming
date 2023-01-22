#!/usr/bin/env bash
# a bash script that returns the size of the body response

out=$(curl -sI "$1" | grep content-length)

echo $out

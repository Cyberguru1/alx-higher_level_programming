#!/bin/bash
# a script that list all available http methods 
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-

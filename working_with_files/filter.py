#!/usr/bin/python3

import csv

filename = "football.csv"

with open(filename, 'w') as file_object:
    content = file_object.readline()

for line in content:
    print(line)


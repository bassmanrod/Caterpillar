#!/usr/bin/env python3
import re

## 1/16/2023 first hit 
## Rod Simioni

try:

    TextFile = open(r"teksystems.txt", "r").read()

    regEx_1 = r"port (\d+)"
    regEx_2 = r"Client Port: (\d+)"
    regEx_3 = r"s_port:\"(\d+)\""

    regexList = [regEx_1, regEx_2, regEx_3]
     
    for port_number in regexList:
        if re.findall(port_number, TextFile):
            final_list = re.findall(port_number, TextFile)
            for line in final_list:
                   print(line)

except FileNotFoundError:
	print('The file teksystems.txt does not exist!')


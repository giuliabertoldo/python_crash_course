# 10.1 READING FROM A FILE

import os.path
scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'pi_digits.txt')

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

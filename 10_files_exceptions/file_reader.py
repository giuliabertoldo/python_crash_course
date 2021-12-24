# 10.1 READING FROM A FILE

# TO SOLVE ERROR:
## https://stackoverflow.com/questions/25924720/filenotfounderror-errno-2
import os.path
### find the directory where the currently running script resides
scriptpath = os.path.dirname(__file__)
#### uses os.path.join to add test.txt with that path.
filename = os.path.join(scriptpath, 'pi_digits.txt')

# continue with Python Crash Course:
with open(filename) as file_object:
    contents = file_object.read()
print(contents.rstrip())

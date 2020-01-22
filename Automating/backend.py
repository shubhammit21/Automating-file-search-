#Feature: open file directly 
#          open folder containing file
#          open url
#                 
# =============================================================================


# =============================================================================
# BACKEND
#Scan the system and store the path for each file
import os
import csv
path = 'C:\\Automation\\file'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r,file))
store_as_dict = {}
for values in files:
    file = values.rsplit('\\',1)
    store_as_dict[file[1]] = file[0]

with open("C:\\Automation\\file\\test.csv",'w') as f:
    for key in store_as_dict.keys():
        
        f.write("%s,%s\n"%(key,store_as_dict[key]))



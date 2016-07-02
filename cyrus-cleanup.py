
import sys
import re
filename = raw_input("Enter the location of clamav output \n e.g. /home/user/clamoutput.txt : \n")

try:
    in_file = open(filename)
    clamav_cyrus_scan = in_file.read() 
    in_file.close()
except:
    print "File cannot be opened:", filename 
    exit()

file_lines = clamav_cyrus_scan.split('\n')
virus_lines = []

try:
    for line in file_lines:
        while line.split()[-1] == 'FOUND':
            virus_lines.append(line)
            break
except IndexError:
    pass;

user_list = []
virus_list = []
virus_files =[]

try:
    for line in virus_lines:
        line_split = re.split('[/ :]', line)
        #print line_split 
        #space, var, spool, cyrus, mail, letter, user, username, folder, file, detected, found = line_split
        user_list.append(line_split[7])
        virus_split = re.split('[ :-]', line)
        virus_list.append(virus_split[-3])
except IndexError:
   pass;

try:
    for line in virus_lines:
        line_split = re.split('[:]', line)
        virus_files.append[line_split[0]
except IndexError:
   pass;






print "virus found in the following user directories:" 
for users in set(user_list):
    print "{:20}" .format(users)
    "\n"

print "\nthe following virus were found:"
for virus in set(virus_list):
    print "{:20}" .format(virus)


print "run this:"
for files in virus_files: 
    print "{:20}" .format(files)


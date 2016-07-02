
import sys
import re
filename = raw_input("Enter the location of clamav output \n e.g. /home/user/clamoutput.txt : ")

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

try:
    for line in virus_lines:
        line_split = re.split('[/ :]', line)
        print line_split 
        #space, var, spool, cyrus, mail, letter, user, username, folder, file, detected, found = line_split
        user_list.append(line_split[7])
        virus_split = re.split('[ :-]', line)
        virus_list.append(virus_split[-3])
#        print username 
         
#        line_split = line.split(':')
#        file_fix = line_split[0].split(" ")
#        split_file = line_split[0].split("/")
#        virus_split = line_split[1].split()
#        user_list.append(split_file[7])
#        virus_list.append(virus_split[0])
except IndexError:
   pass;

#    if len(line_fix) ==2:
#        print "rm {:20}\ {:20}" .format(line_fix[0],line_fix[1])
#    else:
#        print "rm {:20}" .format(line_fix[0])

print "virus found in the following user directories:" 
for users in set(user_list):
    print "{:20}" .format(users)
    "\n"

print "the following virus were found:"
for virus in set(virus_list):
    print "{:20}" .format(virus)

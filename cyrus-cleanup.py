#! /usr/bin/env python

import textfsm


import sys
import re
#filename = raw_input("Enter the location of clamav output \n e.g. /home/user/clamoutput.txt : \n")

try:
#    in_file = open(filename)
    in_file = open("/root/cyrusavscan")
    raw_text_data = in_file.read() 
    in_file.close()
except:
    print "File cannot be opened:", filename 
    exit()

template = open("clamav_cyrus_parser.template")
fsm_table = textfsm.TextFSM(template)
fsm_results = fsm_table.ParseText(raw_text_data)

user_list = []
virus_list = []
virus_files =[]

try:
    for table_line in fsm_results:
        user_list.append(table_line[0].split('/')[7])
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

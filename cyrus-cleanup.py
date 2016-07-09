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
        virus_list.append(table_line[1].split('-')[0])
except IndexError:
   pass;





print "\r"

print "virus or malware was found in the following user directories:" 
for users in set(user_list):
    print "    {}" .format(users)

print "\r"

print "the following virus were found:"
for virus in set(virus_list):
    print "    {}" .format(virus)



import sys
if len(sys.argv) !=2:
    print ' error: no file input\n usage: python cyrus-cleanup.py /home/user/clamoutput.txt'
    sys.exit(2)

in_file = open(sys.argv.pop())
clamav_cyrus_scan = in_file.read() 
in_file.close()

file_lines = clamav_cyrus_scan.split('\n')

user_list = []
virus_list = []

try:
    for line in file_lines:
        line_split = line.split(':')
        file_fix = line_split[0].split(" ")
        split_file = line_split[0].split("/")
        virus_split = line_split[1].split()
        user_list.append(split_file[7])
        virus_list.append(virus_split[0])
except IndexError:
   pass;

#    if len(line_fix) ==2:
#        print "rm {:20}\ {:20}" .format(line_fix[0],line_fix[1])
#    else:
#        print "rm {:20}" .format(line_fix[0])

print "virus found in the following user directories:" 
for users in set(user_list):
    print "{:20}" .format(users)

print "the following virus were found:"
for virus in set(virus_list):
    print "{:20}" .format(virus)

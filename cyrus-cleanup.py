#manual import of file list here:
clamav_cyrus_scan = '''
/var/spool/cyrus/mail/j/user/judy/Junk E-mail/343.: Html.Phishing.Bank-1199 FOUND
/var/spool/cyrus/mail/j/user/judy/JunkE-mail/343.: Html.Phishing.Bank-1199 FOUND
'''

#for now, it gives you a list of commands to paste back into shell
line_breaks = clamav_cyrus_scan.split('\n')
for line in line_breaks:
    line_split = line.split(':')
    virusmail = line_split[0]
    line_fix = line_split[0].split(" ")
    if len(line_fix) ==2:
        print "rm {:20}\ {:20}" .format(line_fix[0],line_fix[1])
    else:
        print "rm {:20}" .format(line_fix[0])

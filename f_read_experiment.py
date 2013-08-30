#-------------------------------------------------------------------------------
# Name:        experiment - file seek(), read(), string.find()
# Purpose:
#
# Author:      jlegind
#
# Created:     19-04-2012
# Copyright:   (c) jlegind 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from linewriter import LineWriter

def main():

    path = "H:/dwctest/testtest.txt"
    lw = LineWriter(path)
    lw.write_line('Wakey wakey, eggs and baky')
    lw.closing()


##    f = open(path, "r", 2)
##
##    i = 1


##        j = 1
##        str = f.readline()
##        lng = len(str)

##
##        while (j < 5):
##            pos = str.find('\t')
##
##            condition = pos
##            f.seek(pos,0)
##            str = f.read(lng-pos)
##            print pos, '\n'
##            print str, '\n'
##            j += 1

        #print 'line', i, ' is: ', f.readline()
        #i += 1

    #f.close()

def get_condition():
    return

if __name__ == '__main__':
    main()


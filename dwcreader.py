#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      jlegind
#
# Created:     28-03-2012
# Copyright:   (c) jlegind 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import csv

def read_param(num_lines):

    read_dwc(num_lines)

def test_dwc(path):

    dwca = open(path, "r", 2)
    print 'DwC-A file name is: ', dwca.name
    print 'Mode is: ', dwca.mode

def read_dwc (path , num_lines, sep):

    dwca = open(path, "r", 2)

    i = 1
    while (i <= num_lines):
        dwcLine = dwca.readline()
        myFields = dwcLine.split(sep)
        #print myFields[4]
        #print 'line', i, ' is:\t', dwcLine
        print dwcLine,
        i += 1

    sub_set = num_lines
    return sub_set
    dwca.closed()

def read_csv (path, num_lines):

    spamReader = csv.reader(open(path, "r"))
    k = num_lines
    j = 0
    while (j<k):
        line = spamReader.next()
        print 'line ', j, ' is: ', line
        #print '*** Number of elements in list***', len(line)
        j += 1

##    #j = 1
##    #for row in spamReader:
##     #   if j == 11:
##      #      break
##       # print 'line ', j, ' is: ', row
##        #j += 1
##
##    #csva = open(path, "rb")
##
##    #i = 0
##    #while (i < 4):
##     #   print 'line', i, ' is: ', csv.reader(csva)
##      #  i += 1

    sub_set = num_lines
    return sub_set
    spamReader.closed()

def write_from (sub_set):

    print 'test write_from'



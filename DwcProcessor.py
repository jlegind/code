#-------------------------------------------------------------------------------
# Name:        dwc processor
# Purpose:      Processes DwC files according to certain criteria
#
# Author:      jlegind
#
# Created:     15-05-2012
# Copyright:   (c) jlegind 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import operator
from linewriter import LineWriter

class DwcProcessor(object):
    """Takes a DwC archive file and returns lines depending on the criteria.
    Can test on a single field."""

    dwc_path = ''
    spamReader = object
    dwca = object

    def __init__(self, path):
        self.dwc_path = path
        self.dwca = codecs.open(self.dwc_path, mode="r", encoding="utf-8-sig")

    def read_lines(self, number, path, printer=0):
        """Reads a number of lines and either prints them or writes to a file.
        Takes parameter no of lines, path to file, boolean print 1 or 0"""

        header = ''
        if (printer == 1):
            my_list = self.dwca.readline()
            my_list = my_list.split('\t')
            for j in my_list:
                header = header + "(%s)%s\t" %(my_list.index(j), j.strip())
                #print "(%s)%s" %(my_list.index(j), j),
            print header

            for j in range(0, number):
                print self.dwca.readline(),
        else:
            lw = LineWriter(path)

            for j in range(0 ,number):
                lw.write_line(self.dwca.readline())
            lw.closing()



    def read_field(self, position, lng=1024, my_operator=">", print_field=1):
        """Position refers to column/field in the archive starting at position [0]
        The "lng" attribute decides the lenght of the field lenght to be tested
        my_operator accepts ">", "<" and "=" """

        ops = {"<": operator.lt, ">": operator.gt, "=": operator.eq}
        op_function = ops[my_operator]
        print "starter.."
        dwcline = self.dwca.readline()
        j = 0

        try:
            while (dwcline):
##                j += 1
##                if (j%1000 is 0):
##                    print j,

                if not dwcline:
##                    print 'End of file - BREAK!'
                    break
                my_list = dwcline.split('\t')
                my_field = my_list[position]
                if (op_function(len(my_field), lng)):

                    if (print_field == 0):
                        j += 1
                        my_list = '\t'.join(my_list)
                        yield my_list
##                    else:
##                        j += 1
##                        print my_field
                dwcline = self.dwca.readline()

            print '\n Total count = ', j , " ***"

        except IOError:
            print 'Cannot read string'


    def read_value(self, position, value, printer = 0):
        """Position refers to column/field in the archive starting at position [0]
        The "value" attribute is the value tested against. Print boolean 1 or 0
        read_value() yields a tab separated string"""

        try:
            a_str = self.dwca.readline()
            j = 0
            k = 0
            modulus_count = None

            while (a_str):
                k += 1
                if (k%1000 is 0):
                    modulus_count = k,

                if not a_str:
                    print 'End of file - BREAK!'
                    break
                try:
                    my_list = a_str.split('\t')
                    my_field = my_list[position]

                    if (my_field == value):
                        j += 1
                        my_str = '\t'.join(my_list)
                        yield my_str

                except IndexError:
                    print "List error. Non valid position."
                    print a_str
                a_str = self.dwca.readline()

            if (value == ''):
                value = 'NULL'
            print '\n Total count of', value , '= ', j , " ***"
        except IOError:
            print 'Cannot read string'


    def update_value(self, position, value, path, Iter=0):
        """update_value() takes a position [0-n] and a value to be updated and updates this
        value at the position. Default parameter is Iter=0. If Iter is set to 1, update_value()
        will replace the values with an iterated value. Output will be written to the
        parameter given in path."""

        try:
            record = self.read_field(position, 0, 0)
            lw = LineWriter(path)

            for j in record:

                    fields = j.split('\t')
                    if (iter==0):
                        fields[position] = value
                    else:
                        value += 1
                        fields[position] = str(value)
                    fields = '\t'.join(fields)
                    lw.write_line(fields)

            lw.closing()

        except IndexError:
            print "update_value() List error. Non valid position."
            print str

    def read_all(self):
        """read_all() returns the size of the file in KB and MB."""

        size = os.path.getsize(self.dwc_path)
        size = float(size)
        kilobytes = size / 1024
        megabytes = size / 1048576
        return '%.0f KB\n%.2f MB' % (kilobytes, megabytes)

        if (kilobytes > 1000000.0):
            print "File size too big. > 1 GB."

        else:
            pass

    def line_count(self):
        """Counts the number of lines and return the integer"""

        with open(self.dwc_path) as f:
            for i, l in enumerate(f):
                pass
        return i + 1
        f.close()

    def read_behind(self, path, num_lines, size=-64, behind=2, printer=0):
        """read_behind() takes a number of lines to be read from the back of the file
        or the middle of the file. The default size in kilobytes is set to 64k,
        but this can be overwritten by assigning another value. Remember to put in
        minus before the size value. Takes args.: Path to file, number of lines, size,
        behind (if set to 2; reads from behind, if not; reads from the middle of the file)"""

        if (behind==2):
            self.dwca.seek((size*1024), behind)
            mylist = []
            k = self.dwca.readline()#reads truncated line
            k = self.dwca.readline()

            while k != '':
                mylist.append(k)
                k = self.dwca.readline()

            mylist.reverse()    #Sorts the list so the original order is preserved
        else:
            size = os.path.getsize(self.dwc_path)
            mid_size = size/2
            self.dwca.seek(mid_size, 0)
            mylist = []
            k = self.dwca.readline()    #reads truncated line
            k = self.dwca.readline()
            j = 0
            while j < num_lines:
                mylist.append(k)
                k = self.dwca.readline()
                j+= 1

        if (printer == 1):
            for j in mylist[:num_lines:]:
                print j,
        if (printer == 0):
            lw = LineWriter(path)
            for j in mylist[:num_lines:]:
                lw.write_line(j)
            lw.closing()
        if k == '':
            print 'end is reached'

    def closing(self):
        self.dwca.close()






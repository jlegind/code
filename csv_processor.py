#-------------------------------------------------------------------------------
# Name:     csv processor
# Purpose:  Process csv files according to certain criteria
#
# Author:      jlegind
#
# Created:     01-05-2012
# Copyright:   (c) jlegind 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import csv

class Csv_processor:
    '''Takes a csv file and returns a number of lines (arrays).
    Can also print lines based on a minimum length of a field'''

    csv_path = ''
    spamReader = object
    dwca = object

    def __init__(self, path):

        self.csv_path = path
        dwca = open(self.csv_path, "r")

        self.spamReader = csv.reader(dwca)

    #returnes a number of arrays
    def lines(self, number):

        __j = 0
        line = []

        while (__j < number):
           line.append(self.spamReader.next())
           __j += 1

        return line
        dwca.close()

    def fields(self, position, lng=1024):
        j = 0
        try:
            for row in self.spamReader:
                j += 1
                if (len(row[position])>lng):
                    print row
                    break
                elif (j % 10000 is 0):
                    print j,
        except IOError:
            print row
        except:
            print "error , line ", j, '\n', row

    def field_value(self, position, value, printer=0):
        j = 0
        i = 0
        try:
            print self.spamReader.next()
            for row in self.spamReader:
                i += 1
                if (row[position] == value):
                    j += 1
                    if (printer == 1):
                        print row
                        #self.spamReader.next()
                elif (i % 10000 is 0):
                    print i
            return j
        except IOError:
            print "IOError : ", row
        except:
            print "error , line ", i, '\n', row

    def file_len(self):
        with open(self.csv_path) as f:
            for i, l in enumerate(f):
                pass
        return i + 1
        f.close()




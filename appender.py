#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jlegind
#
# Created:     25-04-2012
# Copyright:   (c) jlegind 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

class Appender:
    'Appends strings to a list and returns the list'

    myList = []
    item = ''

    def __init__(self, item, delimiter, *vartuple):
        #self.myList = []
        self.item = item
        self.delimiter = delimiter
        self.vartuple = vartuple
        to_append = ''

        for var in vartuple:
                to_append = to_append + delimiter + var

        item = item + to_append + '\n'
        self.myList.append(item)

    def reset_list(self):
        Appender.myList = []

    def reset_item(self):
        self.item = ''



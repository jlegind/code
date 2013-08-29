#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jlegind
#
# Created:     03-09-2012
# Copyright:   (c) jlegind 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

class LineWriter:
    '''Receives lines and writes them to a file'''

    def __init__(self, path):
        self.path = path
        self.fw = codecs.open(path, mode="a", encoding="utf-8-sig")

    def write_line(self, line):

        self.fw.write(line)

    def closing(self):
        self.fw.close()
        print 'File %s closed.' % (self.path)



#-------------------------------------------------------------------------------
# Name:        xmlresponseprocessor
# Purpose:      Class shall parse through an xml file containing DwC records
#               and identify individual records according to specific parameters
#
# Author:      jlegind
#
# Created:     24-05-2012
# Copyright:   (c) jlegind 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import xml.etree.ElementTree as xml
import sys

class XmlResponseProcessor:
    'Looks for specific individual records'

    file_path = ''
    tree = object

    #Tries to create an ElementTree wrapper object. Takes arg. 'path'
    #to an XML file. Exeption will print the error string containing the line
    #number and column(starting at position 0)
    def __init__(self, path):
        try:
            self.file_path = path
            self.tree = xml.parse(self.file_path)
        except:
            err = sys.exc_info()[1]
            print "we have problems..."
            print ("Error = %s"% err)


##    def read_records(self):
##        rootElement = tree.getroot()
##        records = rootElement.findall("record")
##
##        if records != None:
##            for record in records:
##                print record.tag

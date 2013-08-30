#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jlegind
#
# Created:     25-05-2012
# Copyright:   (c) jlegind 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from xmlresponseprocessor import XmlResponseProcessor as xmlP

def main():

    path = "C:/Users/jlegind/Documents/xml/search_response6213.xml"

    xml = xmlP(path)


if __name__ == '__main__':
    main()

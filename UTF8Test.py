#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jlegind
#
# Created:     06-12-2012
# Copyright:   (c) jlegind 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from DwcProcessor import DwcProcessor

class UTF8Test(DwcProcessor):
    '''Simply tests whether a test file is UTF-8 encoded.
    Takes a file path parameter and tests one line at the time and prints the
    line number if the string is not UTF-8'''

    def __init__(self, path):
        super(UTF8Test, self).__init__(path)

        my_file = self.dwca
        dwcline = my_file.readline()
        j = 0

        while (dwcline):
            try:
                dwcline.decode('utf-8')
            except UnicodeDecodeError:
                print "Invalid UTF-8 in line %s" % (j)

            dwcline = my_file.readline()
            j +=1
            if (j %1000 is 0):
                print j,

        else:
            print '%s appears to conform with UTF-8' % (path)


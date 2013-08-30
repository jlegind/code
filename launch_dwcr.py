#-------------------------------------------------------------------------------
# Name:        launch_dwcr
# Purpose:      Creates and executes objects for parsing DwC files
#
# Author:      jlegind
#
# Created:     16-04-2012
# Copyright:   (c) jlegind 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import dwcreader
from UTF8Test import UTF8Test
from DwcProcessor import DwcProcessor as processor
from linewriter import LineWriter
from csv_processor import Csv_processor


def main():

    #my_path = "C:/Users/jlegind/Documents/DwC/Rasanen/eml.xml"
    #my_path = "C:/Users/jlegind/Documents/DwC/birdlife/gbifexport_afghanistan.txt"
    #my_path = "C:/Users/jlegind/Documents/From_Publishers/GBIF-McGill.txt"
    my_path = "E:/artdata/occurrence.txt"
    #dwcreader.read_dwc(my_path, 5, '\t')
    #dwcreader.test_dwc(my_path)
    #my_path = "H:/Leon/occurrence.txt"
    #my_path = "H:/GBIF-Spain/DarwincoreA.txt"
    #my_path = "H:/custom_exports/temperley_2012-10-09_NAF.txt"
    #dwcreader.read_csv(my_path, 1000)
##    csv_p = Csv_processor(my_path)
####    for j in csv_p.lines(10):
####        print j
##    csv_p.field_value(15, 'Belarus', 1)

    #my_path = "H:/dwctest/test8.txt"

    write_path = "E:/senckenberg/test2.txt"

    dwcP = processor(my_path)
    #dwcP(my_path)
    #dwcP.read_lines(10000, write_path, printer=0)
##    dwcP.read_behind(write_path, 10000, behind=0, printer=0)
##    dwcP.read_behind(write_path, 10000, behind=2, printer=0)
    print dwcP.line_count()
####
##    for j in dwcP.read_field(42, 1, my_operator="<", print_field=0):
##        printing = 0
##        if (printing == 1):
##            pass
##        else:
##            print j,
    #print dwcP.read_all()

##    lw = LineWriter(write_path)
##    printer = 0
##    for j in dwcP.read_value(15, 'Russia', printer=1):
##        if (printer == 1):
##            print j,
##        else:
##            lw.write_line(j)
##    lw.closing
##
##    dwcP.closing()

    #dwcP.update_value(19, 0, write_path, 1)
    #my_utf = UTF8Test(my_path)

if __name__ == '__main__':
    main()

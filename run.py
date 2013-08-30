#-------------------------------------------------------------------------------
# Name:        runner
# Purpose:      Launching code with as little control logic as possible
#
# Author:      jlegind
#
# Created:     25-04-2012
# Copyright:   (c) jlegind 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import appender
import csv_processor

def main():

    p = 'H:/NSW/raw_occurrence_record.csv'
    #p = 'C:/Users/jlegind/Documents/DwC/iNaturalist2/observations.csv'
    j = csv_processor.Csv_processor
    k = j(p)

    items = k.lines(100)
    #k.field_value(29 , '')

    for item in items:
        out_string = '\t'.join(item)
        print out_string

    #print k.file_len()
    #k.fields(4, lng=250)
    ##k.fields(1)


if __name__ == '__main__':
    main()

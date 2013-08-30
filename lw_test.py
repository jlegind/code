#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jlegind
#
# Created:     01-08-2013
# Copyright:   (c) jlegind 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from linewriter import LineWriter

def main():
    lw = LineWriter("E:/test/test1.txt")
    lw.write_line('Line twhree')
    lw.closing
    lw.write_line('Line four')
    #lw.closing

if __name__ == '__main__':
    main()

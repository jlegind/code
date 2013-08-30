#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jlegind
#
# Created:     17-04-2012
# Copyright:   (c) jlegind 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/python
import time
import appender

def main():

    t0 = time.clock()
    ##path = r"C:/Users/jlegind/Documents/DwC/test/occurrence.txt"
    path = r"C:/Users/jlegind/Documents/DwC/test/taxon.txt"
    wpath = r"C:/Users/jlegind/Documents/DwC/test/write.txt"
    f = open(path, "r", 2)
    fw = open(wpath, "a")

    i = 1
    global str
    ##apd = appender.Appender
    aList = []
    l_counter = 5
    jj = 0

    while (str):

        str = f.readline()

        if not str:
            print 'Breaking!!!'
            break

        mystr = str.split('\t')
        myField = mystr[2]

        if (len(myField) > 20):
                apd = appender.Appender
                apd(mystr[1], '\t',  myField)
                aList = apd.myList
                #apd.reset_item
                #print aList

        if (len(aList) == l_counter):
                fw.writelines(aList)
                aList = []
                #print aList, '!!!'
                apd.myList = []
                jj += 1
                print '***', jj,

        #print jj,

##        j = 1
##        str = f.readline()
##        lng = len(str)
##
##        while (j < 5):
##            pos = str.find('\t')
##
##            condition = pos
##            f.seek(pos,0)
##            str = f.read(lng-pos)
##            print pos, '\n'
##            print str, '\n'
##            j += 1
    if (len(aList) < l_counter):
        print aList
        fw.writelines(aList)

    f.close()
    fw.close()
    t1 = time.clock()
    print 'Start: ', round(t0, 4) , "\t Stop: " , round(t1, 4)

if __name__ == '__main__':
    main()

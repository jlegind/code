#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jlegind
#
# Created:     18-06-2013
# Copyright:   (c) jlegind 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

try:
    con = mdb.connect('mogo.gbif.org', 'jan', 'f4runitYu', 'portal');

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    ver = cur.fetchone()

    print "Database version : %s " % ver

except mdb.Error, e:

    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

finally:

    if con:
        con.close()
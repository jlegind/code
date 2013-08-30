# -*- coding: utf8 -*-
'''
*******************************
***  DB BASE MODULE
*******************************
$RCSfile: base_dbmod.py,v $
$Revision: 1216 $
$Author: markus $
$Date: 2012-10-16 21:12:09 +0200 (Di, 16 Okt 2012) $

The biocase.wrapper database base module to access datasources.
This is a base class for other dbmods that at least need to implement the connection method 
if they are compliant to the Python DB API 2.0.'''
import sys, string

from string                                import join
from biocase.wrapper.errorclasses         import *
from biocase.wrapper.sql.select         import sqlSelect


import logging
log = logging.getLogger("pywrapper.dbmod")


# uses inherited ANSI SQL
        

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
class DBBasemodule(sqlSelect):
    __version__ = '0.1'
    __dbmod__    = u'DB base module'
    
    # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    def __repr__(self):
        return ("%s v%s" %(self.__class__.__dbmod__, self.__class__.__version__) )

    # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    def __init__(self, psfObj):
        # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
        
        sqlSelect.__init__(self, psfObj)
        #
        # connect to DB        
        
        self.conn = self.createDBconnection()
        
    
    # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    def __del__(self):
        # release db connection
        try:
            self.conn.close()
            log.info("successfully closed %s db connection."%self.__dbmod__)
        except:
            log.error("error when trying to close the %s db connection."%self.__dbmod__)

    # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    def createDBconnection(self):
        raise DbModuleNotSpecifiedError

    # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    def execSelect(self, selectList, whereObj=None, orderByList=[], limit=None, offset=None):
        '''execute a select statement. 
        the selectList gives the wanted attribute/alias tuples,
        the optional whereObj the WHERE filter,
        the optional orderbyList the ORDER BY clause as attribute/alias tuples,
        the optional limit the LIMIT/TOP limitation as an integer.'''
        # get SQL string
        (sql, paras) = self.select(selectList, whereObj, limit=limit, orderByList=orderByList, offset=offset)
        # execute statement
        return self.execSQL(sql, paras)

    # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    def fixAllIds(self, AllIds):
        return AllIds
    
    # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    def execDistinct(self, selectList, whereObj=None):
        '''Select distinct statement. The default routine does a regular select and filters only unique records via Python.'''
        log.debug("Select Distinct List: "+str(selectList))
        # build SELECT clause
        select = "DISTINCT %s" %(join( [self.joinDBAttrObj(dbt) for dbt in selectList], ', ' ) )
        # get SQL string
        (sql, paras) = self.select(selectList, whereObj, selectReplacementString=select, orderByList=selectList)
        # execute statement
        return [r[0] for r in self.execSQL(sql, paras)]

    # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    def execCount(self, DBAttrObj, whereObj=None):
        '''SELECT COUNT(x) statement. The default routine does a regular select and counts the records via Python.'''
        recCount = -1
        # build the select COUNT part
        select = self.apply_template('count', [self.joinDBAttrObj(DBAttrObj)])
        # get complete SELECT SQL string
        (sql, paras) = self.select([DBAttrObj], whereObj, selectReplacementString=select)
        recCount = self.execSQL(sql, paras)[0][0]
        try:
            recCount = int(recCount)
        except:
            pass
        # return result
        return recCount
    
    # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    def execSQL(self, sql, paras=None):     
        # create cursor:
        self.c = self.conn.cursor()
        # execute SQL statement and return result
        log.debug("start DB query")
        try:
            log_sql = sql
            sql = sql.encode(self.psfObj.encoding)
            if paras is not None:
                try:
                    log.info("Executing SQL: '%s' with parameters: %s" %(sql, "'"+join([unicode(p) for p in paras], "', '")+"'"))
                except:
                    log.info("Executing SQL: '%s'" %(log_sql))
                    log.debug("Could not log used SQL parameters")
            else:
                log.info("Executing SQL: '%s'" % (log_sql))
        except:
            self.c.close()
            raise SQLunicodeGenerationError()
        # EXECUTE SQL
        try:
            if paras is None:
                self.c.execute(sql)
            else:
                self.c.execute(sql, paras)
                #self.c.execute(sql, ('%', 'Acalyptophis peronii'))
        except:
            raise SQLError(sql, paras)

        tmp = self.c.fetchall()
        log.debug("end DB query")
        log.info("Hits: "+str(len(tmp)))
        if log.isEnabledFor(logging.DEBUG):
            try:
                if type(tmp) == type('a'):
                    rsString = unicode(tmp, self.psfObj.encoding)
                else:
                    rsString = unicode(tmp)
                log.debug("Resulting Recordset:  "+rsString )
            except:
                log.debug("The Recordset Result could not be converted to a string")
        self.c.close()
        return tmp

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    def execSQLnonUnicode(self, sql, paras=None):
        
        # create cursor:
        self.c = self.conn.cursor()
        # execute SQL statement and return result
        log.debug("start DB query")
        
        # EXECUTE SQL
        try:
            if paras is None:
                self.c.execute(sql)
            else:
                self.c.execute(sql, paras)
        except:
            raise SQLError(sql, paras)                
        tmp = self.c.fetchall()
        log.debug("end DB query")
        log.debug("Hits: "+str(len(tmp)))
        if log.isEnabledFor(logging.DEBUG):
            try:
                if type(tmp) == type('a'):
                    rsString = tmp, self.psfObj.encoding
                else:
                    rsString = tmp
                log.debug("Resulting Recordset:  "+rsString )
            except:
                log.debug("The Recordset Result could not be converted to a string")
        self.c.close()
        
        return tmp
    
    def getTables(self):
        log.error("in base")
        return None

    def getColumns(self, table):
        log.error("in base")
        return None

    def verifyTables(self, tableList):        
        if self.getTables() == None:
            return []
        errornousTables = []
        dbTables = [t.lower() for t in self.getTables()]
        for confTable in [ct.lower() for ct in tableList]:
            if not confTable in dbTables:
                errornousTables.append(confTable)
        #log.error("dbTables: " + str(dbTables))
        #log.error("tableList: " + str(tableList))
        #log.error("errornousTables: " + str(errornousTables))
        return errornousTables

    def hasMetaInfo(self):
        return False

import sqlite

DISPLAY_COLUMNS = [ 'AcctId', 'src', 'dst', 'disposition', 'answer', 'end', 'duration' ]
SELECT = """\
    SELECT %(column)s
    FROM cdr
    ORDER BY %(sort)s AcctId DESC 
    LIMIT %(start)d, %(count)d
"""

SELECT_SEARCH = """\
    SELECT %(column)s  
    FROM cdr
    WHERE %(where)s
    ORDER BY %(sort)s AcctId DESC
    LIMIT %(start)d, %(count)d
"""

class CDR(object):
    def __init__(self, db):
        self._conn = sqlite.connect(db)
        self._curs = self._conn.cursor()
        self._columns = ""
        for column in DISPLAY_COLUMNS:
            self._columns = self._columns + column + ", "
        self._columns = self._columns[:-2]
        print('Connected to file')

    def close(self):
        self._curs.close()
        self._conn.close()

    def search_read_page(self, search, start, count, sorting):
        where = ''
        searchcolindex = 0
        for searchcol in search:
            where = where + DISPLAY_COLUMNS[searchcolindex] + ' LIKE \'%' + searchcol + '%\' AND '
            searchcolindex = searchcolindex + 1
        sql = SELECT_SEARCH % {'column': self._columns, 'sort': self.sort(sorting), 'where': where[:-5], 'start': int(start), 'count': int(count)}
        print sql
        self._curs.execute(sql)
        return self.read(count)
        
    def read_page(self, start, count, sorting):
        sql = SELECT % {'column':self._columns, 'sort': self.sort(sorting), 'start': int(start), 'count': int(count)}
        print(sql)
        self._curs.execute(sql)
        return self.read(count)
    def sort(self, sorting):
        """Create sort string, ends with ", "
        """
        sortsql = ''
        for (column, order) in sorting:
            sortsql = sortsql + column + ' ' + order.upper() + ', '
        return sortsql
    def read(self, count):
        rows = self._curs.fetchmany(count)
        l = list()
        for row in rows:
            #print row['src']
            #print row
            entry = CDREntry()
            entry.update(row)
            l.append(entry)
        return l
    
    def total(self):
        self._curs.execute('SELECT COUNT(*) FROM cdr')
        row = self._curs.fetchone()
        return row[0]
        
cdr = None
class CDREntry(dict):
    """Model a CDR Entry.
    """
    
    def __repr__(self):
        return "<CDREntry('%s', '%s')>" % (self['src'], self['dst'])
    


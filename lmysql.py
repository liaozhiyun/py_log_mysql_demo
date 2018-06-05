

import pymysql

class MySQLCommand(object):
    def __init__(self,host,port,user,passwd,db):
        self.host = host
        self.port = port
        self.user = user
        self.password = passwd
        self.db = db


    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.password,db=self.db)
            self.cursor = self.conn.cursor()
        except:
            print('connect mysql error.')

    def select(self,sql):
        try:
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return rows;
        except:
            print(sql + ' select failed.')
            return None


    def insert(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return 0
        except:
            print(sql + ' insert failed.')
            self.conn.rollback()
            return -1

    def update(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return 0
        except:
            print(sql + ' update failed.')
            self.conn.rollback()
            return -1


    def Close(self):
        self.cursor.close()
        self.conn.close()

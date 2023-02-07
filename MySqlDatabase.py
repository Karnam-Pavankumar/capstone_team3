import mysql.connector

class Mysql_DBaccess:

    def __init__(self,host,user,password,db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        try :
             self.connection = mysql.connector.connect( host=self.host,database=self.db,user=self.user,
              password=self.password)
        except:
               print("error while connecting to to database !!")

    def inser_data( self,filename):
        self.filename = filename
        self.cur = self.connection.cursor()
        sql = 'Insert into files(filename) values(%s);'
        val = (self.filename)
        self.cur.execute(sql,(val,))
        self.connection.commit()

    def search( self ):
        self.cur = self.connection.cursor()
        sql = "SELECT * FROM files limit 0 to 10"
        data = self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def searchDB(self,filname):
        self.f = "filename"
        sql = "select * from files where filename like '%{0}'".format(filname)
        self.cur.execute(sql)
        row = self.cur.fetchone()
        if row==None:
            return 0
        else:
            print(row)

dbobj = Mysql_DBaccess('localhost','root','root','searchfiles')
dbobj.inser_data('c://hcl//file.txt')
dbobj.searchDB('c://hcl//file.txt')






import pymssql


class MSSQL:

    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            raise(NameError,"no dataset informations")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db, charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"connection failed")
        else:
            return cur

    def ExecQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

def main():
    ms = MSSQL(host="192.168.170.1",user="EBook",pwd="ebook", db="ebookdata")
    resList = ms.ExecQuery("SELECT name,sex,class FROM Student_test")
    for (student) in resList:
        print student

if __name__ == '__main__':
    main()
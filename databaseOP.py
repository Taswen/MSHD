import pymysql


class DatabaseOperate:

    def __init__(self):
        self.host = '47.93.229.92'
        self.port = 3306
        self.db = 'data'
        self.user = 'nero'
        self.password = 'Buptsse18.'

        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.password)
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def getAllData(self):
        self.cursor.execute("select count(id) as total from Earthquake")
        data = self.cursor.fetchone();

        print(f"当前数量： {data}")

    def __del__(self):
        self.cursor.close()


if __name__ == "__main__":
    db_op = DatabaseOperate()
    db_op.getAllData()
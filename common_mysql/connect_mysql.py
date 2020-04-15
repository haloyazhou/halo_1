import pymysql
import allure
'''
pip install PyMySQL==0.9.3
'''

dbinfo = {
    "host": "123.56.113.64",
    "user": "root",
    "password": "123456",
    "port": 3319}


class DbConnect():
    def __init__(self, db_cof, database=""):
        # self.db_cof = db_cof
        # 打开数据库连接
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **dbinfo)

        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def select(self, sql):
        # SQL 查询语句
        # sql = "SELECT * FROM EMPLOYEE \
        #        WHERE INCOME > %s" % (1000)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        # SQL 删除、提交、修改语句
        # sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
           # 执行SQL语句
           self.cursor.execute(sql)
           # 提交修改
           self.db.commit()
        except:
           # 发生错误时回滚
           self.db.rollback()

    def close(self):
        # 关闭连接
        self.db.close()

def select_sql(select_sql):
    '''查询数据库'''
    db = DbConnect(dbinfo, database="hrun")
    result = db.select(select_sql)  # 查询
    db.close()
    return result

def execute_sql(insert_sql):
    '''执行sql'''
    db = DbConnect(dbinfo, database="hrun")
    db.execute(insert_sql)  # 查询
    db.close()


if __name__ == '__main__':
    # db = DbConnect(db_cof=dbinfo, database="apps")
    # sql = 'SELECT * from auth_user WHERE username="test";'
    # result = db.select(select_sql)
    # print(result[0]["username"])
    sql = 'SELECT * from UserInfo WHERE username="test1"'
    sql1='DELETE from UserInfo WHERE username="test1"'
    a = execute_sql(sql1)
    b=select_sql(sql)
    print(b)



#import yaml
#import os
#
#
#def readyml(yamlPath):
#    '''读取yaml文件内容
#    realPath: 文件的真实绝对路径 '''
#    curPath = os.path.dirname(os.path.realpath(__file__))
#    print(curPath)
#    yamPath = os.path.join(curPath, "register.yml")
#    if not os.path.isfile(yamlPath):
#        raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s" % yamlPath)
#    # open方法打开直接读出来
#    f = open(yamlPath, 'r', encoding='utf-8')
#    cfg = f.read()
#    d = yaml.load(cfg)
#    # 用load方法转字典
#    print("读取的测试文件数据：%s"%d)
#    return d
#
#if __name__ == '__main__':
#    data = readyml("register.yml")
#




#
#
# yaml安装：
# 文件说明：
#    lxml-4.4.3-cp36-cp36m-win_amd64.whl          yaml文件
#       python36 匹配 lxml4.4.3
# 下载地址
#      https://www.lfd.uci.edu/~gohlke/pythonlibs/
# 安装操作：进入下载的文件-cmd-输入(需要pip设置环境变量)
#      pip install lxml-4.4.3-cp36-cp36m-win_amd64.whll
# (没有wheel库需要：pip install wheel）
# 替换原本django 操作mysql的包，现在使用pumysql操作数据库
import pymysql

pymysql.install_as_MySQLdb()
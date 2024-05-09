u=input("请输入您要设置的用户名：")
p=input("请输入您的密码：")     #输入所需要查询的内容
def select(u):
    import pymysql
    # 1.数据库的连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='ZhLzh106', db='userdb', charset='utf8')
    # 2.创建操作的游标
    cursor = conn.cursor()
    # 3.设置字符编码以及自动提交
    cursor.execute('set names utf8')
    cursor.execute('set autocommit=1')
    # conn.commit()为手动提交
    # 4.编写sql语句
    sql = "select * from users where username=%s"  # 执行查询操作,查询特定内容，特定内容用占位符替代
    print(sql)
    # 5.执行sql语句得到结果集
    cursor.execute(sql, u)  # 查询到的结果集放入cursor里面了，n替代占位符的内容
    # 得到结果集的三种方式
    # fetchone()    得到一条数据
    # fetchmany(n)  得到n条数据
    # fetchall()    得到所有数据
    result = cursor.fetchone()  # fetch 出来，密码唯一，只有一条内容
    print(result)  # 打印所查询到的内容
    # 6.关闭游标和连接
    cursor.close()
    conn.close()
    return result
def insert(u,p):
    import pymysql
    # 1.数据库的连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='ZhLzh106', db='userdb', charset='utf8')
    # 2.创建操作的游标
    cursor = conn.cursor()
    # 3.设置字符编码以及自动提交
    cursor.execute('set names utf8')
    cursor.execute('set autocommit=1')
    # conn.commit()为手动提交
    # 4.编写sql语句
    sql = "insert into users(username,password) values(%s,%s)"  # 执行查询操作,查询特定内容，特定内容用占位符替代
    print(sql)
    # 5.执行sql语句得到结果集
    cursor.execute(sql, (u,p))  # 查询到的结果集放入cursor里面了，n替代占位符的内容
    # 得到结果集的三种方式
    # fetchone()    得到一条数据
    # fetchmany(n)  得到n条数据
    # fetchall()    得到所有数据
    #result = cursor.fetchone()  # fetch 出来，密码唯一，只有一条内容
    #print(result)  # 打印所查询到的内容
    # 6.关闭游标和连接
    cursor.close()
    conn.close()
    #return result
while 1:
    if select(u):
        print("您输入的用户名已存在:")
        n = input("请重新输入您的用户名：")
        continue
    else:
        insert(u, p)
        break

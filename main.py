import sqlite3
from datetime import datetime

conn = sqlite3.connect('dbs/sms.db')


def run_sql(sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        return cursor
    except sqlite3.OperationalError as e:
        print('\033[31;5m [x]出现错误 \033[0m')
        print(e)


def hint():
    print('\033[35;5m//--------------------------------------------//\033[0m')
    print('\033[32;5m请按下列格式使用 : \033[0m')
    print('\033[33;5m[注意] 学号格式为4位班级号加4位学生编号，共八位（例如：53140821）')
    print('\033[32;5m    1.[签到]      sign-in 姓名 学号')
    print('    2.[按人查询]  query-by-student 学号 日期')
    print('    3.[按班查询]  sign-by-class 班级号 日期 \n\033[0m')


def query_by_class(cid, date):
    sql = "select name,sid from sign where sid like '{cid}%' and date='{date}' ;".format(cid=cid, date=date)
    cursor = run_sql(sql)
    for line in cursor.fetchall():
        print(line)
    pass


def query_by_student(sid, date):
    sql = "select name,sid from sign where sid='{sid}' and date='{date}' ;".format(sid=sid, date=date)
    cursor = run_sql(sql)
    for line in cursor.fetchall():
        print(line)
    pass


def sign_in(name, sid):
    now = str(datetime.now()).split(' ')[0]
    sql = "insert into sign (name,sid,date) values('{name}','{sid}','{now}') ;".format(name=name, sid=sid, now=now)
    run_sql(sql)
    pass


command = 'start'

while True:
    hint()
    command = input()
    command = command.split(' ')

    if command[0] == 'exit':
        conn.close()
        break

    if command[0] == 'sign-in':
        print('\033[32;5m[签到]\033[0m')
        if len(command) != 3:
            print('\033[31;5m参数个数不对\033[0m')
            continue
        sign_in(command[1], command[2])
        continue

    if command[0] == 'query-by-student':
        print('\033[32;5m[按学号查询]\033[0m')
        if len(command) != 3:
            print('\033[31;5m参数个数不对\033[0m')
            continue
        query_by_student(command[1], command[2])
        continue

    if command[0] == 'query-by-class':
        print('\033[32;5m[按班级查询]\033[0m')
        if len(command) != 3:
            print('\033[31;5m参数个数不对\033[0m')
            continue
        query_by_class(command[1], command[2])
        continue

    print('\033[31;5m[x]命令错误,请重新输入\033[0m')

print('谢谢使用,再见 !')

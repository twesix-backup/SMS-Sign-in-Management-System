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
        print('[x]出现错误')
        print(e)


def hint():
    print('//--------------------------------------------//')
    print('请按下列格式使用 : ')
    print('[注意] 学号格式为4位班级号加4位学生编号，共八位（例如：53140821）')
    print('    1.[签到]      sign-in 学号')
    print('    2.[按人查询]  query-by-student 学号')
    print('    3.[按班查询]  sign-by-class 班级号 \n')


def query_by_class(cid, date):
    sql = "select name,sid from sign where sid like '{cid}%' and date='{date}' ;".format(cid=cid, date=date)
    cursor = run_sql(sql)
    for line in cursor.fetchall():
        print(line)
    pass


def query_by_student(sid, date):
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
        print('[签到]')
        if len(command) != 3:
            print('参数个数不对')
            continue
        sign_in(command[1], command[2])
        continue

    if command[0] == 'query-by-student':
        print('[按学号查询]')
        if len(command) != 3:
            print('参数个数不对')
            continue
        query_by_student(command[1], command[2])
        continue

    if command[0] == 'query-by-class':
        print('[按班级查询]')
        if len(command) != 3:
            print('参数个数不对')
            continue
        query_by_class(command[1], command[2])
        continue

    print('[x]命令错误,请重新输入')

print('谢谢使用,再见 !')

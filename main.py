import sqlite3

conn = sqlite3.connect('dbs/sms.db')


def run_sql(sql):
    cursor = conn.cursor()
    conn.execute(sql)
    conn.commit()


def hint():
    print('请按下列格式使用 : ')
    print('    1.[签到]     sign-in 姓名 班级')
    print('    2.[按人查询]  query-by-student 学号')
    print('    3.[按班查询]  sign-by-class 班级号 \n')


def query_by_class(cid):
    pass


def query_by_student(sid):
    pass


def sign_in(name, cid):
    pass


command = 'start'
hint()

while True:
    command = input()
    command = command.split(' ')

    if command[0] == 'exit':
        conn.close()
        break

    if command[0] == 'sign-in':
        print('sign-in')
        continue

    if command[0] == 'query-by-student':
        print('query-by-student')
        continue

    if command[0] == 'query-by-class':
        print('query-by-class')
        continue

    print('[x]命令错误,请重新输入')

print('谢谢使用,再见 !')

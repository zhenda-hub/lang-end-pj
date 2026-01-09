# Author: zhenda
# Site  :
# time  : 2021/10/27 22:34
# 整体就是函数堆叠， 重复代码很多
import os
import time

filename = '学生信息/student.txt'

format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
format_data = '{:^6}\t{:^13}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'


def show_student(student_lst):
    print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'Java成绩', '总成绩'))
    for d in student_lst:
        print(format_data.format(
            d['id'], d['name'], d['english'], d['python'], d['java'], d['english'] + d['python'] + d['java']))
    answer = input('是否继续？按空格继续')
    if answer == ' ':
        return


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='UTF_8')
    except:
        stu_txt = open(filename, 'w', encoding='UTF_8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def save2(lst):
    try:
        with open(filename, 'a', encoding='UTF_8') as txt_obj:
            for item in lst:
                txt_obj.write(str(item) + '\n')
    except:
        with open(filename, 'w', encoding='UTF_8') as txt_obj:
            for item in lst:
                txt_obj.write(str(item) + '\n')


def main():
    print('欢迎使用学生信息系统')
    while True:  # 驿站 主界面
        menu()
        try:
            rst = int(input('请选择功能编号'))
            if rst in range(8):
                if rst == 0:
                    rst2 = input('您确定要退出吗？y/n')
                    if rst2 not in ['y', 'n']:
                        print('输入错误')
                        continue
                    if rst2 == 'y':
                        print('谢谢使用')
                        break  # 退出
                    else:
                        continue  # 返回界面
                elif rst == 1:
                    backup()
                    insert()
                elif rst == 2:
                    search()
                elif rst == 3:
                    backup()
                    delete()
                elif rst == 4:
                    backup()
                    modify()
                elif rst == 5:
                    mysort()
                elif rst == 6:
                    total()
                elif rst == 7:
                    show()
            else:
                print('输入错误，请重新输入')
                continue
        except BaseException as e:
            print('发生错误', e)


# 菜单
def menu():
    print('===========================学生信息管理系统===============================')
    print('------------------------------功能菜单----------------------------------')
    print('\t\t\t1. 录入学生信息')
    print('\t\t\t2. 查找学生信息')
    print('\t\t\t3. 删除学生信息')
    print('\t\t\t4. 修改学生信息')
    print('\t\t\t5. 排序')
    print('\t\t\t6. 统计学生总人数')
    print('\t\t\t7. 显示所有学生信息')
    print('\t\t\t0. 退出系统')
    print('-----------------------------------------------------------------------')


# 1
def insert():
    student_list = []  # 所有学生列表
    while True:
        student_id = input('请输入id， 如1001')
        name = input('请输入姓名')
        try:
            english = int(input('请输入英语成绩'))
            python = int(input('请输入python成绩'))
            java = int(input('请输入java成绩'))
        except BaseException as e:
            print('输入错误', e)
            continue
        # 学生信息放入字典中
        student = {'id': student_id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        rst = input('是否输入下一位同学信息？y/n')
        if rst == 'y':
            continue
        else:
            break

    # save(student_list)
    save2(student_list)
    print('学生信息保存完毕！')


# 2
def search():
    while True:
        flag = False
        show_lst = []
        # ------------------------------------------------------------------
        if os.path.exists(filename):
            answer = input('按id查询请输入1， 按姓名查询请输入2')
            if answer == '1':
                answer2 = input('请输入查询id')
            elif answer == '2':
                answer2 = input('请输入查询姓名')
            else:
                print('输入错误')
                search()  # 重新调用
            with open(filename, 'r', encoding='UTF_8') as rfile:
                student_oldlist = rfile.readlines()
                for item in student_oldlist:
                    # dict类型
                    print(eval(item))
                    print(type(eval(item)))
                    # str类型
                    print(item)
                    print(type(item))
                    print(item.strip())
                    print(type(item.strip()))

                    d = eval(item)
                    # d = dict(eval(item))
                    if answer == '1':
                        if d['id'] == answer2:
                            flag = True
                            show_lst.append(d)
                    elif answer == '2':
                        if d['name'] == answer2:
                            flag = True
                            show_lst.append(d)
            show_student(show_lst)
            if not flag:
                print('没有找到此学生信息')

        else:
            print('没有学生信息txt, 将返回主菜单')
            break

        answer3 = input('是否继续查询学生信息？y/n')
        if answer3 == 'y':
            continue
        else:
            break


# 3
def delete():
    show()
    while True:
        student_id = input('请输入希望删除的学生id')
        if os.path.exists(filename):
            with open(filename, 'r', encoding='UTF_8') as file:
                student_old = file.readlines()
        else:
            print('学生信息不存在')
            student_old = []
        if student_old:
            flag = False  # 标记是否找不到这个id
            with open(filename, 'w', encoding='UTF_8') as file2:  # 覆盖写入
                # d = {}
                for item in student_old:
                    d = dict(eval(item))  # 字符串->字典
                    if d['id'] != student_id:
                        file2.write(str(d) + '\n')
                    else:
                        flag = True
            if flag:
                print(f'{student_id}学生信息被删除')
            else:
                print(f'没有{student_id}学生信息')
        else:
            print('没有学生文件')
            break
        show()

        rst = input('还要继续删除学生信息吗？y/n')
        if rst == 'y':
            continue
        else:
            break


# 4
def modify():
    student_old = []
    d = {}
    # ------------------------------------------------------------------------
    show()
    d = {}
    flag = False
    stu_id = input('请输入希望修改的学生id')
    if not os.path.exists(filename):
        print('学生信息txt不存在')
        return  # 跳出函数

    with open(filename, 'r', encoding='UTF_8') as rfile:
        student_old = rfile.readlines()
    with open(filename, 'w', encoding='UTF_8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == stu_id:
                flag = True
                print('学生信息找到了，请修改：')
                while True:
                    try:
                        d['name'] = input(f"请修改姓名({d['name']})")
                        d['english'] = int(input(f"请修改英语成绩({d['english']})"))
                        d['python'] = int(input(f"请修改python成绩({d['python']})"))
                        d['java'] = int(input(f"请修改java成绩({d['java']})"))
                    except:
                        print('输入信息错误，请重新输入')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改完毕')
            else:
                wfile.write(str(d) + '\n')

        if not flag:
            print(f'学生id为{stu_id}的学生不存在')

    show()
    answer = input('是否继续修改其他学生信息？y/n')
    if answer == 'y':
        modify()
    else:
        return


# 5
def mysort():
    while True:
        student_oldlst = []
        d = {}
        student_lst = []
        # -------------------------------------
        order = input('希望升序排列请输入0， 降序排列请输入1')
        if order not in ['1', '0']:
            print('输入错误，请重新输入')
            continue
        mode = input('选择成绩排序：英语按0，python按1，java按2，总成绩按3')
        if mode not in ['0', '1', '2', '3']:
            print('输入错误，请重新输入')
            continue

        if not os.path.exists(filename):
            print('文件不存在')
            break
        with open(filename, 'r', encoding='UTF_8') as rfile:
            student_oldlst = rfile.readlines()
        for item in student_oldlst:
            d = dict(eval(item))
            student_lst.append(d)
        if mode == '0':
            student_lst.sort(key=lambda x: int(x['english']), reverse=bool(int(order)))
        elif mode == '1':
            student_lst.sort(key=lambda x: int(x['python']), reverse=bool(int(order)))
        elif mode == '2':
            student_lst.sort(key=lambda x: int(x['java']), reverse=bool(int(order)))
        elif mode == '3':
            student_lst.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['java']),
                             reverse=bool(int(order)))
        show_student(student_lst)
        break


# 6
def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='Utf_8') as rfile:
            student_oldlist = rfile.readlines()
        print(f'一共有{len(student_oldlist)}个学生')
    else:
        print('学生信息txt不存在')


# 7
def show():
    show_lst = []
    # -------------------------------------------------------------------
    with open(filename, 'r', encoding='UTF_8') as rfile:
        student_oldlist = rfile.readlines()
        for i in student_oldlist:
            d = dict(eval(i))
            show_lst.append(d)
        show_student(show_lst)


def backup():
    current_dir = os.getcwd()
    if not os.path.isdir(current_dir + '\\学生信息'):
        os.makedirs('学生信息')

    time_str = ''
    t = time.localtime()
    for item in t:
        # if len(time_str) < 10:
        time_str += str(item)
    t1 = os.path.splitext(filename)
    # print(t1[0] + time_str + t1[1])

    with open(filename, 'r', encoding='UTF_8') as rfile:
        with open(t1[0] + time_str + t1[1], 'w', encoding='UTF_8') as wfile:
            wfile.write(rfile.read())


if __name__ == '__main__':
    main()
    # print(os.getcwd())

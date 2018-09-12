# -*- coding: utf-8 -*-

import random, user, re

class usermgr:

    def __init__(self):
        # 每次运行前，先清空state文件的内容
        with open('state', 'w') as file_state:
            file_state.truncate()
        self.users = [] # todo : replace this line with your own code

    def getUserNum(self):
        """
        :rtype: int
        """
        count = 0
        print('用户：')
        with open('users', 'r') as file_user:
            for line in file_user.readlines():
                if line[0] == '#':
                    continue
                count += 1
                print(line.strip().split('\t')[0])
        print('总计：', count, '个用户')
        print('==================')
        return count

    def addUser(self, uname, pwd):
        """
        :uname type: string
        :pwd type: string
        :rtype: int
        """
        us = user.user(uname, pwd)
        print('正在添加用户' + uname)
        print('正在登录')
        if us.login() == True:
            print('登录成功')
            print('正在检查是否为已存在用户')
            with open('users', 'r+') as file_user:
                for line in file_user.readlines():
                    if line[0] == '#':
                        continue
                    mat = re.match(uname+'\t', line)
                    if mat != None:
                        print('这个用户已存在')
                        print('==================')
                        return 2
                print('用户' + uname + '添加成功')
                print('==================')
                file_user.write(uname+'\t'+pwd+'\n')
                return 0
        else:
            print('登录失败')
            print('==================')
        return 1

    def post(self, title, message):
        """
        :title type: string
        :message type: string
        :rtype: bool
        """
        num = self.getUserNum()
        rd = random.randint(1, num)
        uname, pwd = "", ""
        with open('users', 'r') as file_user:
            for line in file_user.readlines():
                if line[0] == '#':
                    continue
                uname, pwd = line.strip().split('\t')
                rd -= 1
                if rd == 0:
                    SSR = user.user(uname, pwd)
                    SSR.login()
                    print('用户' + uname + '发帖中')
                    print('==================')
                    return SSR.post(title, message)
        return False

    def preContent(self, type):
        """
        :type type: int
        :rtype: string
        """
        res=""
        if type ==1:
            print('打开文件contents/1')
            with open('contents/1', 'r') as file_contents:
                res=file_contents.read()
        elif type == 2:
            print('打开文件contents/2')
            with open('contents/2', 'r') as file_contents:
                res=file_contents.read()
        elif type == 3 :
            print('打开文件contents/3')
            with open('contents/3', 'r') as file_contents:
                res=file_contents.read()
        elif type == 4 :
            print('打开文件contents/custom')
            with open('contents/custom', 'r') as file_contents:
                res=file_contents.read()
        print('==================')
        return res

    def writeContent(self, content):
        """
        :content type: string
        :rtype: bool 
        """
        print('正在打开文件contents/confirm写入')
        print('==================')
        with open('contents/confirm', 'w') as file_confirm:
            file_confirm.write(content)
        return True 

    def up(self, pid, userNum):
        """
        :pid type: string
        :userNum type: int
        :rtype: None
        """
        # 每次运行前，先清空state文件的内容
        print('清空文件state内容')
        with open('state', 'w') as file_state:
            file_state.truncate()

        count = 0
        users = []
        with open('users', 'r') as file_user:
            for line in file_user.readlines():
                if line[0] == '#':
                    continue
                if count >= userNum:
                    break
                else:
                    uname, pwd = line.strip().split('\t')
                    users.append(user.user(uname, pwd))
                    count += 1
                continue
        if count < userNum:
            print('已获得', count, '个用户，', '不足', userNum, '个')
        """
        with open('users', 'r') as file_user:
            for line in file_user.readlines():
                if line[0] == '#':
                    continue
                if count >= userNum:
                    break
                else:
                    uname.append(line[0:line.find('\t')])
                    pwd.append(line[line.find('\t')+1:line.find('\n')])
                    count=count+1
        """
        count = 0
        with open('contents/confirm', 'r') as file_confirm:
            with open('state','w') as file_state:
                mes=""
                for line in file_confirm.readlines():
                    if line[0] == '#':
                        continue
                    if line[-2:-1] != '\\':
                        mes = mes + line[:-1]
                        us = users[count]
                        us.login()
                        state = us.reply(pid, mes)
                        statestr = "（" + us.username + "发表了“" + mes + "”："
                        if state == True:
                            statestr = statestr + "成功"
                        else:
                            statestr = statestr + "失败"
                        statestr = statestr + "）\n"
                        file_state.write(statestr)
                        print(statestr)
                        count = (count + 1) % userNum
                        mes = ""
                    else:
                        mes = mes + line[:-2] + '\n'
        print('==================')
        return None

    def upShow(self):
        """
        :rtype: string
        """
        ret = ""
        with open('state', 'r') as file_state:
            ret = file_state.read()
        print('状态刷新中')
        print('==================')
        return ret

if __name__ == "__main__":
    hex = usermgr()
    #print(hex.post('usermgr的post test', '1234567890巴拉啦魔仙能力球！'))
    pass

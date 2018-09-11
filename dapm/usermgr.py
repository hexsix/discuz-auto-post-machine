# -*- coding: utf-8 -*-

import random, user, re

class usermgr:

    def __init__(self):
        self.users = [] # todo : replace this line with your own code

    def getUserNum(self):
        count = 0
        with open('users', 'r') as file_user:
            for line in file_user.readlines():
                if line[0] == '#':
                    continue
                count += 1
                #print(line.strip())
        return count

    def addUser(self, uname, pwd):
        """
        :uname type: string
        :pwd type: string
        :rtype: int
        """
        # todo : 服务器没开，去除login判断已经通过离线测试
        us=user.user(uname,pwd)
        if us.login() == True:
            with open('users','r+') as file_user:
                for line in file_user.readlines():
                    if line[0] == '#':
                        continue
                    mat=re.match(uname+'\t',line)
                    if mat!=None:
                        return 2
                file_user.write(uname+'\t'+pwd+'\n')
                return 0
        return 1

    def post(self, title, message):
        """
        :title type: string
        :message type: string
        :rtype: bool
        """
        # todo : 服务器没开，还没有通过测试，也意识到需要 timeout
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
                    print(uname + '\t' + pwd)
                    SSR = user.user(uname, pwd)
                    SSR.login()
                    SSR.post(title, message)
                    return True
        return False

    def preContent(self, type):
        """
        :type type: int
        :rtype: string
        """
        # todo
        return ""

    def writeContent(self, content):
        """
        :content type: string
        :rtype: None
        """
        with open('contents/confirm', 'w') as file_confirm:
            file_confirm.write(content)
        return None

    def up(self, pid, userNum):
        """
        :pid type: string
        :userNum type: int
        :rtype: None
        """
        # todo
        return None

    def upShow(self):
        """
        :rtype: string
        """
        ret = ""
        with open('state', 'r') as file_state:
            ret = file_state.read()
        return ret

if __name__ == "__main__":
    hex = usermgr()
    #print(hex.post('usermgr的post test', '1234567890巴拉啦魔仙能力球！'))
    print(hex.addUser('test2','test2'))
    print(hex.addUser('test2','test2'))

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
        res=""
        if type ==1:
            with open('contents/1', 'r') as file_contents:
                res=file_contents.read()
        elif type == 2:
            with open('contents/2', 'r') as file_contents:
                res=file_contents.read()
        elif type == 3 :
            with open('contents/3', 'r') as file_contents:
                res=file_contents.read()
        elif type == 4 :
            with open('contents/custom', 'r') as file_contents:
                res=file_contents.read()
        return res

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
         # todo : 服务器没开，去除login判断已经通过离线测试
        uname=[]
        pwd=[]
        count=0
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
        count=0
        with open('contents/comfirm', 'r') as file_confirm:
            with open('state','w') as file_state:
                mes=""
                for line in file_confirm.readlines():
                    if line[0]=='#':
                        continue
                    if line[-2:-1] != '\\':
                        mes=mes+line[:-1]
                        us=user.user(uname[count],pwd[count])
                        #print(count,mes)
                        #state=True
                        us.login()
                        state = us.reply(pid,mes)
                        statestr="（"+uname[count]+"发表了“"+mes+"”："
                        if state == True:
                            statestr=statestr+"成功"
                        else:
                            statestr=statestr+"失败"
                        statestr=statestr+"）\n"
                        file_state.write(statestr)
                        count=(count+1)%userNum
                        mes=""
                    else:
                        mes=mes+line[:-2]+'\n'
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
    #print(hex.addUser('test1','test1'))
    #print(hex.addUser('test2','test2'))
    #print(hex.preContent(4))
    #hex.up(10,2)
    pass

# -*- coding: utf-8 -*-

import requests, re

class user:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        return None

    def login(self):
        """
        保存 Cookie 在 ./{username}.cookie 中
        返回登陆成功与否 True/False
        """

        # init
        domain = 'http://10.51.120.224/upload/'
        headers = {
            'Host':'10.51.120.224',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Referer': 'http://10.51.120.224/upload/forum.php',
        }  
        session = requests.session()
        session.headers.clear()
        session.headers.update(headers)

        # formhash
        URL = domain + 'member.php?mod=logging&action=login&infloat=yes&handlekey=login&inajax=1&ajaxtarget=fwin_content_login'
        r = session.get(URL)
        p = r.text.find('formhash') + len('formhash" value="')
        formhash = r.text[p: p+8]
        #print(formhash)

        # login
        postdata = {
            'username': self.username,
            'password': self.password,
            'formhash': formhash,
            'questionid':'0',
            'answer':''
        }
        """
        headers = {
            'Host':'10.51.120.224',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Referer': 'http://10.51.120.224/upload/forum.php',
        }  
        """
        URL = domain + 'member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=Lb833&inajax=1'
        content = session.post(URL, headers = headers, data = postdata)
        if 'succeedhandle_login' not in content.text:
            print('User:%s login Failed.\n'%self.username)
            print(content.text)
            return False
        return True

if __name__ == '__main__':
    testuser = user('administrator', 'r7))thl7^6QD')
    print(testuser.login())

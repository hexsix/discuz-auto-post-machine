# -*- coding: utf-8 -*-

import urllib.request, urllib, http.cookiejar, re, requests

class user:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.headers = {
            'Host':'10.51.120.224',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }  
        self.session = requests.session()
        return None

    def login(self):
        # init
        domain = 'http://10.51.120.224/upload/'
        self.session.headers.clear()
        self.session.headers.update(self.headers)

        # formhash
        URL = domain + 'member.php?mod=logging&action=login&infloat=yes&handlekey=login&inajax=1&ajaxtarget=fwin_content_login'
        r = self.session.get(URL)
        p = r.text.find('formhash') + len('formhash" value="')
        #p = r.text.find('formhash') + len('formhash=')
        formhash = r.text[p: p+8]
        print(formhash)

        # login
        postdata = {
            'username': self.username,
            'password': self.password,
            'formhash': formhash,
            'questionid':'0',
            'answer':''
        }
        URL = domain + 'member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=Lb833&inajax=1'
        content = self.session.post(URL, headers = self.headers, data = postdata)
        
        if 'succeedhandle_login' not in content.text:
            print('User:%s login Failed.\n'%self.username)
            print(content.text)
            return False
        
        return r.cookies

    def post(self, subject, message): 
        url = 'http://10.51.120.224/upload/forum.php?mod=post&action=newthread&fid=2' 
        # formhash 
        r = self.session.get(url)
        #p = r.text.find('formhash') + len('formhash" value="')
        p = r.text.find('formhash') + len('formhash=')
        formhash = r.text[p: p+8]
        print(formhash)

        #发帖
        postdata = {
            'allownoticeauthor':'1',
            'formhash':formhash,
            'message':message,
            'posttime':'',
            'save':'',
            'subject':subject,
            'usesig':'1',
            'wysiwyg':'1',
        }
        url = 'http://10.51.120.224/upload/forum.php?mod=post&action=newthread&fid=2&extra=&topicsubmit=yes'
        r = self.session.post(url, data = postdata)
        print(r.content.decode('utf-8'))
        return None

if __name__ == '__main__':
    testuser = user('administrator', 'r7))thl7^6QD')
    cookie = testuser.login()
    print('succeed login, cookie=', cookie)
    testuser.post('2nd test post 1st merge', 'wula! sakimichan is perfect!')

# -*- coding: utf-8 -*-

import urllib.request, urllib, http.cookiejar, re, requests,usermgr

class user:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.domain = 'http://10.51.120.224/upload/'
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

    def _getFormhash_(self, url, param):
        """
        # this fuction recieve a url and return the formhash of the url
        :type url: string
        :type param: int
        :rtype: string
        """
        formhash = ''
        r = self.session.get(url)
        if param == 0:
            p = r.text.find('formhash') + len('formhash" value="')
            formhash = r.text[p: p + 8]
        else:
            p = r.text.find('formhash') + len('formhash=')
            formhash = r.text[p: p+8]
        return formhash

    def login(self):
        # init
        self.session.headers.clear()
        self.session.headers.update(self.headers)

        # formhash
        URL = self.domain + 'member.php?mod=logging&action=login&infloat=yes&handlekey=login&inajax=1&ajaxtarget=fwin_content_login'
        formhash = self._getFormhash_(URL, 0)

        # login
        postdata = {
            'username': self.username,
            'password': self.password,
            'formhash': formhash,
            'questionid':'0',
            'answer':''
        }
        URL = self.domain + 'member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=Lb833&inajax=1'
        content = self.session.post(URL, headers = self.headers, data = postdata)
        
        if 'succeedhandle_login' not in content.text:
            print('User:%s login Failed.\n'%self.username)
            #print(content.text)
            return False
        
        return True

    def post(self, subject, message): 
        """
        :type subject: string
        :type message: string
        :rtype: None
        """
        # formhash 
        url = self.domain + 'forum.php?mod=post&action=newthread&fid=2' 
        formhash = self._getFormhash_(url, 1)

        # post
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
        url = self.domain + 'forum.php?mod=post&action=newthread&fid=2&extra=&topicsubmit=yes'
        r = self.session.post(url, data = postdata)
        #print(r.content.decode('utf-8'))
        return None

    def reply(self, tid, message):
        """
        :type tid: string
        :type message: string
        :rtype: None
        """
        # formhash 
        url = self.domain + 'forum.php?mod=viewthread&tid=' + tid + '&extra=page%3D1'
        formhash = self._getFormhash_(url, 1)

        # reply
        postdata={
            'formhash':formhash,
            'handlekey':'reply',
            'message':message,
            'noticeauthor':'',	
            'noticeauthormsg':'',	
            'noticetrimstr':'',	
            'subject':'',	
            'usesig':'1',
        }
        url = self.domain + 'forum.php?mod=post&infloat=yes&action=reply&fid=2&extra=&tid=' + tid + '&replysubmit=yes&inajax=1'
        r = self.session.post(url, data = postdata)
        #print(r.content.decode('utf-8'))
        return None

if __name__ == '__main__':
    #testuser = user('administrator', 'r7))thl7^6QD')
    #cookie = testuser.login()
    #print('succeed login, cookie=', cookie)
    #testuser.post('我正在默默地测试', 'wula! sakimichan is perfect!')
    #testuser.reply('23','我在测试回复')
    testuesermgr = usermgr.usermgr()
    testuesermgr.getUserNum()


# -*- coding: utf-8 -*-

import urllib.request, urllib, http.cookiejar, re, requests

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

        # cooooookie
        cookie_filename = './' + self.username + '.cookie'
        cj = http.cookiejar.MozillaCookieJar(cookie_filename)
        handler = urllib.request.HTTPCookieProcessor(cj)
        opener = urllib.request.build_opener(handler)

        # formhash
        URL = domain + 'member.php?mod=logging&action=login&infloat=yes&handlekey=login&inajax=1&ajaxtarget=fwin_content_login'
        response = opener.open(URL)
        source_code = response.read().decode('utf-8')
        patt = re.compile(r'.*?name="formhash".*?value="(.*?)".*?')
        formhash = patt.search(source_code)
        if not formhash:
            print('GET formhash Failed while login.\n')
            print('User:%s login Failed.\n'%self.username)
            return False
        formhash = formhash.group(1)

        # login
        postdata = {
            'username': self.username,
            'password': self.password,
            'formhash': formhash,
            'questionid':0,
            'answer': '',
            'referer': domain
            }
        postdata = urllib.parse.urlencode(postdata).encode(encoding='utf-8')
        req = urllib.request.Request(
            url = domain + 'member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=Lb833&inajax=1',
            data = postdata
            )
        response = opener.open(req)
        cj.save(cookie_filename)
        source_code = response.read(300).decode('utf-8')
        if 'succeedhandle_login' not in source_code:
            print('User:%s login Failed.\n'%self.username)
            return False
        return True
    
    def read_cookie(self):
        filename = self.username + '.cookie'
        cookie = ''
        with open(filename, 'r') as f:
            lines = f.readlines()
            for single_line in lines:
                if single_line[0] == '#':
                    continue
                else:
                    single_line = single_line.rstrip('\n')
                    single_line_split = single_line.split('\t')
                    if len(single_line_split) < 2:
                        continue
                    cookie = cookie + single_line_split[-2]+'='+single_line_split[-1]+';'
        return cookie

    def post(self, subject, message, cookie):
        #发帖
        postdata = {
            'allownoticeauthor':'1',
            'formhash':'182c27fd',
            'message':message,
            'posttime':'',
            'save':'',
            'subject':subject,
            'usesig':'1',
            'wysiwyg':'1',
        }
        #postdata = urllib.parse.urlencode(postdata).encode(encoding='utf-8')
        head={
            'POST':'/upload/forum.php?mod=post&action=newthread&fid=2&extra=&topicsubmit=yes HTTP/1.1',
            'Host':'10.51.120.224',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://10.51.120.224/upload/forum.php?mod=post&action=newthread&fid=2',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '134',
            'Cookie': cookie,
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        #head = urllib.parse.urlencode(head).encode(encoding='utf-8')
        url = 'http://10.51.120.224/upload/forum.php?mod=post&action=newthread&fid=2&extra=&topicsubmit=yes'
        r = requests.post(url, data = postdata, headers = head)
        #print(r.read())
        return None

if __name__ == '__main__':
    testuser = user('administrator', 'r7))thl7^6QD')
    print('succeed login', testuser.login())
    cookie = testuser.read_cookie()
    testuser.post('a test post 1st merge', 'abcdefghijklmnopqrstuvwxyz', cookie)

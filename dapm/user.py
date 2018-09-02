# -*- coding: utf-8 -*-

import urllib.request, urllib, http.cookiejar, re

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

if __name__ == '__main__':
    testuser = user('administrator', 'r7))thl7^6QD')
    print(testuser.login())

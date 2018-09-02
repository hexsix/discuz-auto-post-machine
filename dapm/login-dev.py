# -*- coding: utf-8 -*-

import urllib.request, urllib, http.cookiejar, re

"""
    通用的登陆DZ论坛
    参数说明parms:
    username:用户名(必填),
    password :密码(必填),
    domain:网站域名，注意格式必须是：http://www.xxx.xx/ (必填),
    answer:问题答案,
    questionid:问题ID,
    referer:跳转地址
    这里使用了可变关键字参数(相关信息可参考手册)
"""

def login_dz(**parms):
    """
    函数接受一个字典 dic
    必须含有三个关键字：domain，username 和 password
    返回登录成功与否 True/False
    """

    # 初始化
    parms_key = ['domain','answer','password','questionid','referer','username']
    arg = {}
    for key in parms_key:
        if key in parms:
            arg[key] = parms[key]
        else:
            arg[key] = ''

    # COOOOOOOOOOOOOOOOOOOOOOOOKIE
    # http.cookiejar 总共有四个主要对象，它们的关系是
    # CookieJar ——> 派生 ——> FileCookieJar ——> 派生 ——> MozillaCookieJar 和 LWPCookieJar
    # 要打开 URL，传统的 urllib.request.urlopen() 函数不支持 cookie，使用 urllib.request.build_opener() 函数来创建自己的自定义 Opener 对象
    # 创建完成后 使用 Opener().open() 打开 URL，或者使用 urllib.request.install_opener(Opener()) 安装此 opener，并通过 urllib.request.urlopen() 打开 URL
    cookie_filename = './' + arg['username'] + '.cookie'
    cj = http.cookiejar.LWPCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(handler)

    # 获取 formhash
    # formhash 的存在是为了避免多次提交，在 discuz 上 POST 数据时，必须要有 formhash
    # formhash 在访问网站时(即使不登录)在网页源码中写明，用正则表达式提取它
    URL_login = arg['domain'] + 'member.php?mod=logging&action=login&infloat=yes&handlekey=login&inajax=1&ajaxtarget=fwin_content_login'
    response = opener.open(URL_login)
    source_code = response.read().decode('utf-8')
    patt = re.compile(r'.*?name="formhash".*?value="(.*?)".*?')
    formhash = patt.search(source_code)
    if not formhash:
        raise Exception('GET formhash Fail!')
    formhash = formhash.group(1)

    # 登陆
    postdata = {
        'answer':arg['answer'],
        'formhash':formhash,
        'password':arg['password'],
        'questionid':0 if arg['questionid']=='' else arg['questionid'],
        'referer':arg['domain'] if arg['referer']=='' else arg['referer'],
        'username':arg['username'],
    }
    postdata = urllib.parse.urlencode(postdata).encode(encoding='utf-8')
    req = urllib.request.Request(
        url = arg['domain'] + 'member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=Lb833&inajax=1',
        data = postdata
    )
    response = opener.open(req)
    source_code = response.read(300).decode('utf-8')
    flag = '登陆失败 %s'%arg['username']
    if 'succeedhandle_login' in source_code:
        flag = True
    return flag

if __name__ == '__main__':
    try:
        flag = login_dz(username='administrator', password='r7))thl7^6QD', domain='http://10.51.120.224/upload/')
        print(flag)
    except Exception as e:
        print('Error:',e)


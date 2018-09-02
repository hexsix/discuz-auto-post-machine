# -*- coding: utf-8 -*-

import urllib.request, urllib, http.cookiejar, re,requests

"""
    通用的DZ论坛发帖
    表单数据:
    allownoticeauthor:1
    formhash:
    message:发帖内容
    posttime:
    save:
    subject:标题
    usesig:1
    wysiwyg:1
    这里使用了可变关键字参数(相关信息可参考手册)
"""
def post_dz(**parms):
    # 初始化
    parms_key = ['domain','subject','message','cookie']
    arg = {}
    for key in parms_key:
        if key in parms:
            arg[key] = parms[key]
        else:
            arg[key] = ''

    """
    # 获取formhash
    cookie = http.cookiejar.LWPCookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    url = arg['domain']
    c = opener.open(url).read()
    patt = re.compile(r'.*?name="formhash".*?value="(.*?)".*?')
    formhash = patt.search(c.decode('utf-8'))
    if not formhash:
        raise Exception('GET formhash Fail!')
    formhash = formhash.group(1)
    """

    #发帖
    postdata = {
        'allownoticeauthor':'1',
        'formhash':'182c27fd',
        'message':arg['message'],
        'posttime':'',
        'save':'',
        'subject':arg['subject'],
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
        'Cookie': arg['cookie'],
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    #head = urllib.parse.urlencode(head).encode(encoding='utf-8')
    r = requests.post(url, data = postdata,headers=head)
    print(r.text);
    return
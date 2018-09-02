# -*- coding: utf-8 -*-

import login,post

'''
#登录
user = 'test1'
pwd = 'mytest'
dom = 'http://10.51.120.224/upload/'

try:
    flag = login.login_dz(username=user,password=pwd,domain=dom)
    print(flag)
except Exception as e:
    print('Error:',e)

'''

#发帖
dom='http://10.51.120.224/upload/forum.php?mod=post&action=newthread&fid=2&extra=&topicsubmit=yes'
sub='你真看的见我吗'
mes='can you really see me'
cok='ueyo_2132_sid=hvXcB5; ueyo_2132_saltkey=jI647768; ueyo_2132_lastvisit=1535862040; ueyo_2132_lastact=1535872159%09forum.php%09ajax; ueyo_2132_ulastactivity=cca2kiKh2fw0S6lCLUJoDt8KR%2Fh1emZPr2Fbe9nopzGkhgcg%2BnyS; ueyo_2132_lastcheckfeed=3%7C1535871866; ueyo_2132_editormode_e=1; ueyo_2132_smile=1D1; ueyo_2132_nofavfid=1; ueyo_2132_forum_lastvisit=D_2_1535871871; ueyo_2132_visitedfid=2; ueyo_2132_st_p=3%7C1535871908%7C60dac6358adec10f380e141c8f77b9ef; ueyo_2132_viewid=tid_15; ueyo_2132_auth=e0a5m1KFjvHzLGtHb6FREze%2F1hlIP9Str4DfpT1dvfYeNDlR5PQALgyIvobyBe8b4BKi68nK%2B8%2FwG1MfOEZN; ueyo_2132_st_t=3%7C1535871873%7C7e5d95489e6546a47adf794d049f1568'
post.post_dz(domain=dom,subject=sub,message=mes,cookie=cok)
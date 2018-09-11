import tkinter as tk

class learn:
    mainwindow = tk.Tk()

    var1=tk.StringVar()
    var2=tk.StringVar()

    frm_l=tk.Frame(mainwindow)
    frm_r=tk.Frame(mainwindow)

    ########################左边

    ll1 = tk.Label(frm_l, 
            text='已有用户：  0',    # 标签的文字
            bg='green',     # 背景颜色
            font=('Arial', 12),     # 字体和字体大小
            width=25, height=2  # 标签长宽
            )

    frm_l1=tk.Frame(frm_l)
    ll2=tk.Label(frm_l1,text ='标题：',font=('Arial', 12),width=5,height=2)
    le1=tk.Entry(frm_l1,width=17,font=('Arial', 12))
    ll3=tk.Label(frm_l1,text ='内容：',font=('Arial', 12),width=5,height=2)
    lt1=tk.Text(frm_l1,width=17,height=20,font=('Arial', 12))
    lb1=tk.Button(frm_l1,text='发表新帖子')
    ll4=tk.Label(frm_l1,text='发表帖子    ',font=('Arial', 12),height=2)

    ###########################右边
    
    frm_r1=tk.Frame(frm_r)
    rl1=tk.Label(frm_r1,text ='用户名：',font=('Arial', 12),width=8,height=2)
    re1=tk.Entry(frm_r1,width=15,font=('Arial', 12))
    rl2=tk.Label(frm_r1,text ='密码：',font=('Arial', 12),width=8,height=2)
    re2=tk.Entry(frm_r1,show='*',width=15,font=('Arial', 12))
    rb1=tk.Button(frm_r1,text='添加用户')
    rl3=tk.Label(frm_r1,text ='添加用户    ',font=('Arial', 12),width=12,height=2)

    frm_r2=tk.Frame(frm_r)
    rr1=tk.Radiobutton(frm_r2,text ='AA',variable =var1 ,value ='A')
    rr2=tk.Radiobutton(frm_r2,text ='BB',variable =var1 ,value ='B')
    rr3=tk.Radiobutton(frm_r2,text ='CC',variable =var1 ,value ='C')
    rr4=tk.Radiobutton(frm_r2,text ='DD',variable =var1 ,value ='D')
    rb2=tk.Button(frm_r2,text ='预览回帖内容')
    rt1=tk.Text(frm_r2,width=35,height=6,font=('Arial', 12))
    rb3=tk.Button(frm_r2,text ='确认回帖内容')
    rl4=tk.Label(frm_r2,text ='确认回帖内容    ',font=('Arial', 12),width=16,height=2)
    
    frm_r3=tk.Frame(frm_r2)
    rl5=tk.Label(frm_r3,text ='用户数量：',font=('Arial', 12),width=16,height=2)
    re3=tk.Entry(frm_r3,width=15,font=('Arial', 12))
    rl6=tk.Label(frm_r3,text ='帖子ID：',font=('Arial', 12),width=16,height=2)
    re4=tk.Entry(frm_r3,width=15,font=('Arial', 12))
    rb4=tk.Button(frm_r3,text ='运行顶贴器')

    frm_r4=tk.Frame(frm_r)
    rt2=tk.Text(frm_r4,width=20,height=20,font=('Arial', 12))
    rb5=tk.Button(frm_r4,text ='状态刷新')

    def __init__(self):
        self.mainwindow.title("can not learn")
        self.mainwindow.geometry('800x600')

        self.frm_l.grid(row=1,column=1)
        self.frm_r.grid(row=1,column=2,padx=10)

        ########################左边
        
        self.ll1.grid(row=1,column=1)

        self.frm_l1.grid(row=2,column =1)
        self.ll2.grid(row = 1,column =1,padx=10)
        self.le1.grid(row =1,column =2)
        self.ll3.grid(row = 2,column =1,padx=10)
        self.lt1.grid(row = 2,column =2)
        self.lb1.grid(row =3, column =2,pady=10)
        self.ll4.grid(row =4,column =2)
        
        ###########################右边
        
        self.frm_r1.grid(row =1 ,column =1,columnspan=2)
        self.rl1.grid(row =1,column =1,padx=20)
        self.re1.grid(row =1,column =2,padx=20)
        self.rl2.grid(row =2,column =1)
        self.re2.grid(row =2,column =2)
        self.rb1.grid(row =1,column =3,rowspan =2,padx=10)
        self.rl3.grid(row =1,column =4,rowspan =2,padx=10)

        self.frm_r2.grid(row=2,column =1)
        self.rr1.grid(row =1,column=1)
        self.rr2.grid(row =2,column=1)
        self.rr3.grid(row =1,column=2)
        self.rr4.grid(row =2,column=2)
        self.rb2.grid(row =3,column =1,pady=10,columnspan=2)
        self.rt1.grid(row=4,column=1,columnspan=3)
        self.rb3.grid(row =5,column =1,pady=10,columnspan=2)
        self.rl4.grid(row =6,column =1,columnspan=2)

        self.frm_r3.grid(row =7,column=1,columnspan=2)
        self.rl5.grid(row =1,column=1)
        self.re3.grid(row =1,column=2)
        self.rl6.grid(row =2,column=1)
        self.re4.grid(row =2,column=2)
        self.rb4.grid(row =3,columnspan=3)

        self.frm_r4.grid(row =2,column =2,padx=20)
        self.rt2.grid(row =1)
        self.rb5.grid(row =2,pady=10)


        ######################config
        self.rr1.config(command =self.c_rr)
        self.rr2.config(command =self.c_rr)
        self.rr3.config(command =self.c_rr)
        self.rr4.config(command =self.c_rr)
        
        self.lb1.config(command =self.c_lb1)
        self.rb1.config(command =self.c_rb1)
        self.rb2.config(command =self.c_rb2)
        self.rb3.config(command =self.c_rb3)
        self.rb4.config(command =self.c_rb4)
        self.rb5.config(command =self.c_rb5)
        # 进入消息循环
        self.mainwindow.mainloop()
        return None
        

    def c_rr(self):

        return None

    def c_lb1(self):

        return None

    def c_rb1(self):

        return None

    def c_rb2(self):

        return None

    def c_rb3(self):

        return None

    def c_rb4(self):

        return None

    def c_rb5(self):

        return None


if __name__ == '__main__':
    cnl=learn()

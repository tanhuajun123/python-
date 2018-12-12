#!/user/bin/evn python
from  tkinter import  ttk,Tk
import tkinter.messagebox
from aip import AipSpeech
from winsound import PlaySound
class Voice(object):
    def __init__(self):
        self.top = tkinter.Tk()
        self.top.title('自制语音合成软件 V0.0.1')
        self.top.geometry('500 x 500')
        self.top.resizable(0,0)
        self.top.protocol('WM_DELETE_WINDOW',self.quit)
        self.label = tkinter.Label(self.top,fg='blue',font=('Helvetica',12,'bold'),
                                   text='在下方空白处输入要转换的文字')
        self.label.pack()
        self.confm = tkinter.Frame(self.top)
        self.consb = tkinter.Scrollbar(self.confm)
        self.consb.pack(side = tkinter.RIGHT,fill=tkinter.Y)
        self.contents = tkinter.Text(self.confm,font=10,height=26,
            width= 50,yscrollcommand=self.consb.set)
        self.consb.config(command=self.contents.yview)
        self.contents.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
        self.confm.pack()
        self.selfm = tkinter.Frame(self.top,borderwidth=1,relief=tkinter.SUNKEN,pady=3)
        per_label = tkinter.Label(self.selfm,font=10,text='发音：')
        per_label.grid(colum=0,row=0)
        self.perchosen = ttk.Combobox(self.selfm,width=5,font=9)
        self.perchosen['valuse'] = ('女声','男声','混合')
        self.perchosen.grid(column = 1,row=0)
        self.perchosen.current(0)
        spd_label = tkinter.Label(self.selfm,font=10,text='语 速 ：')
        spd_label.grid(column=2,row=0)
        self.spdchosen = ttk.Combobox(self.selfm,width=5,font=9)
        self.spdchosen['values'] =('慢速','普通','快速')
        self.spdchosen.grid(column=3,row=0)
        self.spdchosen.current(1)
        pit_label = tkinter.Label(self.selfm,font=10,text='语 调 ：')
        pit_label.grid(column=4,row=0)
        self.pitchaosen = ttk.Combobox(self.selfm,width=5,font=9)
        self.pitchaosen['values'] = ('低','中','高')
        self.pitchaosen.grid(column=5,row=0)
        self.pitchaosen.current(1)
        self.selfm.pack()
        self.bfm = tkinter.Frame(self.top)
        self.clrtext = tkinter.Button(self.bfm,text='清 除',width=10,font=8,
            command=self.clrtext,activeforeground = 'white',activebackground='blue')
        self.play = tkinter.Button(self.bfm,text='播 放',width = 10,font=8,
            command=self.txt2voice,activeforeground='white',activebackground='green')
        self.quit = tkinter.Button(self.bfm,text='退 出',width=10,font=8,
            command=self.quit,activeforeground='white',activebackground='red')
        self.play.pack(side=tkinter.LEFT)
        self.clrtext.pack(side=tkinter.LEFT)
        self.quit.pack(side=tkinter.LEFT)
        self.bfm.pack()
        self.top.mainloop()

    def get_voice_para(self):
        per_dict = {'女声':0,'男声':1,'混合':2}
        spd_dict = {'慢速':3,'普通':5,'快速':9}
        pit_dict = {'低':0,'中':5,'高':9}
        self.per = per_dict[self.perchosen.get()]
        self.spd = spd_dict[self.spdchosen.get()]
        self.pit = per_dict[self.pitchaosen.get()]

    def txt2voice(self):
        APP_ID = '15124327'
        API_KEY = 'tIjgKXnnSM7m0o6LQQHnoffw'
        SECRET_KEY = 'n9u76a12YF4IBA9Qy2Rfw8zBbfG25e1w'
        client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)
        txt = self.contents.get('0.0','end')
        if txt == '\n':
            tkinter.messagebox.showinfo('','请输入你需要播放的文字')
            return
        self.get_voice_para()
        result = client.synthesis(txt,'zh',1,
          {
              'per':self.per,
              'pit':self.pit,
              'spd':self.spd
        })
        if  not isinstance(result,dict):
            self.file_count += 1
            file = self.get_filename()
            with open(file,'wb')  as f :
                f.write(result)
        PlaySound(file)

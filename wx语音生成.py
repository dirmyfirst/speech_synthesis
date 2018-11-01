import wx
import wx.xrc
from aip import AipSpeech
from playsound import playsound
import time
import os

class Voice ( wx.Frame ):
    def __init__( self, parent ):
	    wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "语音合成软件 V1.0", pos = wx.DefaultPosition, size = wx.Size( 380,491 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
	    self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
	    bSizer1 = wx.BoxSizer( wx.VERTICAL )
	    bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
	    self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, "在以下空白处输入要转换的文字", wx.DefaultPosition, wx.DefaultSize, 0 )
	    self.m_staticText1.Wrap( -1 )
	    bSizer2.Add( self.m_staticText1, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
	    self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
	    bSizer2.Add( self.m_textCtrl1, 9, wx.ALL|wx.EXPAND, 5 )
		
		
	    bSizer1.Add( bSizer2, 8, wx.EXPAND, 5 )
		
	    bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
	    bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
	    self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, "发音：", wx.DefaultPosition, wx.DefaultSize, 0 )
	    self.m_staticText2.Wrap( -1 )
	    bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
	    m_comboBox2Choices = [ "男声", "女声", "度逍遥", "度丫丫" ]
	    self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, "选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
	    self.m_comboBox2.SetSelection( 0 )
	    bSizer5.Add( self.m_comboBox2, 0, wx.ALL, 5 )
		
	    self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, "语速：", wx.DefaultPosition, wx.DefaultSize, 0 )
	    self.m_staticText3.Wrap( -1 )
	    bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
	    m_comboBox3Choices = [ "慢速0", "慢速1", "慢速2", "慢速3", "慢速4", "中速5", "快速6", "快速7", "快速8", "快速9"]
	    self.m_comboBox3 = wx.ComboBox( self, wx.ID_ANY, "选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox3Choices, 0 )
	    self.m_comboBox3.SetSelection( 1 )
	    bSizer5.Add( self.m_comboBox3, 0, wx.ALL, 5 )
		
	    self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, "语调：", wx.DefaultPosition, wx.DefaultSize, 0 )
	    self.m_staticText4.Wrap( -1 )
	    bSizer5.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
	    m_comboBox5Choices = [ "低0", "低1", "低2", "低3", "低4", "中5", "高6", "高7", "高8", "高9"]
	    self.m_comboBox5 = wx.ComboBox( self, wx.ID_ANY, "选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox5Choices, 0 )
	    self.m_comboBox5.SetSelection( 1 )
	    bSizer5.Add( self.m_comboBox5, 0, wx.ALL, 5 )
		
		
	    bSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )
		
	    bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
	    self.m_button2 = wx.Button( self, wx.ID_ANY, "播放", wx.DefaultPosition, wx.DefaultSize, 0 )
	    bSizer4.Add( self.m_button2, 2, wx.ALL, 5 )
		
	    self.m_button3 = wx.Button( self, wx.ID_ANY, "清除", wx.DefaultPosition, wx.DefaultSize, 0 )
	    bSizer4.Add( self.m_button3, 2, wx.ALL, 5 )
		
	    self.m_button4 = wx.Button( self, wx.ID_ANY, "退出", wx.DefaultPosition, wx.DefaultSize, 0 )
	    bSizer4.Add( self.m_button4, 2, wx.ALL, 5 )
		
		
	    bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
	    bSizer1.Add( bSizer3, 2, wx.EXPAND, 5 )
		
		
	    self.SetSizer( bSizer1 )
	    self.Layout()
		
	    self.Centre( wx.BOTH )
		
	    # Connect Events
	    self.m_button2.Bind( wx.EVT_BUTTON, self.play )
	    self.m_button3.Bind( wx.EVT_BUTTON, self.clrtext )
	    self.m_button4.Bind( wx.EVT_BUTTON, self.quit )
	    self.m_comboBox2.Bind( wx.EVT_TEXT, self.per )
	    self.m_comboBox3.Bind( wx.EVT_TEXT, self.spd )
	    self.m_comboBox5.Bind( wx.EVT_TEXT, self.pit )
		
	
    def __del__( self ):
	    pass
	
	
    # Virtual event handlers, overide them in your derived class
    def play( self, event ):
        APP_ID = '11432907'
        API_KEY = 'xpwKZZSnY1b7TsrhjLEZVOfh'
        SECRET_KEY = 'fGGj34NPfceGYWC53ZdTCzomUYWjPqcV'
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        txt = self.m_textCtrl1.GetValue()
        if txt == '':
            wx.MessageBox('请输入需要播放的文字')
        else:
            result  = client.synthesis(txt, 'zh', 1,
                                       {'per':self.per,
                                        'pit':self.pit,
                                        'spd':self.spd})
            
        if not isinstance(result,dict):
            time_ = time.strftime("%Y-%m-%d-%H-%M-%S")
            time_file = time_ + '.mp3'
            with open(time_file,'wb') as f:
                f.write(result)
                print('完成')
            cur_path = os.getcwd()
            file_path = os.path.join(cur_path,time_file)
            print(file_path)
            playsound(file_path)
		
	
    def clrtext( self, event ):
        self.m_textCtrl1.Clear()
        event.Skip()
        

    #关闭主窗口前确认一下是否真的关闭
    def quit( self, event ):
        r = wx.MessageBox("是否真的要关闭窗口？", "请确认", wx.CANCEL|wx.OK|wx.ICON_QUESTION)
        if r == wx.OK:
            self.Destroy()
        event.Skip()
        


    def per( self, event ):
	    per_dict = {'女声':0,'男声':1,'度逍遥':3,'度丫丫':4}
	    self.per = per_dict[event.GetString()]
	    event.Skip()

    def spd( self, event ):
	    spd_dict = {'慢速0':0,'慢速1':1,'慢速2':2,'慢速3':3,'慢速4':4,'中速5':5,'快速6':6,'快速7':7,'快速8':8,'快速9':9}
	    self.spd = spd_dict[event.GetString()]
	    event.Skip()
	
    def pit( self, event ):
	    pit_dict = {'低0':0,'低1':1,'低2':2,'低3':3,'低4':4,'中5':5,'高6':6,'高7':7,'高8':8,'高9':9}
	    self.pit = pit_dict[event.GetString()]
	    event.Skip()

	
app = wx.App(False)
frame = Voice(None)
frame.Show(True)
app.MainLoop()

# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"newick 分析", pos = wx.DefaultPosition, size = wx.Size( 343,364 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.choseFile = wx.Button( self, wx.ID_ANY, u"選擇檔案", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.choseFile.SetDefault() 
		bSizer1.Add( self.choseFile, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"合併分支" ), wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"匹配起始值：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.merge_st = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,23 ), 0 )
		fgSizer1.Add( self.merge_st, 0, wx.ALL, 0 )
		
		self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"匹配結束值：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.merge_ed = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,23 ), 0 )
		fgSizer1.Add( self.merge_ed, 0, wx.ALL, 0 )
		
		
		sbSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		self.merge_button = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"合併", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.merge_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"機率分群" ), wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"門檻值：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.value = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,23 ), 0 )
		fgSizer2.Add( self.value, 0, wx.ALL, 0 )
		
		
		sbSizer2.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		self.m_button3 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"分群", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"以根節點距離篩選" ), wx.VERTICAL )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText13 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"門檻值：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer4.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.m_textCtrl9 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,23 ), 0 )
		fgSizer4.Add( self.m_textCtrl9, 0, wx.ALL, 0 )
		
		
		sbSizer3.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		self.m_button61 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"篩選", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_button61, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gSizer1.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"以相近點距離篩選" ), wx.VERTICAL )
		
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText15 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"門檻值：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer5.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.m_textCtrl12 = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,23 ), 0 )
		fgSizer5.Add( self.m_textCtrl12, 0, wx.ALL, 0 )
		
		
		sbSizer5.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		self.m_staticText14 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"比較的點：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		sbSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.m_textCtrl10 = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		sbSizer5.Add( self.m_textCtrl10, 0, wx.ALL, 5 )
		
		self.m_button8 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"篩選", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gSizer1.Add( sbSizer5, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.choseFile.Bind( wx.EVT_BUTTON, self.OpenfileButton )
		self.merge_button.Bind( wx.EVT_BUTTON, self.MergeButtonClick )
		self.m_button3.Bind( wx.EVT_BUTTON, self.ProbableButtonClick )
		self.m_button61.Bind( wx.EVT_BUTTON, self.Rootdistance )
		self.m_button8.Bind( wx.EVT_BUTTON, self.Pointdistance )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OpenfileButton( self, event ):
		event.Skip()
	
	def MergeButtonClick( self, event ):
		event.Skip()
	
	def ProbableButtonClick( self, event ):
		event.Skip()
	
	def Rootdistance( self, event ):
		event.Skip()
	
	def Pointdistance( self, event ):
		event.Skip()

﻿# -*- coding: utf-8 -*-  
import os
import re
import wx
import locale
import newick_GUI
import webbrowser
from Bio import Phylo

# file: practice_main.py
# import practice.py, which was generated by wxFB
import merge
import probable_newick as p_n
import distance_node_and_root_newick as d_n

class Practice(newick_GUI.MyFrame1):

	def __init__(self, parent): 	
		locale.setlocale(locale.LC_ALL, 'C')
		newick_GUI.MyFrame1.__init__(self, parent)
		self.path = ""

	def OpenfileButton(self, event):
		openFileDialog = wx.FileDialog(self, "Open", "", "", "Newick files (*.nwk)|*.nwk", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		openFileDialog.ShowModal()		
		self.path = openFileDialog.GetPath()

		if self.path != "":
			st = self.path.rfind("/") + 1
			self.m_staticText161.SetForegroundColour((0, 100, 0))
			self.m_staticText161.SetLabel(self.path[st :])			
			self.m_staticText16.SetLabel(u"成功匯入檔案！")

	def explanation( self, event ):
		url = "https://drive.google.com/uc?export=download&id=0B3kYqO3jdS2CT0RBak9KNHdDeVU"
		webbrowser.open(url)

	def MergeButtonClick( self, event ):
		st = int(self.merge_st.GetValue())
		ed = int(self.merge_ed.GetValue())
		if st < 0:
			self.m_staticText16.SetForegroundColour((255, 0, 0))
			self.m_staticText16.SetLabel(u"起始值僅可輸入大於 0 的數值！")
		elif ed < 0:
			self.m_staticText16.SetForegroundColour((255, 0, 0))
			self.m_staticText16.SetLabel(u"結束值僅可輸入大於 0 的數值！")
		elif st > ed:
			self.m_staticText16.SetForegroundColour((255, 0, 0))
			self.m_staticText16.SetLabel(u"匹配起始值不可大於結束值！")
		else:
			self.m_staticText16.SetForegroundColour((0, 0, 0))
			self.m_staticText16.SetLabel(u"合併中 . . .")
			merge.merge_br(self.path, int(st), int(ed))

			tree = Phylo.read(r"output/merge_output.nwk",  "newick")
			Phylo.draw(tree, branch_labels=lambda c: c.branch_length)
			self.m_staticText16.SetLabel(u"合併成功！")
		
	def ProbableButtonClick( self, event ):
		value = float(self.value.GetValue())
		if value < 0 or value > 1:
			self.m_staticText16.SetForegroundColour((255, 0, 0))
			self.m_staticText16.SetLabel(u"門檻值僅可介在 0 和 1 之間！")
		else:
			self.m_staticText16.SetForegroundColour((0, 0, 0))
			self.m_staticText16.SetLabel(u"分群中 . . .")
			p_n.probable(self.path, value)

			tree = Phylo.read(r"output/probable_output.nwk",  "newick")
			Phylo.draw(tree, branch_labels=lambda c: c.branch_length)
			self.m_staticText16.SetLabel(u"分群成功！")

	def Rootdistance( self, event ):		
		distance = self.m_textCtrl9.GetValue()
		if int(distance) < 0:
			self.m_staticText16.SetForegroundColour((255, 0, 0))
			self.m_staticText16.SetLabel(u"門檻值僅可輸入大於 0 的數值！")
		else:
			self.m_staticText16.SetForegroundColour((0, 0, 0))
			self.m_staticText16.SetLabel(u"篩選中 . . .")
			d_n.Filterdistance(self.path, "root", distance)

			self.m_staticText16.SetLabel(u"篩選成功！")
	
	def Pointdistance( self, event ):
		distance = self.m_textCtrl12.GetValue()
		node = self.m_textCtrl10.GetValue()
		if int(distance) < 0:
			self.m_staticText16.SetForegroundColour((255, 0, 0))
			self.m_staticText16.SetLabel(u"門檻值僅可輸入大於 0 的數值！")
		else:
			self.m_staticText16.SetForegroundColour((0, 0, 0))
			self.m_staticText16.SetLabel(u"篩選中 . . .")
			d_n.Filterdistance(self.path, node, distance)

			self.m_staticText16.SetLabel(u"篩選成功！")
	
class EventTriggerMain(wx.App):
	
	def OnInit(self):
		self.m_frame = Practice(None)
		self.m_frame.Show()
		return True

app = EventTriggerMain()
app.MainLoop()
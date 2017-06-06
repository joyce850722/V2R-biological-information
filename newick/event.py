﻿ # -*- coding: utf-8 -*-  
# file: practice_main.py
# import practice.py, which was generated by wxFB

import os
import wx
import locale
import newick_GUI
import merge
import probable_newick as p_n
import distance_node_and_root_newick as d_n

class Practice(newick_GUI.MyFrame1):

	def __init__(self, parent): 	
		locale.setlocale(locale.LC_ALL, 'C')    #區域設置
		newick_GUI.MyFrame1.__init__(self, parent)
		self.path = ""  #檔案路徑

	def OpenfileButton(self, event):
		openFileDialog = wx.FileDialog(self, "Open", "", "", "Newick files (*.nwk)|*.nwk", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		openFileDialog.ShowModal()		
		self.path = openFileDialog.GetPath()

		#tree = Phylo.read(self.path, "newick")
		#Phylo.draw(tree, branch_labels=lambda c: c.branch_length)		
		
	def MergeButtonClick( self, event ):
		st = int(self.merge_st.GetValue())
		ed = int(self.merge_ed.GetValue())
		merge.merge_br(self.path, st, ed)
		
	def ProbableButtonClick( self, event ):		
		value = float(self.value.GetValue())
		p_n.probable(self.path, value)

	def Rootdistance( self, event ):		
		distance = self.m_textCtrl9.GetValue()
		d_n.Filterdistance(self.path, "root", distance)
	
	def Pointdistance( self, event ):
		node = self.m_textCtrl10.GetValue()
		distance = self.m_textCtrl12.GetValue()
		d_n.Filterdistance(self.path, node, distance)
	
class EventTriggerMain(wx.App):
	
	def OnInit(self):
		self.m_frame = Practice(None)
		self.m_frame.Show()
		return True

app = EventTriggerMain()
app.MainLoop()
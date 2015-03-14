#!/usr/bin/env python

import os
import sys
from util import IconCreator
from util import FolderInformation
import config

try:
	import pygtk
	pygtk.require("2.0")
except:
	pass
try:
	import gtk
	import gtk.glade
except:
	sys.exit(1)

class MainWindow:
	def __init__(self):
		self.gladeFile = config.packageDir + "colorcode.glade"
		self.wTree = gtk.glade.XML( self.gladeFile )

		self.window = self.wTree.get_widget( "colorselectiondialog" )
		if( self.window ):
			self.window.connect( "destroy", gtk.main_quit )

		self.wTree.signal_autoconnect( self )

	def on_ok_clicked(self, item):
		cso = self.wTree.get_widget( "colorsel-color_selection1" )
		colorObject = cso.get_current_color()
		colorString = colorObject.to_string()
		color = colorString.split('#')[1]
		self.colorSelected = color[0] + color[1] + color[4] + color[5] + color[8] + color[9]
		gtk.main_quit()

	def on_cancel_clicked(self, item):
		exit()
	
	def on_help_clicked(self, item):
		print 'help'

	def run(self, folderPath):
		gtk.main()	
	
		try:
			color = self.colorSelected
		except Exception, e:
			exit()	

		fi = FolderInformation( folderPath )
		icon = fi.getIcon()

		ic = IconCreator( icon, color )
		nIcon = ic.createIcon()

		fi.setIcon( nIcon )
	

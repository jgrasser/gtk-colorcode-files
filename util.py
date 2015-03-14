#!/usr/bin/python
import os, string
import config

class IconCreator:
	#pass in filepaths please
	def __init__( self, existingIcon, color):
		self.original = existingIcon
		self.color = color

	def setColor( self, color ):
		self.color = color

	def createIcon( self ):
		if( len( self.color ) == 0 ):
			raise Exception( "No color set!");
		else:
			colorList = self.getColorList( self.original )
			#filter out black and white and grey colors
			bwgList = self.filterOutBlackWhiteGrey( colorList )
			#if no colors, dealing with greyscale icon, restore to origanal list
			if( len( colorList ) == 0 ):
				colorList = bwgList
			
			#change colors to new color
			commandList = []
			#create sed commands
			commandList.append("sed s/#" + colorList[0] + "/#" + self.color + "/ " + self.original)
			for x in range(1, len( colorList ) ):
				commandList.append("sed s/#" + colorList[x] + "/#" + self.color + "/ ")
		
			#string then together
			command = commandList[0]
			for x in range(1, len( commandList ) ):
				command += " | "  + commandList[x]
		
			#needs to change
			filesaved = config.saveDirectory + self.color + '.svg'
			command += " > " + filesaved
			os.popen( command )
		
			return filesaved

	def getColorList(self, filename):
		command = "awk -F'#' '/:#/ {color = substr($2, 0, 6); print color }' " + filename
		pipe = os.popen( command )
		result = pipe.read()
		colorList = string.rsplit( result, '\n' )
		#Remove empty string at end	
		colorList.pop()
		return colorList

	def filterOutBlackWhiteGrey(self, colorList ):
		removeList = []
		for color in colorList:
			searchString = color[0] + color[1]
			n = color.count( searchString )
			if( n == 3 ):
				removeList.append( color )
	
		for color in removeList:
			colorList.remove( color )
		
		return removeList


class FolderInformation:
	def __init__(self, f):
		self.folder = f
		pipe = os.popen( 'gvfs-info ' + f )
		self.metadata = pipe.read()
		pipe.close()

	def getFolder(self):
		return self.folder

	def getMetadata(self):
		return self.metadata

	def getIcon( self ):
		iconTheme = self.getIconTheme()
		#checkGlobalDir
		iconFile = ''
		exceptionList = []
	
 		try:
			iconFile = self.checkGobalDirectory( iconTheme )
		except Exception, e:
			exceptionList.append(e)
	
		try:
			iconFile = self.checkLocalDirectory( iconTheme )
		except Exception, e:
			exceptionList.append(e)
	
		if( self.fileNotFound( exceptionList ) == 0 ):
			iconFile = config.defaultIconFile
	
		print "Using icon at: " + iconFile
		return iconFile

	def fileNotFound( self, exceptionList ):
		if( len( exceptionList ) == 2 ):
			return 0
		else:
			return 1

	def getIconTheme(self):
		pipe = os.popen( 'gconftool-2 --get /desktop/gnome/interface/icon_theme' )
		theme = pipe.read()
		#strip off \n char at end
		return theme.__getslice__( 0, len( theme ) - 1 )
	
	def checkGobalDirectory(self, iconTheme ):
		iconFile = config.globalIconDirectory + iconTheme + '/' + config.defaultIcon
		if( not os.path.exists( iconFile ) ):
			raise Exception( "Not in global dir: " + iconFile )
		else:
			return iconFile
	
	def checkLocalDirectory(self, iconTheme ):
		iconFile = config.localIconDirectory + iconTheme + '/' + config.defaultIcon
		if( not os.path.exists( iconFile ) ):
			raise Exception( "Not in local dir: " + iconFile )
		else:
			return iconFile
	
	def setIcon(self, icon):
		command = 'gvfs-set-attribute -t string \'' + self.folder + '\' metadata::custom-icon file:///' + icon
		os.system( command )
		


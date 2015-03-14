import os

packageDir = '/usr/share/pyshared/colorcode/'
#packageDir = '/media/DEIMOS/colorcode/'
VERSION = '1.0.0'

#important directories
globalIconDirectory = '/usr/share/icons/'
localIconDirectory = '/home/' + os.getenv( "USERNAME") + '/.icons/'
saveDirectory = '/home/' + os.getenv("USERNAME") + '/.colorcode/'

#default values
defaultIcon = 'folder.svg'
defaultSize = '48'
defaultFolderTheme = 'Humanity'
defaultIconFile = '/usr/share/icons/Humanity/places/48/folder.svg'




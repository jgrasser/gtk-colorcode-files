import sys
sys.path.insert(0, '/usr/share/pyshared/colorcode')
from app import MainWindow

import os
import urllib

import nautilus
import gconf

class ColorcodeExtension(nautilus.MenuProvider):
    def __init__(self):
        pass
        
    def runColorcode(self, file):
        filename = urllib.unquote(file.get_uri()[7:])
        app = MainWindow()
        app.run( filename )
        
    def menu_activate_cb(self, menu, file):
        self.runColorcode(file)
       
    def get_file_items(self, window, files):
        if len(files) != 1:
            return
        
        file = files[0]
        if not file.is_directory() or file.get_uri_scheme() != 'file':
            return
        
        item = nautilus.MenuItem('NautilusPython::colorcode_file_item',
                                 'Colorcode...' ,
                                 'Colorcode... %s' % file.get_name())
        item.connect('activate', self.menu_activate_cb, file)
        return item,

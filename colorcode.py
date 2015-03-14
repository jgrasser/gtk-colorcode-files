#! /usr/bin/python -OOt

import sys
import config
from app import MainWindow

def main():
        try:
                #from Alacarte import config
                datadir = config.packageDir
                version = config.VERSION
        except:
                datadir = '.'
                version = '0.9'
        app = MainWindow()
        app.run( sys.argv[1] )

if __name__ == '__main__':
        main()


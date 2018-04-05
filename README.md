# GrabFromInsta
A tiny library capable of parsing an Instagram url and returning the url of the picture.
It uses urllib to grab the HTML code and then parses it.
This repo also contains a CLI and a GUI implementation of the library.
All written in python3.
Usage:
import grabfrominsta as gfi
from urllib import request
a = gfi.grabfrominsta(url)
request.urlretreive(a,path)


Or simply use the GUI/CLI interface

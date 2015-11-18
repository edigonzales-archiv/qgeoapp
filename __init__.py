from QGeoApp import QGeoApp
from PyQt4.QtCore import *
import os

def name(): 
    return "QGeoApp" 

def description():
    return QCoreApplication.translate("init","Framework for applications modules")

def version(): 
    return "Version 0.0.1" 

def qgisMinimumVersion():
    return "1.8"
    
def icon():
	return "qgeoapp.png"    

def classFactory(iface): 
    return QGeoApp(iface, name(), version())



 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

from doCreateDifferenceLayer import CreateDifferenceDialog

class ComplexCheck(QObject):

    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
    
    def run(self):     
        dlg = CreateDifferenceDialog(self.iface.mainWindow())
        dlg.initGui()
        dlg.show()

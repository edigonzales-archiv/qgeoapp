 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import os, time
from qgeoapp.basic.tools.qgeoapputils import QGeoAppUtils


class ComplexCheck(QObject):

    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.qutils = QGeoAppUtils()

    def run(self):        
        try:
            _temp = __import__("perimeterrand_maengel", globals(), locals(), ['ComplexCheck'])
            c = _temp.ComplexCheck(self.iface)
            c.run()
   
            _temp = __import__("perimeterrand_checklayer", globals(), locals(), ['ComplexCheck'])
            c = _temp.ComplexCheck(self.iface)
            c.run()
   
        except:
            QMessageBox.critical(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Error loading all complex checks."))




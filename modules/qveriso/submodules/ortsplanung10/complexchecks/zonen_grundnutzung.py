 # -*- coding: utf8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import os, time
from qgeoapp.basic.tools.qgeoapputils import QGeoAppUtils


class ComplexCheck(QObject):

    def __init__(self, iface, projectId, submodule):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.projectId = projectId
        self.submodule = submodule
        self.qutils = QGeoAppUtils()

    def run(self):        
        group = "Zonen_Grundnutzung" + " (" + str(self.projectId) + ")"
        table = {}
        table["type"] = "postgres"
        table["title"] = "Zonengrundnutzung"
        table["featuretype"] = "zonen_grundnutzung_zone_grundng"
        table["geom"] = "geometrie"
        table["key"] = "ogc_fid"            
        table["sql"] = ""
        table["readonly"] = "true"
        table["group"] = group
        table["style"] = "tseinteilung/toleranzstufe.qml"

        self.qutils.loadLayer(self.iface, table, None, "/python/plugins/qgeoapp/modules/qveriso/submodules/" + self.submodule + "/qml/")       

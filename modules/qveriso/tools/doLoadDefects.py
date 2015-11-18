# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import time, os
from qgeoapp.basic.tools.qgeoapputils import QGeoAppUtils


class LoadDefects(QObject):
    def __init__(self, iface, projectId, submodule):
        self.iface = iface
        self.projectId = projectId
        self.submodule = submodule
        self.qutils = QGeoAppUtils()

        
    def run(self):
        table = {}
        table["type"] = "postgres"
        table["title"] = u"Maengelliste"
        table["featuretype"] = "maengel"
        table["geom"] = "the_geom"
        table["key"] = "ogc_fid"
        table["readonly"] = "false"
        table["group"] = u"Mängel" + " (" + self.projectId + ")"
        table["style"] = "maengel.qml"
        
        
        vlayer = self.qutils.loadLayer(self.iface, table, None, "/python/plugins/qgeoapp/modules/qveriso/submodules/" + self.submodule + "/qml/")
        vlayer.setLayerName(u"Mängelliste")
        form = QDir.convertSeparators(QDir.cleanPath( QgsApplication.qgisSettingsDirPath() + '/python/plugins/qgeoapp/modules/qveriso/submodules/'+ self.submodule +'/defects/maengelForm.ui' ))
        vlayer.setEditForm(form)
        vlayer.setEditFormInit( "qgeoapp.modules.qveriso.submodules."+self.submodule+".defects.maengelFormInit.featureFormInit" )


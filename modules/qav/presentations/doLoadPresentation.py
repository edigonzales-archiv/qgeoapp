 # -*- coding: utf8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgeoapp.basic.tools.qgeoapputils import *

import os, json, time, sys


class LoadPresentation(QObject):
    
    def __init__(self, iface, presentation):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        
        self.presentation = presentation

        self.settings = QSettings("CatAIS","QGeoApp")
        self.ili = str(self.settings.value("project/active/ili").toString())
        self.moduleName = str(self.settings.value("project/active/module").toString())
        
        self.storagetype = str(self.settings.value("project/active/storagetype").toString())
        self.dbhost = str(self.settings.value("project/active/host").toString())
        self.dbport = str(self.settings.value("project/active/port").toString())
        self.dbname = str(self.settings.value("project/active/dbname").toString())
        self.dbschema = str(self.settings.value("project/active/schema").toString())
        self.dbuser = str(self.settings.value("project/active/readuser").toString())
        self.dbpwd = str(self.settings.value("project/active/readpwd").toString())
        self.dbadmin = str(self.settings.value("project/active/writeuser").toString())
        self.dbadminpwd = str(self.settings.value("project/active/writepwd").toString())
    
    def run(self):
        # read chosen presentation informations
        presentationFile = self.presentation["file"]
        groupName = self.presentation["displayname"]
        
        layers = {}
        filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/modules/"+self.moduleName.lower()+"/models/"+self.ili.lower()+"/config/presentations/"+presentationFile))

        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            layers = json.load(open(filename)) 
        except:
            QApplication.restoreOverrideCursor()
            message = sys.exc_info()[0]                        
            QMessageBox.critical(None, "QGeoAppModule.QAV",  QCoreApplication.translate("QGeoAppModule.QAV", "Error processing: ") + str(filename) + "\n\n" + str(message))
            return None
        QApplication.restoreOverrideCursor()
        
        # add the layers to the map canvas
        parentGroupName = "Amtliche Vermessung"
        for layer in layers["featuretypes"]:
            QGeoAppUtils().loadLayer(self.iface, layer, parentGroupName)
            



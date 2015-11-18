 # -*- coding: utf8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import os, json, time, sys


class QGeoAppModule(QObject):
    
    def __init__(self, iface, toolBar):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        
        self.toolBar = toolBar
        
        self.settings = QSettings("CatAIS","QGeoApp")
        self.ili = str(self.settings.value("project/active/ili").toString())
        self.moduleName = str(self.settings.value("project/active/module").toString())

        self.DEBUG = True
        
    def initGui(self):
        try:
            # read the presentations file with all the available presentations
            presentations = self.doReadPresentationsFile()
            
            # adjust toolbar
            actions = self.toolBar.actions()
            for action in actions:
                try:
                    objectName = action.defaultWidget().objectName()
                    # delete existing module menus
                    if objectName[0:13] == "QGeoAppModule":
                        self.toolBar.removeAction(action)
                    # remember the action where we want to insert our new menu 
                    # (e.g. settings menu bar)
                    if objectName == "QGeoApp.Main.SettingsMenuBar":
                        self.beforeAction = action
                except AttributeError:
                    pass
                
            # and now add our module specific menubars
            # presentation
            menuBarPresentation = QMenuBar(self.toolBar)
            menuBarPresentation.setObjectName("QGeoAppModule.QAV.PresentationsMenuBar")        
            menuBarPresentation.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
            menuPresentation = QMenu(menuBarPresentation)
            menuPresentation.setTitle(QCoreApplication.translate( "QGeoAppModule.QAV","Presentation"))        
            
            if presentations != None:
                for presentation in presentations["presentations"]:
                    action = QAction(QCoreApplication.translate("QGeoAppModule.QAV", unicode(presentation["displayname"])), self.iface.mainWindow())
                    menuPresentation.addAction(action)
                    QObject.connect(action, SIGNAL( "triggered()"), lambda activePresentation=presentation: self.doLoadPresentation(activePresentation))

            menuBarPresentation.addMenu(menuPresentation)
            self.toolBar.insertWidget(self.beforeAction, menuBarPresentation)

        except:
            message = sys.exc_info()[0]
            QMessageBox.critical(None, "QGeoAppModule.QAV", str(message))


    def doReadPresentationsFile(self):
        presentations = {}
        filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/modules/"+self.moduleName.lower()+"/models/"+self.ili.lower()+"/config/presentations/index.json"))

        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            presentations = json.load(open(filename)) 
        except:
            QApplication.restoreOverrideCursor()
            message = sys.exc_info()[0]                        
            QMessageBox.critical(None, "QGeoAppModule.QAV",  QCoreApplication.translate("QGeoAppModule.QAV", "Error processing: ") + str(filename) + "\n\n" + str(message))
            return None
        QApplication.restoreOverrideCursor()
        return presentations


    def doLoadPresentation(self, presentation):
        from presentations.doLoadPresentation import LoadPresentation
        d = LoadPresentation(self.iface, presentation)
        d.run()


        
    def run(self):
        print "fooooooooooo"

        
        



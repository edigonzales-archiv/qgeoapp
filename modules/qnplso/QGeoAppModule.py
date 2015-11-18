 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import os, json, time, sys
#from tools.doShowChecklist import ShowChecklist
#from tools.doLoadDefects import LoadDefects
#from tools.doExportDefects import ExportDefects
#from tools.qverisoutils import QVerisoUtils
from qgeoapp.basic.tools.qgeoapputils import QGeoAppUtils


class QGeoAppModule(QObject):
    
    def __init__(self, iface, toolBar):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.toolBar = toolBar
        self.utils = QGeoAppUtils()
        
        self.settings = QSettings("CatAIS","QGeoApp")
        self.projectsRootPath = self.settings.value("projects/rootdir").toString()
        self.projectId = str(self.settings.value("project/active/id").toString())
        self.ili = str(self.settings.value("project/active/ili").toString())
        self.moduleName = str(self.settings.value("project/active/module").toString())
        self.subModuleName = str(self.settings.value("project/active/submodule").toString())
        
        self.dbhost = str(self.settings.value("project/active/host").toString())
        self.dbport = str(self.settings.value("project/active/port").toString())
        self.dbname = str(self.settings.value("project/active/dbname").toString())
        self.dbschema = str(self.settings.value("project/active/schema").toString())
        self.dbuser = str(self.settings.value("project/active/readuser").toString())
        self.dbpwd = str(self.settings.value("project/active/readpwd").toString())
        self.dbadmin = str(self.settings.value("project/active/writeuser").toString())
        self.dbadminpwd = str(self.settings.value("project/active/writepwd").toString())

        self.DEBUG = True
        
    def initGui(self):
        # remove all the applications module specific menus
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
                # get settings menu bar for module specific settings
                if objectName == "QGeoApp.Main.SettingsMenuBar":
                    self.settingsAction = action
            except AttributeError:
                pass
                
        # remove all the application module specific options/settings in the settings menu
        settingsMenuBar = self.settingsAction.defaultWidget()
        settingsMenu = self.settingsAction.defaultWidget().actions()[0].parentWidget()
        
        actions = settingsMenu.actions()
        for action in actions:
            objectName = action.objectName()
            if objectName[0:13] == "QGeoAppModule":
               settingsMenu.removeAction(action) 
            
            if action.isSeparator() == True:
                settingsMenu.removeAction(action)
            
        # add all the application module specific options/settings in the settings menu
        settingsMenu.addSeparator()
        
        action = QAction(QCoreApplication.translate("QGeoAppModule.QNPLSO", "Additional databases"), self.iface.mainWindow())
        action.setObjectName("QGeoAppModule.QNPLSO.DatabaseSpatiaLite")
        QObject.connect(action, SIGNAL("triggered()"), lambda foo="bar":  self.doSetDatabase(foo))        

        settingsMenu.addActions([action])     


    def doSetDatabase(self, foo):
        print "baaaar"
        from settings.doSetDatabase import SetDatabaseDialog
        d = SetDatabaseDialog(self.iface.mainWindow())        
        d.initGui()
        d.show()

            
        # and now add our module specific menus
#        self.doInitChecksLoader()
#        self.doInitDefectsLoader()
#        self.doInitTopicsTableLoader()
#        self.doInitBaseLayerLoader()


#    def doInitDefectsLoader(self):
#        menuBar = QMenuBar(self.toolBar)
#        menuBar.setObjectName("QGeoAppModule.QVeriso.LoadDefectsMenuBar")        
#        menuBar.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
#        menu = QMenu(menuBar)
#        menu.setTitle(QCoreApplication.translate( "QGeoAppModule.QVeriso","Defects"))  
#
#        action = QAction(QCoreApplication.translate("QGeoAppModule.QVeriso", "Load defects layer"), self.iface.mainWindow())
#        QObject.connect(action, SIGNAL( "triggered()"), lambda foo="bar": self.doLoadDefects(foo))
#        menu.addAction(action)     
#        
#        action = QAction(QCoreApplication.translate("QGeoAppModule.QVeriso", "Export defects layer"), self.iface.mainWindow())
#        QObject.connect(action, SIGNAL( "triggered()"), lambda foo="bar": self.doExportDefects(foo))
#        menu.addAction(action)     
#
#        menuBar.addMenu(menu)
#        self.toolBar.insertWidget(self.beforeAction, menuBar)
#
#
#    def doLoadDefects(self, foo):
#        d = LoadDefects(self.iface, self.projectId, self.subModuleName)
#        d.run()
#
#        
#    def doExportDefects(self, foo):
#        d = ExportDefects(self.iface)
#        d.run()
#
#
#    def doInitChecksLoader(self):
#        menuBar = QMenuBar(self.toolBar)
#        menuBar.setObjectName("QGeoAppModule.QVeriso.LoadChecksMenuBar")        
#        menuBar.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
#        menu = QMenu(menuBar)
#        menu.setTitle(QCoreApplication.translate( "QGeoAppModule.QVeriso","Checks"))  
#        
#        # load checklist
#        action = QAction(QCoreApplication.translate("QGeoAppModule.QVeriso", "Load checklist"), self.iface.mainWindow())
#        QObject.connect(action, SIGNAL( "triggered()"), lambda foo="bar": self.doLoadChecklist(foo))
#        menu.addAction(action)     
#
#        menu.addSeparator()
#        
#        # load checks
#        checkTopics = self.vutils.getCheckTopicsName(self.subModuleName)
#
#        try:
#            for checkTopic in checkTopics:
#                singleCheckMenu = menu.addMenu(unicode(checkTopic))   
#                checks = self.vutils.getChecks(self.subModuleName, checkTopic)
#                for check in checks:
#                    action = QAction(check["title"], self.iface.mainWindow())
#                    try:
#                        shortcut = check["shortcut"]
#                        action.setShortcut(shortcut)
#                    except:
#                        pass
#                    singleCheckMenu.addAction(action)                            
#                    if check["type"] == "simple":
#                        QObject.connect(action, SIGNAL( "triggered()"), lambda simpleCheck=check: self.doShowSimpleCheck(simpleCheck))
#                    elif check["type"] == "complex":
#                        QObject.connect(action, SIGNAL( "triggered()"), lambda complexCheck=check: self.doShowComplexCheck(complexCheck))
#        except:
#            print "No checks defined."
#            #messagebox
#            
#        menuBar.addMenu(menu)
#        self.toolBar.insertWidget(self.beforeAction, menuBar)
#        
#    
#    def doShowSimpleCheck(self, check):
#        print "simpleCheck"
#        
#        
#    def doShowComplexCheck(self, check):
#        try:
#            module = str(check["file"])
#            print module
#            _temp = __import__("submodules." + self.subModuleName+ "." + module, globals(), locals(), ['ComplexCheck'])
#            c = _temp.ComplexCheck(self.iface, self.projectId, self.subModuleName)
#            c.run()
#        except:
#            print "error loading complex check"
#           #messagebox
#                
#    
#    def doLoadChecklist(self, foo):
#        d = ShowChecklist(self.iface, self.projectId, self.projectsRootPath, self.subModuleName)
#        d.run()        
#
#
#    def doInitBaseLayerLoader(self):
#        menuBar = QMenuBar(self.toolBar)
#        menuBar.setObjectName("QGeoAppModule.QVeriso.LoadBaseLayersMenuBar")        
#        menuBar.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
#        menu = QMenu(menuBar)
#        menu.setTitle(QCoreApplication.translate( "QGeoAppModule.QVeriso","Baselayer"))        
#
#        #add the baselayers
#        baselayers = self.vutils.getBaselayers(self.subModuleName)
#        try:
#            for baselayer in baselayers:
#                action = QAction(unicode(baselayer["title"]), self.iface.mainWindow())
#                menu.addAction(action)
#                QObject.connect(action, SIGNAL( "triggered()" ), lambda layer=baselayer: self.doShowBaseLayer(layer))
#        except:
#            print "no baselayers found"
#            #messagebox
#
#        menuBar.addMenu(menu)
#        self.toolBar.insertWidget(self.beforeAction, menuBar)
#
#
#    def doShowBaseLayer(self, layer):
#        print "showbaselayer"
#        QApplication.setOverrideCursor(Qt.WaitCursor)
#        try:           
#            layer["group"] = "Baselayers"
#            self.qutils.loadLayer(self.iface, layer, None, "/python/plugins/qgeoapp/modules/qveriso/submodules/" + self.subModuleName + "/qml/")       
#        except:        
#            print "error adding baselayer"         
#            QApplication.restoreOverrideCursor()
#        QApplication.restoreOverrideCursor()
#
#
#    def doInitTopicsTableLoader(self):
#        menuBar = QMenuBar(self.toolBar)
#        menuBar.setObjectName("QGeoAppModule.QVeriso.LoadTopicsTablesMenuBar")        
#        menuBar.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
#        menu = QMenu(menuBar)
#        menu.setTitle(QCoreApplication.translate( "QGeoAppModule.QVeriso","Data"))        
#
#        # add the topic menus
#        topics = self.vutils.getTopics(self.subModuleName)
#        try:
#            for topic in topics:
#                singleTopicMenu = menu.addMenu(unicode(topic['title']))   
#                action = QAction( QCoreApplication.translate("QGeoAppModule.QVeriso", "Load topic"), self.iface.mainWindow() )
#                singleTopicMenu.addAction(action)    
#                singleTopicMenu.addSeparator()      
#                QObject.connect(action, SIGNAL("triggered()"), lambda topic=topic: self.doShowTopic(topic))                   
#                for table in topic["tables"]:
#                    action = QAction(unicode(table["title"]), self.iface.mainWindow())
#                    singleTopicMenu.addAction(action)     
#                    QObject.connect( action, SIGNAL( "triggered()" ), lambda layer=table: self.doShowSingleTopicLayer(layer) )    
#        except:
#            print "No topics found."
#            #messagebox
#
#        menuBar.addMenu(menu)
#        self.toolBar.insertWidget(self.beforeAction, menuBar)
#
#
#    def doShowTopic(self, topic):
#        tables = topic["tables"]
#        n = len(tables)
#        for i in reversed(xrange(0, n)):
#            QApplication.setOverrideCursor(Qt.WaitCursor)                    
#            try:
#                tables[i]["group"] =  tables[i]["group"] + " (" + str(self.dbschema) + ")"
#                self.qutils.loadLayer(self.iface, tables[i], None, "/python/plugins/qgeoapp/modules/qveriso/submodules/" + self.subModuleName + "/qml/")   
#            except:
#                QApplication.setOverrideCursor(Qt.WaitCursor)        
#            QApplication.restoreOverrideCursor()
#
#        
#    def doShowSingleTopicLayer(self, layer):
#        QApplication.setOverrideCursor(Qt.WaitCursor)          
#        try:
#            layer["group"] =  layer["group"] + " (" + str(self.dbschema) + ")"
#            self.qutils.loadLayer(self.iface, layer, None, "/python/plugins/qgeoapp/modules/qveriso/submodules/" + self.subModuleName + "/qml/")       
#        except:        
#            QApplication.restoreOverrideCursor()
#        QApplication.restoreOverrideCursor()


    def run(self):
        print "fooooooooooo"

        
        



# -*- coding: utf-8 -*-
#---------------------------------------------------------------------
# 
# QGeoApp - Framework for application modules
#
# Copyright (C) 2012 Stefan Ziegler
#
# EMAIL: stefan.ziegler (at) bd.so.ch
# WEB  : www.catais.org
#
#---------------------------------------------------------------------
# 
# licensed under the terms of GNU GPL 2
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# 
#---------------------------------------------------------------------

## Import the PyQt and the QGIS libraries.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtXml
from qgis.core import *
from qgis.gui import *

from datetime import datetime, date, time
import os, sys, time, math, locale

import resources

class QGeoApp: 
    def __init__(self, iface, pluginName, version):
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.pluginName = pluginName
        self.version = version

        self.settings = QSettings("CatAIS","QGeoApp")

        self.DEBUG = True

        # Initialise the translation environment.
        userPluginPath = QFileInfo(QgsApplication.qgisUserDbFilePath()).path()+"/python/plugins/qgeoapp"  
        systemPluginPath = QgsApplication.prefixPath()+"/share/qgis/python/plugins/qgeoapp"
        locale = QSettings().value("locale/userLocale").toString()
        myLocale = locale[0:2]       
    
        if QFileInfo(userPluginPath).exists():
            pluginPath = userPluginPath+"/i18n/QGeoApp_"+myLocale+".qm"
        elif QFileInfo(systemPluginPath).exists():
            pluginPath = systemPluginPath+"/i18n/QGeoApp_"+myLocale+".qm"

        self.localePath = pluginPath
        if QFileInfo(self.localePath).exists():
            self.translator = QTranslator()
            self.translator.load(self.localePath)
          
            if qVersion() > '4.3.3':        
                QCoreApplication.installTranslator(self.translator)

        
    def initGui(self):  
        # create action that will start plugin configuration.    
        self.action = QAction(QIcon(":/plugins/qgeoapp/qgeoapp.png"), "Framwork for application modules", self.iface.mainWindow())
        QObject.connect(self.action, SIGNAL("triggered()"), self.run) 

        # add toolbar button and menu item.
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&QGeoApp", self.action)
        
        # create main toolbar
        self.toolBar = self.iface.addToolBar("QGeoApp Main Toolbar")
        #self.toolBar.setStyleSheet("QToolBar { background-color: rgba(0, 255, 0, 10%);}");
        self.toolBar.setObjectName("QGeoAppMainToolBar")
        self.toolBar.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
        
        # projects
        self.menuBarProjects = QMenuBar()
        #self.menuBarProjects.setStyleSheet("QMenuBar { { background-color: rgba(0, 0, 0, 0%);}");              
        self.menuBarProjects.setObjectName("QGeoApp.Main.ProjectsMenuBar")                
        self.menuBarProjects.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred))
        self.menuProjects = QMenu()
        #self.menuProjects.setStyleSheet("QMenu::item:title { background: blue; border: 1px solid black;}");                      
        self.menuProjects.setTitle(QCoreApplication.translate( "QGeoApp","Projects"))
        
        self.menuBarProjects.addMenu(self.menuProjects)
        
        # import/export
        self.menuBarImportExport = QMenuBar()
        self.menuBarImportExport.setObjectName("QGeoApp.Main.ImportExportMenuBar")        
        self.menuBarImportExport.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
        self.menuImportExport = QMenu()
        #self.menuImportExport.setPalette(QPalette(Qt.red));        
        self.menuImportExport.setTitle(QCoreApplication.translate( "QGeoApp","File"))
        
        self.importdata = QAction(QCoreApplication.translate("QGeoApp", "Import"), self.iface.mainWindow())
        QObject.connect(self.importdata, SIGNAL("triggered()"), self.doImportData)     
        
        self.exportdata = QAction(QCoreApplication.translate("QGeoApp", "Export"), self.iface.mainWindow())
        
        # does not work???!!!!
        self.menuImportExport.addSeparator()
        
        self.deleteproject = QAction(QCoreApplication.translate("QGeoApp", "Delete project"), self.iface.mainWindow())     
        QObject.connect(self.deleteproject, SIGNAL("triggered()"), self.doDeleteProject)             
        
        self.menuImportExport.addActions([self.importdata, self.deleteproject])
        self.menuBarImportExport.addMenu(self.menuImportExport)        
        
        # settings
        self.menuBarSettings = QMenuBar()
        self.menuBarSettings.setObjectName("QGeoApp.Main.SettingsMenuBar")
        self.menuBarSettings.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))        
        self.menuSettings = QMenu()
        self.menuSettings.setTitle(QCoreApplication.translate( "QGeoApp","Settings"))
        
        self.options = QAction(QCoreApplication.translate("QGeoApp", "Options"), self.iface.mainWindow())
        QObject.connect(self.options, SIGNAL("triggered()"), self.doOptions)     
        
        self.menuSettings.addActions([self.options])
        self.menuBarSettings.addMenu(self.menuSettings)
        
        # help
        self.menuBarHelp = QMenuBar()
        self.menuBarHelp.setObjectName("QGeoApp.Main.HelpMenuBar")
        self.menuBarHelp.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))                
        self.menuHelp = QMenu()
        self.menuHelp.setTitle(QCoreApplication.translate( "QGeoApp","Help"))
        
        self.about = QAction(QCoreApplication.translate("QGeoApp", "About"), self.iface.mainWindow())
        QObject.connect(self.about, SIGNAL("triggered()"), self.doAbout)        
        
        self.menuHelp.addActions([self.about])
        self.menuBarHelp.addMenu(self.menuHelp)

        # add menus to toolbar
        self.toolBar.addWidget(self.menuBarProjects)  
        self.toolBar.addWidget(self.menuBarImportExport)        
        self.toolBar.addWidget(self.menuBarSettings)
        self.toolBar.addWidget(self.menuBarHelp)
        
        # initial load of project menu entries
        self.doLoadProjectsFile()
    

    def doImportData(self):
        from basic.file.doImportData import ImportDataDialog
        self.import_dlg = ImportDataDialog(self.iface.mainWindow())
        self.import_dlg.initGui()
        self.import_dlg.show()
        QObject.connect(self.import_dlg, SIGNAL("projectsFileHasChanged()"), self.doLoadProjectsFile)           


    def doDeleteProject(self):
        from basic.file.doDeleteProject import DeleteProjectDialog
        self.del_dlg = DeleteProjectDialog(self.iface.mainWindow())
        ret = self.del_dlg.initGui()
        if ret <> False:            
            print "nicht flasch"
            self.del_dlg.show()
            QObject.connect(self.del_dlg, SIGNAL("projectsFileHasChanged()"), self.doLoadProjectsFile)           


    def doOptions(self):
        from basic.settings.doOptions import OptionsDialog
        self.opt_dlg = OptionsDialog(self.iface.mainWindow())
        self.opt_dlg.initGui()
        self.opt_dlg.show()
        QObject.connect(self.opt_dlg, SIGNAL("projectsFileHasChanged()"), self.doLoadProjectsFile)           

        
    def doAbout(self):
        from basic.help.doAbout import AboutDialog
        self.about_dlg = AboutDialog(self.iface.mainWindow(), self.version)
        self.about_dlg.show()
 

    def doLoadProjectsFile(self):
        from basic.projects.doLoadProjectsFile import LoadProjectsFile
        d = LoadProjectsFile()
        projects = d.read()
        
        if projects != None:
            groupedProjects = {}
            for project in projects:
                moduleName = project["appmodule"]
                try:
                    moduleList = groupedProjects[moduleName]
                except KeyError:
                    moduleList = []
                
                moduleList.append(project)
                groupedProjects[moduleName] = moduleList
            
            self.menuProjects.clear()
            for key in groupedProjects:
                modules = groupedProjects[key]
                groupMenu = self.menuProjects.addMenu(QCoreApplication.translate("QGeoApp", unicode(key)))
                sortedProjectsList = sorted(modules, key=lambda k: k['displayname']) 
                for project in sortedProjectsList:
                    action = QAction(QCoreApplication.translate("QGeoApp", unicode(project["displayname"])), self.iface.mainWindow())
                    groupMenu.addAction(action)
                    QObject.connect(action, SIGNAL( "triggered()"), lambda activeProject=project: self.doLoadProject(activeProject))


    def doLoadProject(self, project):
        # save the active project information to the settings
        self.settings.setValue("project/active/id", QVariant(str(project["id"])))
        self.settings.setValue("project/active/displayname", QVariant(str(project["displayname"])))
        self.settings.setValue("project/active/appmodule", QVariant(str(project["appmodule"])))
        try:
            self.settings.setValue("project/active/subappmodule", QVariant(str(project["subappmodule"])))
        except:
            self.settings.setValue("project/active/subappmodule", QVariant(str("")))
        self.settings.setValue("project/active/ilimodelname", QVariant(str(project["ilimodelname"])))
        self.settings.setValue("project/active/epsg", QVariant(str(project["epsg"])))
        self.settings.setValue("project/active/provider", QVariant(str(project["provider"])))
        self.settings.setValue("project/active/dbhost", QVariant(str(project["dbhost"])))
        self.settings.setValue("project/active/dbport", QVariant(str(project["dbport"])))
        self.settings.setValue("project/active/dbname", QVariant(str(project["dbname"])))
        self.settings.setValue("project/active/dbschema", QVariant(str(project["dbschema"])))
        self.settings.setValue("project/active/dbuser", QVariant(str(project["dbuser"])))
        self.settings.setValue("project/active/dbpwd", QVariant(str(project["dbpwd"])))
        self.settings.setValue("project/active/dbadmin", QVariant(str(project["dbadmin"])))
        self.settings.setValue("project/active/dbadminpwd", QVariant(str(project["dbadminpwd"])))
        self.settings.setValue("project/active/projectdir", QVariant(str(project["projectdir"])))

        # load application module
        moduleName = str(project["appmodule"]).lower()
#        try:
        _temp = __import__("modules." + moduleName + ".QGeoAppModule", globals(), locals(), ['QGeoAppModule'])
        c = _temp.QGeoAppModule(self.iface, self.toolBar)
        c.initGui()
#            c.run()            
#        except ImportError:
#            QMessageBox.critical(None, "QGeoApp",  QCoreApplication.translate("QGeoApp", "Module '" + moduleName + "' import error."))

        
    def unload(self):
        ## Remove the plugin menu item and icon.
        self.iface.removeToolBarIcon(self.action)        
        self.iface.mainWindow().removeToolBar(self.toolBar)
        
    
    def run(self): 
        print "TEST...."
        from basic.tools.qgeoapputils import QGeoAppUtils
        from basic.tools.QDiffLineSegments import QDiffLineSegments
        
        utils = QGeoAppUtils()
        vlayer1 = utils.getVectorLayerByName("poly1")
        vlayer2 = utils.getVectorLayerByName("poly2")
        print vlayer1.isValid()
        print vlayer2.isValid()
        
        diffs = QDiffLineSegments(self.iface, vlayer1, vlayer2)
        diffs.run()
        
        
        

# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from qgis.core import *
from qgis.gui import *
import os, json, sys, tempfile, time

from Ui_deleteproject import Ui_DeleteProject
from qgeoapp.basic.projects.doLoadProjectsFile import LoadProjectsFile

class DeleteProjectDialog(QDialog, Ui_DeleteProject):
  
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        self.okButton.setText("Delete")
        self.connect(self.okButton, SIGNAL("accepted()"), self.accept)
        
        # settings
        self.settings = QSettings("CatAIS","QGeoApp")
        self.projectsdatabase = self.settings.value("projects/database/path").toString()


    def initGui(self):     
        d = LoadProjectsFile()
        projects = d.read() 
 
        if projects == None:
            return False
        
        self.projects = projects
        sortedProjects = sorted(self.projects, key=lambda k: k['displayname']) 
    
        self.cBoxProject.clear()    
        for project in sortedProjects:
            self.cBoxProject.addItem(unicode(project["displayname"]), QVariant(project["dbschema"]))

        self.cBoxProject.insertItem(0, QCoreApplication.translate("QGeoApp", "Choose project...."), None)
        self.cBoxProject.setCurrentIndex(0)


    def accept(self):
        currIdx = self.cBoxProject.currentIndex()
        if currIdx == 0:
            return
        
        dbschema = str(self.cBoxProject.itemData(currIdx).toString())
        
        i = 0
        for project in self.projects:
            if dbschema ==  str(project["dbschema"]):                
                self.dbhost = str(project["dbhost"])
                self.dbname = str(project["dbname"])
                self.dbport = str(project["dbport"])
                self.dbschema = dbschema
                self.dbadmin = str(project["dbadmin"])
                self.dbadminpwd = str(project["dbadminpwd"])
                self.projectIndex = i
            i += 1
                 
        if self.dbhost == None or self.dbname == None or self.dbport == None or self.dbschema == None or self.dbadmin == None or self.dbadminpwd == None:
            QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Should not reach here!"))

        
        # delete geodata in db 
        db = QSqlDatabase.addDatabase("QPSQL", "PostgreSQL")
        db.setHostName(self.dbhost)
        db.setDatabaseName(self.dbname)
        db.setUserName(self.dbadmin)
        db.setPassword(self.dbadminpwd)
        try:
            db.setPort(int(self.dbport))
        except ValueError:
            QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Port is not a integer value."))            
            return
        
        if  db.open() == False:
            QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Could not open database:\n") + str(db.lastError().driverText()))            
            return
            
        sql = "BEGIN;"
        sql += "DROP SCHEMA IF EXISTS " + self.dbschema + " CASCADE;"
        sql += "DELETE FROM public.geometry_columns WHERE f_table_schema = '" + self.dbschema + "';"
        sql += "COMMIT;"
        
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.buttonBox.setEnabled(False)        
        try:
            query = db.exec_(sql)
            
            if query.isActive() == False:
                QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Error occured while deleting project."))            
                return
            
            db.close()
                
            # delete project entry in project database
            pdb = QSqlDatabase.addDatabase("QSQLITE", "Projectdatabase")
            pdb.setDatabaseName(self.projectsdatabase) 

            if  pdb.open() == False:
                QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Could not open projects database:\n") + str(pdb.lastError().driverText()))            
                return 
                
            sql = "DELETE FROM projects WHERE dbschema = '" + self.dbschema + "';"

            query = pdb.exec_(sql)
            
            if query.isActive() == False:
                QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Error occured while updating projects database."))            
                return 
            
            pdb.close()
            self.emit(SIGNAL("projectsFileHasChanged()"))
            self.initGui()
            
        except:
            QMessageBox.critical(None, "QGeoApp",  QCoreApplication.translate("QGeoApp", "Something went wrong while deleting project."))            
            QApplication.restoreOverrideCursor()        
            self.buttonBox.setEnabled(True)
            
        QApplication.restoreOverrideCursor()        
        self.buttonBox.setEnabled(True)
        QMessageBox.warning(None, "QGeoApp",  QCoreApplication.translate("QGeoApp", "Project deleted. Please remove project directory manually."))



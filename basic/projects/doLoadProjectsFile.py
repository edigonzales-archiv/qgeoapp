 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from qgis.core import *
from qgis.gui import *
import os, json


class LoadProjectsFile(QObject):
    
    def __init__(self):
        pass


    def read(self):                
        self.settings = QSettings("CatAIS","QGeoApp")
        filename = self.settings.value("projects/database/path").toString()
        
        if filename == "" or filename == None:
            QMessageBox.warning(None, "QGeoApp",  QCoreApplication.translate("QGeoApp", "No project database found."))
            return None
            
        self.projects = []
        
        try:
            self.db = QSqlDatabase.addDatabase("QSQLITE", "Projectdatabase")
            self.db.setDatabaseName(filename) 

            if  self.db.open() == False:
                QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Could not open database:\n") + str(self.db.lastError().driverText()))            
                return 

            sql = "SELECT * FROM projects;"

            query = self.db.exec_(sql)
            
            if query.isActive() == False:
                QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Error occured while fetching projects informations."))            
                return 

            record = query.record()
            while query.next():
                project = {}
                project["id"] = str(query.value(record.indexOf("id")).toString())
                project["displayname"] = str(query.value(record.indexOf("displayname")).toString())
                project["dbhost"] = str(query.value(record.indexOf("dbhost")).toString())
                project["dbname"] = str(query.value(record.indexOf("dbname")).toString())
                project["dbport"] = str(query.value(record.indexOf("dbport")).toString())
                project["dbschema"] = str(query.value(record.indexOf("dbschema")).toString())                
                project["dbuser"] = str(query.value(record.indexOf("dbuser")).toString())
                project["dbpwd"] = str(query.value(record.indexOf("dbpwd")).toString())
                project["dbadmin"] = str(query.value(record.indexOf("dbadmin")).toString())
                project["dbadminpwd"] = str(query.value(record.indexOf("dbadminpwd")).toString())
                project["provider"] = str(query.value(record.indexOf("provider")).toString())
                project["epsg"] = str(query.value(record.indexOf("epsg")).toString())
                project["ilimodelname"] = str(query.value(record.indexOf("ilimodelname")).toString())
                project["appmodule"] = str(query.value(record.indexOf("appmodule")).toString())
                project["subappmodule"] = str(query.value(record.indexOf("subappmodule")).toString())
                project["projectrootdir"] = str(query.value(record.indexOf("projectrootdir")).toString())
                project["projectdir"] = str(query.value(record.indexOf("projectdir")).toString())
                
                self.projects.append(project)

            self.db.close()

        except:
            QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Could not read projects database:\n"))            
            return 

        return self.projects

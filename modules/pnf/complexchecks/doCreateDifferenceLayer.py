 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from qgis.core import *
from qgis.gui import *
from Ui_createdifferencelayer import Ui_CreateDifferenceLayer
import datetime


class CreateDifferenceDialog(QDialog, Ui_CreateDifferenceLayer):

    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
#        self.bar = QgsMessageBar(self)
#        self.bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed) 
#        self.gridLayout.addWidget(self.bar, 0, 0, 0, 1, Qt.AlignBottom)                
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        self.okButton.setText("Create")
        self.connect(self.okButton, SIGNAL("accepted()"), lambda foo="bar": self.accept(foo)) 
        
    def initGui(self):             
        self.settings = QSettings("CatAIS","QGeoApp")
        filename = str(self.settings.value("projects/database/path").toString())
        module_name = str(self.settings.value("project/active/appmodule").toString())
        self.projectId = str(self.settings.value("project/active/id").toString())
        

        if filename == "" or filename == None:
            QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "No project database found."))            
            return
            
        self.projects = []

        try:
            self.db = QSqlDatabase.addDatabase("QSQLITE", "Projectdatabase")
            self.db.setDatabaseName(filename) 

            if  self.db.open() == False:
                QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Could not open database.")+ str(self.db.lastError().driverText()))                             
                return 

            sql = "SELECT * FROM projects WHERE appmodule = '"+module_name+"' ORDER BY displayname;"
            print sql

            query = self.db.exec_(sql)
            
            if not query.isActive():
                # does not work on qgis startup...                
                #self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Error occured while fetching projects informations.") , level=QgsMessageBar.CRITICAL, duration=5)                            
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
                project["appmodulename"] = unicode(query.value(record.indexOf("appmodulename")).toString())
                project["projectrootdir"] = str(query.value(record.indexOf("projectrootdir")).toString())
                project["projectdir"] = str(query.value(record.indexOf("projectdir")).toString())
                project["datadate"] = str(query.value(record.indexOf("datadate")).toString())
                project["importdate"] = str(query.value(record.indexOf("importdate")).toString())                
                project["datadate"] = str(query.value(record.indexOf("datadate")).toString())
                project["notes"] = unicode(query.value(record.indexOf("notes")).toString())
                
                self.projects.append(project)

            self.db.close()

        except Exception, e:
            print "Couldn't do it: %s" % e
            QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Could not read projects database."))            
            return 
            
        if self.projects:
            i = 0
            for project in self.projects:
                if unicode(project["displayname"]) == self.projectId:
                    self.cmbBoxProjectBefore.insertItem(self.cmbBoxProjectBefore.count(), unicode(project["displayname"]) + str(" (aktives Projekt)"), i)
                    self.cmbBoxProjectAfter.insertItem(self.cmbBoxProjectAfter.count(), unicode(project["displayname"]) + str(" (aktives Projekt)"), i)
                else:
                    self.cmbBoxProjectBefore.insertItem(self.cmbBoxProjectBefore.count(), unicode(project["displayname"]), i)
                    self.cmbBoxProjectAfter.insertItem(self.cmbBoxProjectAfter.count(), unicode(project["displayname"]), i)
                i += 1
                
            self.cmbBoxProjectBefore.insertItem(0, QCoreApplication.translate("QGeoAppModule.PNF", "Choose project..."), None)
            self.cmbBoxProjectBefore.setCurrentIndex(0)
            self.cmbBoxProjectAfter.insertItem(0, QCoreApplication.translate("QGeoAppModule.PNF", "Choose project..."), None)
            self.cmbBoxProjectAfter.setCurrentIndex(0)

    @pyqtSignature("on_cmbBoxProjectBefore_currentIndexChanged(int)")      
    def on_cmbBoxProjectBefore_currentIndexChanged(self, idx):
        self.lineEditDateBefore.clear()  
        self.textEditBefore.clear()  
        
        if idx > 0:
            project_data = self.projects[idx-1]

            if project_data:                
                self.dbschema_before = str(project_data["dbschema"])
                datadate = datetime.datetime.strptime(str(project_data["datadate"]), "%Y-%m-%d").date()
                
                self.lineEditDateBefore.setText(datadate.strftime("%d. %B %Y"))
                self.textEditBefore.insertPlainText(unicode(project_data["notes"]))
            
    @pyqtSignature("on_cmbBoxProjectAfter_currentIndexChanged(int)")      
    def on_cmbBoxProjectAfter_currentIndexChanged(self, idx):
        self.lineEditDateAfter.clear()  
        self.textEditAfter.clear()  
        
        if idx > 0:
            project_data = self.projects[idx-1]

            if project_data:                
                self.dbschema_after = str(project_data["dbschema"])
                datadate = datetime.datetime.strptime(str(project_data["datadate"]), "%Y-%m-%d").date()
                
                self.lineEditDateAfter.setText(datadate.strftime("%d. %B %Y"))
                self.textEditAfter.insertPlainText(unicode(project_data["notes"]))
            
    def accept(self):
        if self.cmbBoxProjectBefore.currentIndex() == 0 or self.cmbBoxProjectAfter.currentIndex() == 0:
            QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "No project choosen."))            
            return
        
        dbschema = str(self.settings.value("project/active/dbschema").toString())
        dbhost = str(self.settings.value("project/active/dbhost").toString())
        dbname = str(self.settings.value("project/active/dbname").toString())
        dbport = str(self.settings.value("project/active/dbport").toString())
        dbschema = str(self.settings.value("project/active/dbschema").toString())
        dbadmin = str(self.settings.value("project/active/dbadmin").toString())
        dbadminpwd = str(self.settings.value("project/active/dbadminpwd").toString())

        if not dbhost or not dbname or not dbport or not dbschema or not dbadmin or not dbadminpwd:
            QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Should not reach here."))                        

        db = QSqlDatabase.addDatabase("QPSQL", "PostgreSQL")
        db.setHostName(dbhost)
        db.setDatabaseName(dbname)
        db.setUserName(dbadmin)
        db.setPassword(dbadminpwd)
        try:
            db.setPort(int(dbport))
        except ValueError, e:
            print "Couldn't do it: %s" % e
            QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Port is not a integer value."))                        
            return
        
        if not db.open():
            QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Could not open database."))                                    
            return

        # delete existing data in the tables
        sql = "BEGIN;"
        sql += "DELETE FROM "+dbschema+".t_bb_before_except_after;"
        sql += "DELETE FROM "+dbschema+".t_bb_after_except_before;"
        sql += "DELETE FROM "+dbschema+".t_eo_fl_before_except_after;"
        sql += "DELETE FROM "+dbschema+".t_eo_fl_after_except_before;"
        sql += "DELETE FROM "+dbschema+".t_eo_li_before_except_after;"
        sql += "DELETE FROM "+dbschema+".t_eo_li_after_except_before;"
        sql += "DELETE FROM "+dbschema+".t_eo_pt_before_except_after;"
        sql += "DELETE FROM "+dbschema+".t_eo_pt_after_except_before;"
        sql += "COMMIT;"

        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.buttonBox.setEnabled(False)        
        try:
            query = db.exec_(sql)

            if not query.isActive():
                QApplication.restoreOverrideCursor()        
                self.buttonBox.setEnabled(True)     
                QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Something went wrong while deleting data."))                                    
                return
        
            sql = """
            BEGIN;
            -- BODENBEDECKUNG BEFORE EXCEPT AFTER
            INSERT INTO """+dbschema+""".t_bb_before_except_after (the_geom)
            SELECT ST_GeomFromEWKB(the_geom)
            FROM
            (                                                            
            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END as the_geom
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_before+""".bodenbedeckung_boflaeche
              ) AS linestrings
            ) AS segments_before

            EXCEPT 

            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END as the_geom
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_after+""".bodenbedeckung_boflaeche
              ) AS linestrings
            ) AS segments_after
            ) as foo;


            -- BODENBEDECKUNG AFTER EXCEPT BEFORE
            INSERT INTO """+dbschema+""".t_bb_after_except_before (the_geom)
            SELECT ST_GeomFromEWKB(the_geom)
            FROM
            (                                                
            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END as the_geom
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_after+""".bodenbedeckung_boflaeche
              ) AS linestrings
            ) AS segments_before

            EXCEPT 

            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END as the_geom
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_before+""".bodenbedeckung_boflaeche
              ) AS linestrings
            ) AS segments_after
            ) as foo;
            
            
            -- EO FLAECHE BEFORE EXCEPT AFTER
            INSERT INTO """+dbschema+""".t_eo_fl_before_except_after (the_geom)
            SELECT ST_GeomFromEWKB(the_geom)
            FROM
            (                                    
            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END as the_geom
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_before+""".einzelobjekte_flaechenelement
              ) AS linestrings
            ) AS segments_before

            EXCEPT 

            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END as the_geom
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_after+""".einzelobjekte_flaechenelement
              ) AS linestrings
            ) AS segments_after
            ) as foo;
            
            
            -- EO FLAECHE AFTER EXCEPT BEFORE
            INSERT INTO """+dbschema+""".t_eo_fl_after_except_before (the_geom)
            SELECT ST_GeomFromEWKB(the_geom)
            FROM
            (                        
            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END as the_geom
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_after+""".einzelobjekte_flaechenelement
              ) AS linestrings
            ) AS segments_before

            EXCEPT 

            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN (ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE (ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END as the_geom
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_before+""".einzelobjekte_flaechenelement
              ) AS linestrings
            ) AS segments_after
            ) as foo;


            -- EO LINIE BEFORE EXCEPT AFTER
            INSERT INTO """+dbschema+""".t_eo_li_before_except_after (the_geom)
            SELECT ST_GeomFromEWKB(the_geom)
            FROM
            (            
            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END as the_geom
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_before+""".einzelobjekte_flaechenelement
              ) AS linestrings
            ) AS segments_before

            EXCEPT 

            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END as the_geom
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_after+""".einzelobjekte_flaechenelement
              ) AS linestrings
            ) AS segments_after
            ) as foo;
            
            
            -- EO LINIE AFTER EXCEPT BEFORE
            INSERT INTO """+dbschema+""".t_eo_li_after_except_before (the_geom)
            SELECT ST_GeomFromEWKB(the_geom)
            FROM
            (
            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001)) 
                        ELSE ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001)) 
                   END as the_geom
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump((geometrie))).geom              
                FROM """+self.dbschema_after+""".einzelobjekte_linienelement
              ) AS linestrings
            ) AS segments_before

            EXCEPT 

            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001)) 
                        ELSE ST_AsEWKB(ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001)) 
                   END as the_geom
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump((geometrie))).geom
                FROM """+self.dbschema_before+""".einzelobjekte_linienelement
              ) AS linestrings
            ) AS segments_after
            ) as foo;


            -- EO PUNKT BEFORE EXCEPT AFTER
            INSERT INTO """+dbschema+""".t_eo_pt_before_except_after (the_geom)            
            SELECT ST_GeomFromEWKB(the_geom)
            FROM
            (
            SELECT ST_AsEWKB(ST_SnapToGrid(geometrie, 0.001)) as the_geom
            FROM """+self.dbschema_before+""".einzelobjekte_punktelement

            EXCEPT

            SELECT ST_AsEWKB(ST_SnapToGrid(geometrie, 0.001)) as the_geom
            FROM """+self.dbschema_after+""".einzelobjekte_punktelement
            ) as foo;

            -- EO PUNKT AFTER EXCEPT BEFORE
            INSERT INTO """+dbschema+""".t_eo_pt_after_except_before (the_geom)   
            SELECT ST_GeomFromEWKB(the_geom)
            FROM
            (
            SELECT ST_AsEWKB(ST_SnapToGrid(geometrie, 0.001)) as the_geom
            FROM """+self.dbschema_after+""".einzelobjekte_punktelement

            EXCEPT

            SELECT ST_AsEWKB(ST_SnapToGrid(geometrie, 0.001)) as the_geom
            FROM """+self.dbschema_before+""".einzelobjekte_punktelement
            ) as foo;
            COMMIT;
            """
            
            print sql
                        
            query = db.exec_(sql)

            if not query.isActive():
                QApplication.restoreOverrideCursor()        
                self.buttonBox.setEnabled(True)    
                QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Something went wrong while creating data."))                                                    
                return

            db.close()
            
        except Exception, e:
            print "Couldn't do it: %s" % e
            QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Something went wrong while deleting/creating data."))                                                    
            QApplication.restoreOverrideCursor()        
            self.buttonBox.setEnabled(True)
            return
            
        QApplication.restoreOverrideCursor()        
        self.buttonBox.setEnabled(True)
        QMessageBox.information(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Difference layer created."))                                                            



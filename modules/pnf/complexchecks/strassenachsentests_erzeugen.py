 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from qgis.core import *
from qgis.gui import *


class ComplexCheck(QObject):

    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.settings = QSettings("CatAIS","QGeoApp")

    def run(self):     
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

        sql = "BEGIN;"
        sql += "DELETE FROM "+dbschema+".t_achsen_ausserhalb;"
        sql += "COMMIT;"
        
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            query = db.exec_(sql)

            if not query.isActive():
                QApplication.restoreOverrideCursor()        
                QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Something went wrong while deleting data."))                                    
                return

            sql = """
            BEGIN;            
            INSERT INTO """+dbschema+""".t_achsen_ausserhalb (the_geom)
            SELECT geom
            FROM
            (
             SELECT (ST_DumpPoints(geometrie)).geom
             FROM """+dbschema+""".gebaeudeadressen_strassenstueck
            ) as achse LEFT JOIN
            (
             SELECT ogc_fid, geometrie
             FROM """+dbschema+""".bodenbedeckung_boflaeche
             WHERE art = 1
            ) as str ON ST_Intersects(str.geometrie, achse.geom)
            WHERE str.ogc_fid IS NULL;
            
            INSERT INTO """+dbschema+""".t_falscher_anfangspunkt (the_geom)
            SELECT the_geom
            FROM
            (
             SELECT ST_SnapToGrid(anfangspunkt,0.001) as the_geom
             FROM """+dbschema+""".gebaeudeadressen_strassenstueck

             EXCEPT

             SELECT ST_SnapToGrid((ST_DumpPoints(ST_Boundary(ST_MakeLine(ST_StartPoint(geometrie),ST_EndPoint(geometrie))))).geom,0.001) as the_geom
             FROM """+dbschema+""".gebaeudeadressen_strassenstueck
            ) as a
            WHERE geometrytype(the_geom) = 'POINT';

            INSERT INTO """+dbschema+""".t_doppelte_achsen (the_geom)
            SELECT ST_GeomFromEWKB(the_geom) as the_geom
            FROM
            (
            SELECT ST_AsEWKB(the_geom) as the_geom
            FROM
            (
              SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN ST_SnapToGrid(ST_MakeLine(sp,ep), 0.001)  
                          ELSE ST_SnapToGrid(ST_MakeLine(ep,sp), 0.001)
                     END as the_geom
              FROM
              (
                SELECT
                  ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                  ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
                FROM
                (
                  SELECT ((ST_Dump((geometrie))).geom)
                  FROM """+dbschema+""".gebaeudeadressen_strassenstueck
                ) AS linestrings
              ) AS segments
            ) as a
            GROUP BY ST_AsEWKB(the_geom)
            HAVING count(1)>1
            ) as foo;
            COMMIT;
            """
                        
            query = db.exec_(sql)
            
            print sql

            if not query.isActive():
                QApplication.restoreOverrideCursor()        
                QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Something went wrong while creating data."))                                                    
                return

            db.close()
            
        except Exception, e:
            print "Couldn't do it: %s" % e
            QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Something went wrong while deleting/creating data."))                                                    
            QApplication.restoreOverrideCursor()        
            return
            
        QApplication.restoreOverrideCursor()        
        QMessageBox.information(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Layers created."))                                                            

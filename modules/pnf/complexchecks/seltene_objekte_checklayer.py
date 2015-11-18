 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from qgis.core import *
from qgis.gui import *

import os, time
import xlwt as pycel
from qgeoapp.basic.tools.qgeoapputils import QGeoAppUtils


class ComplexCheck(QObject):

    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
    
        self.qutils = QGeoAppUtils()

    def run(self):        
        settings = QSettings("CatAIS","QGeoApp")
        projectId = str(settings.value("project/active/id").toString())
        projectdir = str(settings.value("project/active/projectdir").toString())        
        dbhost = str(settings.value("project/active/dbhost").toString())
        dbport = str(settings.value("project/active/dbport").toString())
        dbname = str(settings.value("project/active/dbname").toString())
        dbschema = str(settings.value("project/active/dbschema").toString())
        dbuser = str(settings.value("project/active/dbuser").toString())
        dbpwd = str(settings.value("project/active/dbpwd").toString())        
        
        QApplication.setOverrideCursor(Qt.WaitCursor)
#        try:
        group = u"Checklayer - Seltene Objekte" + " (" + str(projectId) + ")"
        
        layer = {}
        layer["type"] = "postgres"
        layer["title"] = "BB.BoFlaeche"
        layer["featuretype"] = "bodenbedeckung_boflaeche"
        layer["geom"] = "geometrie"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "true"
        layer["group"] = group
        layer["style"] = "bb/bb_bb_plan.qml"

        vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
        if vlayer <> False:
            self.iface.legendInterface().setLayerVisible(vlayer, True)    

        layer = {}
        layer["type"] = "postgres"
        layer["title"] = "EO.Einzelobjekt"
        layer["featuretype"] = "einzelobjekte_einzelobjekt"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "true"
        layer["group"] = group

        eoeolayer = self.qutils.loadProjectLayer(self.iface, layer)    

        layer = {}
        layer["type"] = "postgres"
        layer["title"] = u"EO.Flaechenelement"
        layer["featuretype"] = "einzelobjekte_flaechenelement"
        layer["geom"] = "geometrie"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "true"
        layer["group"] = group
        layer["style"] = "eo/eo_fl_bb_plan.qml"

        eoflayer = self.qutils.loadProjectLayer(self.iface, layer)    
        if eoflayer <> False:
            self.iface.legendInterface().setLayerVisible(eoflayer, True)    
            
        if eoeolayer <> False and eoflayer <> False:
            joinLayerId = eoeolayer.id()
            joinProvider = eoeolayer.dataProvider()
            joinProvider.select(joinProvider.attributeIndexes())
            joinIdx = joinProvider.fieldNameIndex("tid")
            
            targetProvider = eoflayer.dataProvider()
            targetProvider.select(targetProvider.attributeIndexes())
            targetIdx = targetProvider.fieldNameIndex("flaechenelement_von")

            joinInfo = QgsVectorJoinInfo()
            joinInfo.joinField = joinIdx
            joinInfo.joinLayerId = joinLayerId
            joinInfo.targetField = targetIdx
            joinInfo.memoryCache = True
            
            eoflayer.addJoin(joinInfo)

        layer = {}
        layer["type"] = "postgres"
        layer["title"] = u"EO.Linienelement"
        layer["featuretype"] = "einzelobjekte_linienelement"
        layer["geom"] = "geometrie"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "true"
        layer["group"] = group
        layer["style"] = "eo/eo_li_bb_plan.qml"

        eolilayer = self.qutils.loadProjectLayer(self.iface, layer)    
        if eolilayer <> False:
            self.iface.legendInterface().setLayerVisible(eolilayer, True)    

        if eoeolayer <> False and eolilayer <> False:
            joinLayerId = eoeolayer.id()
            joinProvider = eoeolayer.dataProvider()
            joinProvider.select(joinProvider.attributeIndexes())
            joinIdx = joinProvider.fieldNameIndex("tid")
            
            targetProvider = eolilayer.dataProvider()
            targetProvider.select(targetProvider.attributeIndexes())
            targetIdx = targetProvider.fieldNameIndex("linienelement_von")

            joinInfo = QgsVectorJoinInfo()
            joinInfo.joinField = joinIdx
            joinInfo.joinLayerId = joinLayerId
            joinInfo.targetField = targetIdx
            joinInfo.memoryCache = True
            
            eolilayer.addJoin(joinInfo)

        layer = {}
        layer["type"] = "postgres"
        layer["title"] = u"LI.Liegenschaft"
        layer["featuretype"] = "liegenschaften_liegenschaft"
        layer["geom"] = "geometrie"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "true"
        layer["group"] = group
        layer["style"] = "li/liegenschaft_ortho.qml"

        vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
        if vlayer <> False:
            self.iface.legendInterface().setLayerVisible(vlayer, False)    

        layer = {}
        layer["type"] = "postgres"
        layer["title"] = "BB.Boeschungsbauwerk"
        layer["featuretype"] = "t_boeschungbwerke"
        layer["geom"] = "the_geom"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "true"
        layer["group"] = group
        layer["style"] = "checks/checklayer_punkt.qml"

        vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
        if vlayer <> False:
            self.iface.legendInterface().setLayerVisible(vlayer, True)    
            
        layer = {}
        layer["type"] = "postgres"
        layer["title"] = "EO.Brunnen"
        layer["featuretype"] = "t_brunnen"
        layer["geom"] = "the_geom"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "true"
        layer["group"] = group
        layer["style"] = "checks/checklayer_punkt.qml"

        vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
        if vlayer <> False:
            self.iface.legendInterface().setLayerVisible(vlayer, True)    
        

#        except:            
#            QApplication.restoreOverrideCursor()        
        QApplication.restoreOverrideCursor()        

        # Export feature count in excel file.
        try:
            db = QSqlDatabase.addDatabase("QPSQL", "SelteneObjekte")
            db.setDatabaseName(dbname)
            db.setHostName(dbhost)
            db.setUserName(dbuser)
            db.setPassword(dbpwd)
            
            if  db.open() == False:
                QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Could not open database:\n") + str(db.lastError().driverText()))            
                return 

            # Create excel file.
            wb = pycel.Workbook(encoding='utf-8')
            wb.country_code = 41
            
            style1 = pycel.easyxf('font: bold on;');
            style2 = pycel.easyxf('font: italic on;');

            # Bodenbedeckung            
            sql = """SELECT CASE WHEN anz IS NULL THEN 0 ELSE anz END, bb_art.code as art, bb_art.code_txt as art_txt
FROM
(
 SELECT count(art) as anz, art_txt, art
 FROM """+dbschema+""".bodenbedeckung_boflaeche
 WHERE art IN (7, 9, 19, 20, 21, 22, 30, 33, 35, 36, 37, 38, 39, 40)
 GROUP BY art, art_txt
) bb
FULL JOIN """+dbschema+""".enum__bodenbedeckung_bbart bb_art ON bb_art.code = bb.art
WHERE bb_art.code IN (7, 9, 19, 20, 21, 22, 30, 33, 35, 36, 37, 38, 39, 40)
ORDER BY bb_art.code;"""

            query = db.exec_(sql)
            
            if query.isActive() == False:
                QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Error occured while fetching data informations."))            
                return 
                        
            ws = wb.add_sheet(u'BB seltene Objekte')
            ws.paper_size_code = 8
            ws.print_centered_vert = False
            ws.print_centered_horz = False
            ws.top_margin = 1.0
            ws.left_margin = 1.0 
            ws.bottom_margin = 1.0
            ws.portrait = True
            
            ws.write(0, 0,  str("BB seltene Objekte: "), style1 )
            ws.write(0, 1,  projectId)        

            ws.write(2, 0, str("Art"))
            ws.write(2, 1, str("Art-Text"))
            ws.write(2, 2, str("Anzahl"))

            i = 0
            record = query.record()
            while query.next():
                anz = str(query.value(record.indexOf("anz")).toString())
                art = str(query.value(record.indexOf("art")).toString())
                art_txt = str(query.value(record.indexOf("art_txt")).toString())
                
                ws.write(3+i, 0, art)
                ws.write(3+i, 1, art_txt)
                ws.write(3+i, 2, anz)
                
                i += 1

            # Einzelobjekte
            sql = """SELECT CASE WHEN anz IS NULL THEN 0 ELSE anz END, eo_art.code as art, eo_art.code_txt as art_txt
FROM
(
 SELECT count(art) as anz, art_txt, art
 FROM """+dbschema+""".einzelobjekte_einzelobjekt
 WHERE art IN (9, 14, 15, 16, 17, 18, 23, 30, 31, 35, 36, 37, 38, 40, 42)
 GROUP BY art, art_txt
) eo
FULL JOIN """+dbschema+""".enum__einzelobjekte_eoart eo_art ON eo_art.code = eo.art
WHERE eo_art.code IN (9, 14, 15, 16, 17, 18, 23, 30, 31, 35, 36, 37, 38, 40, 42)
ORDER BY eo_art.code"""

            query = db.exec_(sql)
            
            if query.isActive() == False:
                QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Error occured while fetching data informations."))            
                return 

            ws = wb.add_sheet(u'EO seltene Objekte')
            ws.paper_size_code = 8
            ws.print_centered_vert = False
            ws.print_centered_horz = False
            ws.top_margin = 1.0
            ws.left_margin = 1.0 
            ws.bottom_margin = 1.0
            ws.portrait = True
            
            ws.write(0, 0,  str("EO seltene Objekte: "), style1)
            ws.write(0, 1,  projectId)        

            ws.write(2, 0, str("Art"))
            ws.write(2, 1, str("Art-Text"))
            ws.write(2, 2, str("Anzahl"))

            i = 0
            record = query.record()
            while query.next():
                anz = str(query.value(record.indexOf("anz")).toString())
                art = str(query.value(record.indexOf("art")).toString())
                art_txt = str(query.value(record.indexOf("art_txt")).toString())
                
                ws.write(3+i, 0, art)
                ws.write(3+i, 1, art_txt)
                if int(anz) > 0:
                    ws.write(3+i, 2, anz, style1)
                else:
                    ws.write(3+i, 2, anz)
                
                i += 1

            file = QDir.convertSeparators(QDir.cleanPath(projectdir + os.sep + "seltene_objekte.xls"))
            try:
                wb.save(file)
                QMessageBox.information( None, "", QCoreApplication.translate("QGeoAppModule.PNF", "File written:\n") + file)
            except IOError:
                QMessageBox.warning( None, "", QCoreApplication.translate("QGeoAppModule.PNF", "File <b>not</b> written!<br>")+ file)
                return

            db.close()
    
        except:
            QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Error exporting data from database to excel."))            

        self.canvas.setMapUnits(0)		

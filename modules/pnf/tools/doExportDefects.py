# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import time, os
import xlwt as pycel


class ExportDefects( QObject ):
    def __init__(self, iface):
        self.iface = iface

        
    def run(self):
        settings = QSettings("CatAIS","QGeoApp")
        dbhost = str(settings.value("project/active/dbhost").toString())
        dbport = str(settings.value("project/active/dbport").toString())
        dbname = str(settings.value("project/active/dbname").toString())
        dbschema = str(settings.value("project/active/dbschema").toString())
        dbuser = str(settings.value("project/active/dbuser").toString())
        dbpwd = str(settings.value("project/active/dbpwd").toString())        
        projectdir = str(settings.value("project/active/projectdir").toString())
        projectId = str(settings.value("project/active/id").toString())
        
        uri = QgsDataSourceURI()        
        uri.setConnection(dbhost, dbport, dbname, dbuser, dbpwd)
        uri.setDataSource(dbschema, "t_maengel", "the_geom", "", "ogc_fid")        
        vlayer = QgsVectorLayer(uri.uri(), "Maengel (Punkte)", "postgres")
        
        
        uri = QgsDataSourceURI()        
        uri.setConnection(dbhost, dbport, dbname, dbuser, dbpwd)
        uri.setDataSource(dbschema, "t_maengel_linie", "the_geom", "", "ogc_fid")        
        vlayer_line = QgsVectorLayer(uri.uri(), "Maengel (Linien)", "postgres")

        if not vlayer.isValid():
            QMessageBox.critical(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Could not load defects layer."))            
            return
        
        if not vlayer_line.isValid():
            QMessageBox.critical(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Could not load defects layer."))            
            return        
        
        if vlayer.featureCount() == 0 and vlayer_line.featureCount() == 0:
            QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Defects layer are empty."))                   
            return

        # create excel file
        wb = pycel.Workbook(encoding='utf-8')
        wb.country_code = 41
        
        style1 = pycel.easyxf('font: bold on;');
        style2 = pycel.easyxf('font: italic on;');
        
        ws = wb.add_sheet(u'Mängelliste (Punkte)')
        ws.paper_size_code = 8
        ws.print_centered_vert = False
        ws.print_centered_horz = False
        ws.top_margin = 1.0
        ws.left_margin = 1.0 
        ws.bottom_margin = 1.0
        ws.portrait = True
        
        ws.write(0, 0,  str("Operat: "), style1 )
        ws.write(0, 1,  projectId)        

        provider = vlayer.dataProvider()
        feat = QgsFeature()
        allAttrs = provider.attributeIndexes()
        provider.select(allAttrs)
        
        attrs = provider.fields()
        for i in attrs:
            ws.write(4, i, str(attrs[i].name()), style2)

        ws.write(4, i+1, "Y-Koordinate", style2)
        ws.write(4, i+2, "X-Koordinate", style2)            

        if vlayer.featureCount() > 0:
            j = 0
            while provider.nextFeature(feat):
                geom = feat.geometry()
                point = geom.asPoint()
                attrMap = feat.attributeMap()
                for i in attrMap:
                    type = attrMap[i].type()
                    if type == 4:
                        value = int(attrMap[i].toInt()[0])
                        print value
                    elif type == 10:
                        value = unicode(attrMap[i].toString())
                    else:
                        pass
                    ws.write(5+j, i, value)
                    
                ws.write(5+j, i+1, round(point.x(), 3))
                ws.write(5+j, i+2, round(point.y(), 3))
                
                j += 1
            
            
        ws_line = wb.add_sheet(u'Mängelliste (Linie)')
        ws_line.paper_size_code = 8
        ws_line.print_centered_vert = False
        ws_line.print_centered_horz = False
        ws_line.top_margin = 1.0
        ws_line.left_margin = 1.0 
        ws_line.bottom_margin = 1.0
        ws_line.portrait = True
        
        ws_line.write(0, 0,  str("Operat: "), style1 )
        ws_line.write(0, 1,  projectId)        

        provider_line = vlayer_line.dataProvider()
        feat = QgsFeature()
        allAttrs = provider_line.attributeIndexes()
        provider_line.select(allAttrs)
        
        attrs = provider_line.fields()
        for i in attrs:
            ws_line.write(4, i, str(attrs[i].name()), style2)

        ws_line.write(4, i+1, "Y-Koordinate", style2)
        ws_line.write(4, i+2, "X-Koordinate", style2)            
        ws_line.write(4, i+3, u"Länge [hm]", style2)  
        
        if vlayer_line.featureCount() > 0:
            j = 0
            while provider_line.nextFeature(feat):
                geom = feat.geometry()
                point = geom.vertexAt(0)
                attrMap = feat.attributeMap()
                for i in attrMap:
                    type = attrMap[i].type()
                    if type == 4:
                        value = int(attrMap[i].toInt()[0])
                        print value
                    elif type == 10:
                        value = unicode(attrMap[i].toString())
                    else:
                        pass
                    ws_line.write(5+j, i, value)
                    
                ws_line.write(5+j, i+1, round(point.x(), 3))
                ws_line.write(5+j, i+2, round(point.y(), 3))
                ws_line.write(5+j, i+3, round(geom.length(), 2))
                 
                j += 1

        
        
        file = QDir.convertSeparators(QDir.cleanPath(projectdir + os.sep + "maengel.xls"))
        try:
            wb.save(file)
            QMessageBox.information( None, "", QCoreApplication.translate("QGeoAppModule.PNF", "Defect(s) written:\n") + file)
        except IOError:
            QMessageBox.warning( None, "", QCoreApplication.translate("QGeoAppModule.PNF", "Defect(s) <b>not</b> written!<br>")+ file)
            return

# -*- coding: latin1 -*-
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
        dbhost = str(settings.value("project/active/host").toString())
        dbport = str(settings.value("project/active/port").toString())
        dbname = str(settings.value("project/active/dbname").toString())
        dbschema = str(settings.value("project/active/schema").toString())
        dbuser = str(settings.value("project/active/readuser").toString())
        dbpwd = str(settings.value("project/active/readpwd").toString())        
        
        projectsRootPath = str(settings.value("projects/rootdir").toString())
        projectId = str(settings.value("project/active/id").toString())
        
        uri = QgsDataSourceURI()        
        uri.setConnection(dbhost, dbport, dbname, dbuser, dbpwd)
        uri.setDataSource(dbschema, "maengel", "the_geom", "", "ogc_fid")        
        vlayer = QgsVectorLayer(uri.uri(), "Maengel", "postgres")
        
        if not vlayer.isValid():
            print "Layer failed to load!"        
            return
            # messagebox
        
        if vlayer.featureCount() == 0:
            print "No defects."        
            return
            # messagebox

        # create excel file
        wb = pycel.Workbook(encoding='utf-8')
        wb.country_code = 41
        
        style1 = pycel.easyxf('font: bold on;');
        style2 = pycel.easyxf('font: italic on;');
        
        ws = wb.add_sheet(u'Mängelliste')
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
                    value = str(attrMap[i].toString())
                else:
                    pass
                ws.write(5+j, i, value)
                
            ws.write(5+j, i+1, round(point.x(), 3))
            ws.write(5+j, i+2, round(point.y(), 3))
            
            j += 1

        file = projectsRootPath + os.sep + projectId + os.sep + "maengel.xls"
        try:
            wb.save(file)
            QMessageBox.information( None, "", QCoreApplication.translate("QGeoAppModule.QVeriso", "Defect(s) written:\n") + file)
        except IOError:
            QMessageBox.warning( None, "", QCoreApplication.translate("QGeoAppModule.QVeriso", "Defect(s) <b>not</b> written!<br>")+ file)
            return

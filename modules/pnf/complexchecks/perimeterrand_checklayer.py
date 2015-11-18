 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from qgis.core import *
from qgis.gui import *

import os, time
from qgeoapp.basic.tools.qgeoapputils import QGeoAppUtils


class ComplexCheck(QObject):

    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
    
        self.qutils = QGeoAppUtils()

    def run(self):        
        QApplication.setOverrideCursor(Qt.WaitCursor)
#        try:        
        
        settings = QSettings("CatAIS","QGeoApp")
        dbhost = str(settings.value("project/active/dbhost").toString())
        dbport = str(settings.value("project/active/dbport").toString())
        dbname = str(settings.value("project/active/dbname").toString())
        dbschema = str(settings.value("project/active/dbschema").toString())
        dbuser = str(settings.value("project/active/dbuser").toString())
        dbpwd = str(settings.value("project/active/dbpwd").toString())        
        projectId = str(settings.value("project/active/id").toString())
    
        group = u"Gemeinde - Perimeterrand" + " (" + str(projectId) + ")"
            
        layer = {}
        layer["type"] = "wms"
        layer["title"] = "Orthofoto CIR"
        layer["url"] = "http://www.sogis1.so.ch/cgi-bin/sogis/sogis_orthofoto.wms"
        layer["layers"] = "Orthofoto_CIR_SO"
        layer["format"] = "image/jpeg"
        layer["crs"] = "EPSG:21781"
        layer["group"] = group
        rlayer = self.qutils.loadLayer(self.iface, layer, None, None)                     
            
        layer = {}
        layer["type"] = "wms"
        layer["title"] = "Orthofoto RGB"
        layer["url"] = "http://www.sogis1.so.ch/cgi-bin/sogis/sogis_orthofoto.wms"
        layer["layers"] = "Orthofoto_SO"
        layer["format"] = "image/jpeg"
        layer["crs"] = "EPSG:21781"
        layer["group"] = group
        rlayer = self.qutils.loadLayer(self.iface, layer, None, None) 
        if rlayer <> False:
            self.iface.legendInterface().setLayerVisible(rlayer, False)                 
            
        layer = {}
        layer["type"] = "wms"
        layer["title"] = "AV-WMS (V+D)"
        layer["url"] = "http://WMS_SO:TkBT@geodata01.admin.ch/SWMS"
        layer["layers"] = "av_wms"
        layer["format"] = "image/jpeg"
        layer["crs"] = "EPSG:21781"
        layer["group"] = group
        rlayer = self.qutils.loadLayer(self.iface, layer, None, None)        
        if rlayer <> False:
            self.iface.legendInterface().setLayerVisible(rlayer, True)     
    
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
        layer["title"] = "Gemeindegrenze"
        layer["featuretype"] = "gemeindegrenzen_gemeindegrenze"
        layer["geom"] = "geometrie"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "true"
        layer["group"] = group
        layer["style"] = "gemeindegrenze/gemgre_strichliert.qml"

        gemgrelayer = self.qutils.loadProjectLayer(self.iface, layer) 
        if gemgrelayer <> False:
            self.iface.legendInterface().setLayerVisible(gemgrelayer, True)     

        if gemgrelayer <> False:
            rect = gemgrelayer.extent()
            rect.scale(1.2)
            self.iface.mapCanvas().setExtent(rect)        
            self.iface.mapCanvas().refresh() 


#        except:            
#            QApplication.restoreOverrideCursor()        
        QApplication.restoreOverrideCursor()        

        self.canvas.setMapUnits(0)		

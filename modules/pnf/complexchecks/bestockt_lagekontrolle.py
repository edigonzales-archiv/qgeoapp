 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
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
        self.settings = QSettings("CatAIS","QGeoApp")
        projectId = str(self.settings.value("project/active/id").toString())
        
        QApplication.setOverrideCursor(Qt.WaitCursor)
#        try:
        group = u"Lagekontrolle - Bestockte Fläche" + " (" + str(projectId) + ")"
        
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
            self.iface.legendInterface().setLayerVisible(rlayer, True)     
           
        layer = {}
        layer["type"] = "wms"
        layer["title"] = "DOM"
        layer["url"] = "http://www.sogis1.so.ch/wms/wms_lidar"
        layer["layers"] = "dom_relief_2014"
        layer["format"] = "image/jpeg"
        layer["crs"] = "EPSG:21781"
        layer["group"] = group
        rlayer = self.qutils.loadLayer(self.iface, layer, None, None)                 

        layer = {}
        layer["type"] = "wms"
        layer["title"] = "DTM"
        layer["url"] = "http://www.sogis1.so.ch/wms/wms_lidar"
        layer["layers"] = "dtm_relief_2014"
        layer["format"] = "image/jpeg"
        layer["crs"] = "EPSG:21781"
        layer["group"] = group
        rlayer = self.qutils.loadLayer(self.iface, layer, None, None)                 
                               
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
  
        layer = {}
        layer["type"] = "postgres"
        layer["title"] = "BB.BoFlaeche"
        layer["featuretype"] = "bodenbedeckung_boflaeche"
        layer["geom"] = "geometrie"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "true"
        layer["group"] = group
        layer["style"] = "bb/bb_bestockte_ortho.qml"

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
        layer["style"] = "eo/eo_fl_bestockte_ortho.qml"

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
        layer["style"] = "eo/eo_li_bestockte_ortho.qml"

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
        layer["title"] = u"EO.Punktelement"
        layer["featuretype"] = "einzelobjekte_punktelement"
        layer["geom"] = "geometrie"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "true"
        layer["group"] = group
        layer["style"] = "eo/eo_pk_andere.qml"

        eopklayer = self.qutils.loadProjectLayer(self.iface, layer)    
        if eopklayer <> False:
            self.iface.legendInterface().setLayerVisible(eopklayer, True)    

        if eoeolayer <> False and eopklayer <> False:
            joinLayerId = eoeolayer.id()
            joinProvider = eoeolayer.dataProvider()
            joinProvider.select(joinProvider.attributeIndexes())
            joinIdx = joinProvider.fieldNameIndex("tid")
            
            targetProvider = eopklayer.dataProvider()
            targetProvider.select(targetProvider.attributeIndexes())
            targetIdx = targetProvider.fieldNameIndex("punktelement_von")

            joinInfo = QgsVectorJoinInfo()
            joinInfo.joinField = joinIdx
            joinInfo.joinLayerId = joinLayerId
            joinInfo.targetField = targetIdx
            joinInfo.memoryCache = True
            
            eopklayer.addJoin(joinInfo)

        layer = {}
        layer["type"] = "postgres"
        layer["title"] = u"Waldplan (AWJF)"
        layer["featuretype"] = "waldplan_awjf"
        layer["geom"] = "geom"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "true"
        layer["group"] = group
        layer["style"] = "sogis/waldplan_awjf.qml"

        params =  {}
        params["appmodule"] = str(self.settings.value("project/active/appmodule").toString())
        params["subappmodule"] = str(self.settings.value("project/active/subappmodule").toString())      
        params["provider"] = "postgres"
        params["dbhost"] = str(self.settings.value("project/active/dbhost").toString())
        params["dbport"] = str(self.settings.value("project/active/dbport").toString())
        params["dbname"] = "pnf_varia"
        params["dbschema"] = "sogis"
        params["dbuser"] = str(self.settings.value("project/active/dbuser").toString())
        params["dbpwd"] = str(self.settings.value("project/active/dbpwd").toString())
        params["dbadmin"] = str(self.settings.value("project/active/dbadmin").toString())
        params["dbadminpwd"] = str(self.settings.value("project/active/dbadminpwd").toString())
        
        layer["params"] = params

        vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
        if vlayer <> False:
            self.iface.legendInterface().setLayerVisible(vlayer, False)    

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
        layer["title"] = "TS-Einteilung"
        layer["featuretype"] = "tseinteilung_toleranzstufe"
        layer["geom"] = "geometrie"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "true"
        layer["group"] = group
        layer["style"] = "ts/ts_einteilung.qml"
        
        vlayer = self.qutils.loadProjectLayer(self.iface, layer)       

        layer = {}
        layer["type"] = "postgres"
        layer["title"] = "Kontrollraster (Planeinteilung)"
        layer["featuretype"] = "t_kontrollraster_plan_bestockt"
        layer["geom"] = "the_geom"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "false"
        layer["group"] = group
        layer["style"] = "kontrollraster/kontrollraster.qml"
        
        vlayer = self.qutils.loadProjectLayer(self.iface, layer)       
        if vlayer <> False:            
            self.iface.legendInterface().setLayerVisible(vlayer, False)        
            provider = vlayer.dataProvider()
            provider.select(provider.attributeIndexes())
            ogc_fid_idx = provider.fieldNameIndex("ogc_fid")
            vlayer.setEditType(ogc_fid_idx, 10)
            
            plannummer_idx = provider.fieldNameIndex("plannummer")
            vlayer.setEditType(plannummer_idx, 10)            
            
            kontrolliert_idx = provider.fieldNameIndex("kontrolliert")
            vlayer.setEditType(kontrolliert_idx, 7)
            vlayer.setCheckedState(kontrolliert_idx, 't', 'f')

        layer = {}
        layer["type"] = "postgres"
        layer["title"] = "Kontrollraster"
        layer["featuretype"] = "t_kontrollraster_bestockte_500"
        layer["geom"] = "the_geom"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "false"
        layer["group"] = group
        layer["style"] = "kontrollraster/kontrollraster.qml"
        
        vlayer = self.qutils.loadProjectLayer(self.iface, layer)       
        if vlayer <> False:            
            self.iface.legendInterface().setLayerVisible(vlayer, True)        
            provider = vlayer.dataProvider()
            provider.select(provider.attributeIndexes())
            ogc_fid_idx = provider.fieldNameIndex("ogc_fid")
#        vlayer.setEditType(ogc_fid_idx, QgsVectorLayer.EditType.Hidden)
            vlayer.setEditType(ogc_fid_idx, 10)
            
            kontrolliert_idx = provider.fieldNameIndex("kontrolliert")
            vlayer.setEditType(kontrolliert_idx, 7)
            vlayer.setCheckedState(kontrolliert_idx, 't', 'f')

        if gemgrelayer <> False:
            rect = gemgrelayer.extent()
            rect.scale(1.2)
            self.iface.mapCanvas().setExtent(rect)        
            self.iface.mapCanvas().refresh() 


#        except:            
#            QApplication.restoreOverrideCursor()        
        QApplication.restoreOverrideCursor()        

        self.canvas.setMapUnits(0)		

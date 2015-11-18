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
        group = "Checklayer - Strasse" + " (" + str(projectId) + ")"
        
        layer = {}
        layer["type"] = "postgres"
        layer["title"] = "BB.BoFlaeche"
        layer["featuretype"] = "bodenbedeckung_boflaeche"
        layer["geom"] = "geometrie"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "true"
        layer["group"] = group
        layer["style"] = "bb/bb_strasse_bbplan.qml"

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
        layer["style"] = "eo/eo_fl_strasse_ortho.qml"

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
        layer["style"] = "eo/eo_li_strasse_ortho.qml"

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
        layer["title"] = "Pfeiler < 0.25 m2"
        layer["featuretype"] = "t_pfeiler_50cm"
        layer["geom"] = "the_geom"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "false"
        layer["group"] = group
        layer["style"] = "checks/checklayer_punkt.qml"
        
        vlayer = self.qutils.loadProjectLayer(self.iface, layer)       
        if vlayer <> False:            
            self.iface.legendInterface().setLayerVisible(vlayer, True)        

        layer = {}
        layer["type"] = "postgres"
        layer["title"] = "BB.Strasse_Weg > 10000 m2"
        layer["featuretype"] = "t_str_flaeche_10000"
        layer["geom"] = "the_geom"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "false"
        layer["group"] = group
        layer["style"] = "checks/checklayer_punkt.qml"
        
        vlayer = self.qutils.loadProjectLayer(self.iface, layer)       
        if vlayer <> False:            
            self.iface.legendInterface().setLayerVisible(vlayer, True)  

        layer = {}
        layer["type"] = "postgres"
        layer["title"] = "EO.schmaler_Weg in TS 2"
        layer["featuretype"] = "t_schmaler_weg_ts2"
        layer["geom"] = "the_geom"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "false"
        layer["group"] = group
        layer["style"] = "checks/checklayer_punkt.qml"
        
        vlayer = self.qutils.loadProjectLayer(self.iface, layer)       
        if vlayer <> False:            
            self.iface.legendInterface().setLayerVisible(vlayer, True)  


#        except:            
#            QApplication.restoreOverrideCursor()        
        QApplication.restoreOverrideCursor()        

        self.canvas.setMapUnits(0)		

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
        group = "Checklayer - Bebautes Gebiet" + " (" + str(projectId) + ")"
        
  
        layer = {}
        layer["type"] = "postgres"
        layer["title"] = "BB.Objektname 'u.'"
        layer["featuretype"] = "t_bbobj_u"
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
        layer["title"] = "EO.Objektname 'u.'"
        layer["featuretype"] = "t_eoobj_u"
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
        layer["title"] = "EO.Treppe nicht ein Objekt"
        layer["featuretype"] = "t_treppe_modellbildung"
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
        layer["title"] = u"EO.Flächenelement 'übrig. Geb.teil' freistehend"
        layer["featuretype"] = "t_gebteil_frei"
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
        layer["title"] = u"EO.Linienelement 'übrig. Geb.teil' ausserhalb Gebäude"
        layer["featuretype"] = "t_gebteil_ausserhalb"
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
        layer["title"] = u"EO.Flächenelement 'übrig. Geb.teil' innerhalb Gebäude"
        layer["featuretype"] = "t_gebteil_geb"
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
        layer["title"] = u"EO.Pfeiler im Gebäude"
        layer["featuretype"] = "t_pfeiler_gebaeude"
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
        layer["title"] = u"EO.uebriger_Gebaeudeteil < 1.5 m2"
        layer["featuretype"] = "t_gebteil_15"
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
        layer["title"] = u"Ein EO.Objekt pro Element"
        layer["featuretype"] = "t_eo_modellbildung"
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
        layer["title"] = u"BB.Wasserbecken mit EO.Mauer"
        layer["featuretype"] = "t_mauer_wasserbecken"
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
        layer["title"] = u"EO.Linienelement Mauer"
        layer["featuretype"] = "t_mauer_linien"
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
        layer["title"] = u"EO.Linienelement Mauer ausserhalb EO.Flächenelement Mauer"
        layer["featuretype"] = "t_mauer_ausserhalb"
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
        layer["title"] = u"EO.Mauer freistehend"
        layer["featuretype"] = "t_mauer_freistehend"
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
        layer["title"] = "EO.Mauer nicht ein Objekt"
        layer["featuretype"] = "t_mauer_modellbildung"
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
        layer["title"] = u"BB.Gebaeude ohne Gartenanlage"
        layer["featuretype"] = "t_abgrenzung_gartenanlage"
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
        layer["title"] = u"BB.Gebaeude ohne Erschliessung"
        layer["featuretype"] = "t_geb_ohne_ersch"
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
        layer["title"] = u"BB.Parkplatz < 100 m2"
        layer["featuretype"] = "t_pp_kleiner_100"
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
        layer["title"] = u"BB.Gebaeude mit mehreren Adressen"
        layer["featuretype"] = "t_2_gebein"
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
        layer["title"] = u"BB.Gebaeude < 6 m2"
        layer["featuretype"] = "t_gebaeude_kleiner_6"
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
        layer["title"] = u"EO.Linienelement unterird. Gebaeude"
        layer["featuretype"] = "t_u_geb_linien"
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
        layer["title"] = u"EO.Unterstand auf Gebäude"
        layer["featuretype"] = "t_unterstand_auf_geb"
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

        self.canvas.setMapUnits(0)		

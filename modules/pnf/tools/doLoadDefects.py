 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import os, time
from qgeoapp.basic.tools.qgeoapputils import QGeoAppUtils


class LoadDefects(QObject):

    def __init__(self, iface, projectId):
        self.iface = iface
        self.projectId = projectId
        self.canvas = self.iface.mapCanvas()
        self.qutils = QGeoAppUtils()

    def run(self):        
        self.settings = QSettings("CatAIS","QGeoApp")
        self.projectId = str(self.settings.value("project/active/id").toString())
        
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:            
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Fehlerarten"
            layer["featuretype"] = "t_maengel_fehler"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = "true"
            layer["group"] = u"Mängel" + " (" + self.projectId + ")"

            lyr_fehlerarten = self.qutils.loadProjectLayer(self.iface, layer)    
            if lyr_fehlerarten <> False:
                lyr_fehlerarten.setLayerName(u"Fehlerarten")

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Maengelarten"
            layer["featuretype"] = "t_maengel_art"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = "true"
            layer["group"] = u"Mängel" + " (" + self.projectId + ")"

            lyr_maengelarten = self.qutils.loadProjectLayer(self.iface, layer)    
            if lyr_maengelarten <> False:
                lyr_maengelarten.setLayerName(u"Mängelarten")

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"Maengelliste (Punkte)"
            layer["featuretype"] = "t_maengel"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"
            layer["readonly"] = "true"
            layer["sql"] = ""                        
            layer["group"] = u"Mängel" + " (" + self.projectId + ")"
            layer["style"] = "maengel/maengel.qml"

            vlayer = self.qutils.loadProjectLayer(self.iface, layer)  
            if vlayer <> False:
                self.iface.legendInterface().setLayerVisible(vlayer, True) 
                vlayer.setLayerName(u"Mängelliste (Punkte)")
                #vlayer.saveDefaultStyle()            

                provider = vlayer.dataProvider()
                provider.select(provider.attributeIndexes())
                ogc_fid_idx = provider.fieldNameIndex("ogc_fid")
                gruppe_idx = provider.fieldNameIndex("gruppe")
                art_idx = provider.fieldNameIndex("art")
                fehler_idx = provider.fieldNameIndex("fehler")
                feld_idx = provider.fieldNameIndex("feldkontrolle")
                lnf_idx = provider.fieldNameIndex("lnf")
                terr_idx = provider.fieldNameIndex("terrestrisch")
                bemerkung_idx = provider.fieldNameIndex("bemerkung")
                datum_idx = provider.fieldNameIndex("datum")  

                vlayer.addAttributeAlias(gruppe_idx, "Gruppe:")
                vlayer.addAttributeAlias(art_idx, "Art:")
                vlayer.addAttributeAlias(fehler_idx, "Fehler:")
                vlayer.addAttributeAlias(feld_idx, "Feldkontrolle:")
                vlayer.addAttributeAlias(lnf_idx, u"Laufende Nachführung:")
                vlayer.addAttributeAlias(terr_idx, "Terrestrische Aufnahme:")
                vlayer.addAttributeAlias(bemerkung_idx, "Bemerkung:")
      
                vlayer.setEditType(ogc_fid_idx, 11)
                vlayer.setEditType(gruppe_idx, 15)
                vlayer.setEditType(art_idx, 15)
                vlayer.setEditType(fehler_idx, 15)
                vlayer.setEditType(feld_idx, 7)
                vlayer.setEditType(lnf_idx, 7)
                vlayer.setEditType(terr_idx, 7)
                vlayer.setEditType(bemerkung_idx, 12)            
                vlayer.setEditType(datum_idx, 11)            
                
                vlayer.setCheckedState(feld_idx, 't', 'f')
                vlayer.setCheckedState(lnf_idx, 't', 'f')
                vlayer.setCheckedState(terr_idx, 't', 'f')
                
                gruppe_valrel = vlayer.valueRelation(gruppe_idx)
                gruppe_valrel.mLayer = lyr_maengelarten.id()
                gruppe_valrel.mKey = "gruppe"
                gruppe_valrel.mValue = "gruppe"
                #gruppe_valrel.mFilterExpression = "\"gruppe\" = 'Strasse'"
                gruppe_valrel.mOrderByValue = True
                gruppe_valrel.mAllowNull = False
                gruppe_valrel.mAllowMulti = False
                
                art_valrel = vlayer.valueRelation(art_idx)
                art_valrel.mLayer = lyr_maengelarten.id()
                art_valrel.mKey = "art_txt"
                art_valrel.mValue = "art_txt"
                art_valrel.mOrderByValue = True
                art_valrel.mAllowNull = False
                art_valrel.mAllowMulti = False
                
                fehler_valrel = vlayer.valueRelation(fehler_idx)
                fehler_valrel.mLayer = lyr_fehlerarten.id()
                fehler_valrel.mKey = "fehler_txt"
                fehler_valrel.mValue = "fehler_txt"
                fehler_valrel.mOrderByValue = True
                fehler_valrel.mAllowNull = False
                fehler_valrel.mAllowMulti = False            


            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"Maengelliste (Linien)"
            layer["featuretype"] = "t_maengel_linie"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"
            layer["readonly"] = "true"
            layer["sql"] = ""                        
            layer["group"] = u"Mängel" + " (" + self.projectId + ")"
            layer["style"] = "maengel/maengel_linie.qml"

            vlayer = self.qutils.loadProjectLayer(self.iface, layer)  
            if vlayer <> False:
                self.iface.legendInterface().setLayerVisible(vlayer, True) 
                vlayer.setLayerName(u"Mängelliste (Linie)")
                #vlayer.saveDefaultStyle()                
                    
                provider = vlayer.dataProvider()
                provider.select(provider.attributeIndexes())
                ogc_fid_idx = provider.fieldNameIndex("ogc_fid")
                gruppe_idx = provider.fieldNameIndex("gruppe")
                art_idx = provider.fieldNameIndex("art")
                fehler_idx = provider.fieldNameIndex("fehler")
                feld_idx = provider.fieldNameIndex("feldkontrolle")
                lnf_idx = provider.fieldNameIndex("lnf")
                terr_idx = provider.fieldNameIndex("terrestrisch")                
                bemerkung_idx = provider.fieldNameIndex("bemerkung")
                datum_idx = provider.fieldNameIndex("datum")  

                vlayer.addAttributeAlias(gruppe_idx, "Gruppe:")
                vlayer.addAttributeAlias(art_idx, "Art:")
                vlayer.addAttributeAlias(fehler_idx, "Fehler:")
                vlayer.addAttributeAlias(feld_idx, "Feldkontrolle:")
                vlayer.addAttributeAlias(lnf_idx, u"Laufende Nachführung:")
                vlayer.addAttributeAlias(terr_idx, "Terrestrische Aufnahme:")                
                vlayer.addAttributeAlias(bemerkung_idx, "Bemerkung:")
      
                vlayer.setEditType(ogc_fid_idx, 11)
                vlayer.setEditType(gruppe_idx, 15)
                vlayer.setEditType(art_idx, 15)
                vlayer.setEditType(fehler_idx, 15)
                vlayer.setEditType(feld_idx, 7)
                vlayer.setEditType(lnf_idx, 7)
                vlayer.setEditType(terr_idx, 7)                
                vlayer.setEditType(bemerkung_idx, 12)            
                vlayer.setEditType(datum_idx, 11)            
                
                vlayer.setCheckedState(feld_idx, 't', 'f')
                vlayer.setCheckedState(lnf_idx, 't', 'f')
                vlayer.setCheckedState(terr_idx, 't', 'f')                
                
                gruppe_valrel = vlayer.valueRelation(gruppe_idx)
                gruppe_valrel.mLayer = lyr_maengelarten.id()
                gruppe_valrel.mKey = "gruppe"
                gruppe_valrel.mValue = "gruppe"
                gruppe_valrel.mOrderByValue = True
                gruppe_valrel.mAllowNull = False
                gruppe_valrel.mAllowMulti = False
                
                art_valrel = vlayer.valueRelation(art_idx)
                art_valrel.mLayer = lyr_maengelarten.id()
                art_valrel.mKey = "art_txt"
                art_valrel.mValue = "art_txt"
                art_valrel.mOrderByValue = True
                art_valrel.mAllowNull = False
                art_valrel.mAllowMulti = False
                
                fehler_valrel = vlayer.valueRelation(fehler_idx)
                fehler_valrel.mLayer = lyr_fehlerarten.id()
                fehler_valrel.mKey = "fehler_txt"
                fehler_valrel.mValue = "fehler_txt"
                fehler_valrel.mOrderByValue = True
                fehler_valrel.mAllowNull = False
                fehler_valrel.mAllowMulti = False     
            
        except:            
            QApplication.restoreOverrideCursor()        
        QApplication.restoreOverrideCursor()        

        self.canvas.setMapUnits(0)		

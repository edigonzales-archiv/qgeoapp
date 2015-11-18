 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

from qgeoapp.basic.tools.qgeoapputils import QGeoAppUtils

class ComplexCheck(QObject):

    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
    
        self.qutils = QGeoAppUtils()
    
    def run(self):        
        self.settings = QSettings("CatAIS","QGeoApp")
        project_id = str(self.settings.value("project/active/id").toString())
#        epsg = str(self.settings.value("project/active/epgs").toString())
        

        if not project_id:
#            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "project_id not set"), level=QgsMessageBar.CRITICAL, duration=5)                                
            return
        
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            group = "Differenzlayer " + " (" + str(project_id) + ")"
            
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "BB vorher NICHT in nachher"
            layer["featuretype"] = "t_bb_before_except_after"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "bb/bb_before_except_after.qml"

            vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "BB nachher NICHT in vorher"
            layer["featuretype"] = "t_bb_after_except_before"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "bb/bb_after_except_before.qml"

            vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "EO.Flaeche vorher NICHT in nachher"
            layer["featuretype"] = "t_eo_fl_before_except_after"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "eo/eo_fl_before_except_after.qml"

            vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "EO.Flaeche nachher NICHT in vorher"
            layer["featuretype"] = "t_eo_fl_after_except_before"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "eo/eo_fl_after_except_before.qml"

            vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "EO.Linie vorher NICHT in nachher"
            layer["featuretype"] = "t_eo_li_before_except_after"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "eo/eo_li_before_except_after.qml"

            vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "EO.Linie nachher NICHT in vorher"
            layer["featuretype"] = "t_eo_li_after_except_before"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "eo/eo_li_after_except_before.qml"

            vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "EO.Punkt vorher NICHT in nachher"
            layer["featuretype"] = "t_eo_pt_before_except_after"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "eo/eo_pt_before_except_after.qml"

            vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "EO.Punkt nachher NICHT in vorher"
            layer["featuretype"] = "t_eo_pt_after_except_before"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "eo/eo_pt_after_except_before.qml"

            vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    


        except Exception, e:
            QApplication.restoreOverrideCursor()            
            print "Couldn't do it: %s" % e            
            QMessageBox.warning(None, "QGeoAppModule.PNF",  str(e))                                                                
#            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", str(e)), level=QgsMessageBar.CRITICAL, duration=5)                    
        QApplication.restoreOverrideCursor()        

        # Workaround for geometryless-tables-wgs84-bug.
        try:
            self.canvas.setMapUnits(0)		
            srs = QgsCoordinateReferenceSystem()
            srs.createFromSrid(int(21781))
            renderer = self.canvas.mapRenderer()
            renderer.setDestinationCrs(srs)
        except Exception, e:
            print "Couldn't do it: %s" % e            
            QMessageBox.warning(None, "QGeoAppModule.PNF",  str(e))                                                                

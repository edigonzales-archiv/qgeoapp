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
                
        if not project_id:
#            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "project_id not set"), level=QgsMessageBar.CRITICAL, duration=5)                                
            return
        
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            group = "Strassenachsentests " + " (" + str(project_id) + ")"
                            
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Strassenachsen ausserhalb BB.Strasse_Weg"
            layer["featuretype"] = "t_achsen_ausserhalb"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "geb/achsen_ausserhalb.qml"
        
            vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Anfangspunkte falsch"
            layer["featuretype"] = "t_falscher_anfangspunkt"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "geb/falscher_anfangspunkt.qml"
        
            vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    
                
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Doppelte Strassenachsen"
            layer["featuretype"] = "t_doppelte_achsen"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "geb/doppelte_achsen.qml"
        
            vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

        except Exception, e:
            QApplication.restoreOverrideCursor()            
            print "Couldn't do it: %s" % e            
            QMessageBox.warning(None, "QGeoAppModule.PNF",  str(e))                                                                
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

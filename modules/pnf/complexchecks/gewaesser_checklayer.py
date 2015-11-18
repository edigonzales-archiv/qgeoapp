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
        group = u"Checklayer - Gewässer" + " (" + str(projectId) + ")"
        
        layer = {}
        layer["type"] = "postgres"
        layer["title"] = "BB.stehendes_Gewaesser < 100 m2"
        layer["featuretype"] = "t_gewaesser_100"
        layer["geom"] = "the_geom"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "true"
        layer["group"] = group
        layer["style"] = "checks/checklayer_punkt.qml"

        vlayer = self.qutils.loadProjectLayer(self.iface, layer) 
        if vlayer <> False:
            self.iface.legendInterface().setLayerVisible(vlayer, True) 
            # featureCount funktioniert nicht. Workaround:
            vlayer.removeSelection()
            vlayer.invertSelection()  
            anz_gewaesser_100 = vlayer.selectedFeatureCount()
            vlayer.removeSelection()
 
        layer = {}
        layer["type"] = "postgres"
        layer["title"] = u"EO.eingedoltes_Gewaesser auf BB.Gewaesser"
        layer["featuretype"] = "t_einged_fliessend"
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
        layer["title"] = "EO.Quelle"
        layer["featuretype"] = "t_eo_quellen"
        layer["geom"] = "the_geom"
        layer["key"] = "ogc_fid"            
        layer["sql"] = ""
        layer["readonly"] = "true"
        layer["group"] = group
        layer["style"] = "checks/checklayer_punkt.qml"

        vlayer = self.qutils.loadProjectLayer(self.iface, layer) 
        if vlayer <> False:
            self.iface.legendInterface().setLayerVisible(vlayer, True)     
            # featureCount funktioniert nicht. Workaround:
            vlayer.removeSelection()
            vlayer.invertSelection()  
            anz_quellen = vlayer.selectedFeatureCount()
            vlayer.removeSelection()


#        QMessageBox.information( None, "Checklayer", "<b>Checklayer:</b> <br>"
#                                + "<table>"
#                                + "<tr> <td>Anzahl Quellen: </td> <td>" + str(anz_quellen) +  "</td> </tr>"
#                                + u"<tr> <td>Anzahl ste. Gewässer &lt; 100 m2: </td> <td>" + str(anz_gewaesser_100) +  "</td> </tr>"
#                                + "</table>")


#        except:            
#            QApplication.restoreOverrideCursor()        
        QApplication.restoreOverrideCursor()        

        self.canvas.setMapUnits(0)		

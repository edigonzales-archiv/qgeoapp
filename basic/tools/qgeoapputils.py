# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtXml
from qgis.core import *
from qgis.gui import *

import time, os, json, locale, sys

class QGeoAppUtils: 
    def loadProjectLayer(self, iface, layer, collapseLegend = False):
        settings = QSettings("CatAIS","QGeoApp")
        moduleName = str(settings.value("project/active/appmodule").toString())
        subModuleName = str(settings.value("project/active/subappmodule").toString())        
        provider = str(settings.value("project/active/provider").toString())
        dbhost = str(settings.value("project/active/dbhost").toString())
        dbport = str(settings.value("project/active/dbport").toString())
        dbname = str(settings.value("project/active/dbname").toString())
        dbschema = str(settings.value("project/active/dbschema").toString())
        dbuser = str(settings.value("project/active/dbuser").toString())
        dbpwd = str(settings.value("project/active/dbpwd").toString())
        dbadmin = str(settings.value("project/active/dbadmin").toString())
        dbadminpwd = str(settings.value("project/active/dbadminpwd").toString())

        if dbhost == "" or dbport == "" or dbname == "" or dbschema == "" or dbuser == "" or dbpwd == ""  or dbadmin == "" or dbadminpwd == "":
            QMessageBox.critical(None, "QGeoApp.Utils",  QCoreApplication.translate("QGeoApp.Utils", "Missing database parameter. Cannot load layer."))                
            return False

        if moduleName == "" or provider == "":
            QMessageBox.critical(None, "QGeoApp.Utils",  QCoreApplication.translate("QGeoApp.Utils", "Missing parameter. Cannot load layer."))                
            return False

        # ZUM DEBUGGEN
        if 1 > 0:
        #try:
            featureType = str(layer["featuretype"])
            title = unicode(layer["title"])
            key = str(layer["key"])            
            try:
                geom = str(layer["geom"])
            except:
                geom = ""
            try:
                style = str(layer["style"])
            except:
                style = ""
            try:
                group = unicode(layer["group"])
            except:
                group = None
            try:
                sql = str(layer["sql"])
            except:
                sql = ""
            try:
                params = layer["params"]
                moduleName = params["appmodule"]
                subModuleName = params["subappmodule"]
                provider = params["provider"]
                dbhost = params["dbhost"]
                dbport = params["dbport"]
                dbname = params["dbname"]
                dbschema = params["dbschema"]
                dbuser = params["dbuser"]
                dbpwd = params["dbpwd"]
                dbadmin = params["dbadmin"]
                dbadminpwd = params["dbadminpwd"]
            except:
                params = None

            if geom == "":
                if str(layer["readonly"]) == "true":
                    uri = QgsDataSourceURI("dbname='"+dbname+"' host="+dbhost+" port="+dbport+" user='"+dbuser+"' password='"+dbpwd+"' table=\""+dbschema+"\".\""+featureType+"\" key="+key+" sql="+sql)
                else:
                    uri = QgsDataSourceURI("dbname='"+dbname+"' host="+dbhost+" port="+dbport+" user='"+dbadmin+"' password='"+dbadminpwd+"' table=\""+dbschema+"\".\""+featureType+"\" key="+key+" sql="+sql)
            else:
                uri = QgsDataSourceURI()
                if str(layer["readonly"]) == "true":
                    uri.setConnection(dbhost, dbport, dbname, dbuser, dbpwd)
                else:
                    uri.setConnection(dbhost, dbport, dbname, dbadmin, dbadminpwd)
                uri.setDataSource(dbschema, featureType, geom, sql, key)

            print "***************************3"
            print uri.uri()

            vlayer = QgsVectorLayer(uri.uri(), title, provider)
            
            if subModuleName == "":
                pathToQml = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/modules/"+moduleName+"/qml/"+style))
            else:
                pathToQml = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/modules/"+moduleName+"/submodules/"+subModuleName+"qml/"+style))

            qml = QDir.convertSeparators(QDir.cleanPath(pathToQml))
            vlayer.loadNamedStyle(qml)
            
            if not vlayer.isValid():
                QMessageBox.critical(None, "QGeoApp.Utils",  QCoreApplication.translate("QGeoApp.Utils", "Layer is not valid."))     
                return False       
            else:
                QgsMapLayerRegistry.instance().addMapLayer(vlayer)

            if collapseLegend == True:
                legendTree = iface.mainWindow().findChild(QDockWidget,"Legend").findChild(QTreeWidget)   
                legendTree.collapseItem(legendTree.currentItem())
            
            # furchtbares Gebastel....
            grpList = iface.legendInterface().groups()
            grpIdx = grpList.indexOf(group)

            if grpIdx >= 0:
                grpIdxAbs = self.getGroupIndex( iface, group )
                if grpIdxAbs <> 0:
                    iface.legendInterface().moveLayer(vlayer, grpIdx)
                    #iface.legendInterface().setLayerVisible(vlayer, False)
                    iface.legendInterface().setGroupExpanded(grpIdx-1,  False)
                    #iface.legendInterface().setGroupVisible(grpIdx-1,  False)                
            else:      
                grpIdx = iface.legendInterface().addGroup(group)
                iface.legendInterface().moveLayer(vlayer, grpIdx)
       
            #iface.legendInterface().setLayerVisible(vlayer,  False)
            iface.legendInterface().setGroupExpanded(grpIdx,  False)
            #iface.legendInterface().setGroupVisible(grpIdx,  False)            
            


            return vlayer
            
#        except:
#            QMessageBox.critical(None, "QGeoApp.Utils",  QCoreApplication.translate("QGeoApp.Utils", "Error adding layer."))                
#            return False

    
    def loadLayer(self, iface, layer, parentGroupName, pathToQml):
        settings = QSettings("CatAIS","QGeoApp")
        moduleName = str(settings.value("project/active/appmodule").toString())
        
        if layer["type"] == "wms":
            url = layer["url"]
            title = layer["title"]
            layers = layer["layers"].split(",") 
            format = layer["format"]
            crs = layer["crs"]
            
            styles = []
            for i in range(len(layers)):
                styles.append("")

            try:
                group = layer["group"]
            except:
                group = ""
                p#rint "no group for layer" + str(title)    
                
            try:
                style = layer["style"]
            except:
                style = ""

			# Neue API:
            # Ignore noch als parameter!
            #uri = "IgnoreGetMapUrl=1&crs="+crs+"&layers="+layers+"&styles="+styles+"&format="+format+"&url="+url
            #vlayer = QgsRasterLayer (uri, title, "wms", False)      
            
            # 1.8 / enterprise API
            vlayer = QgsRasterLayer(0, url, title, "wms", layers, styles, format, crs)        
            
            if style <> "":
                pathToQml = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/modules/"+moduleName+"/qml/"+style))
                qml = QDir.convertSeparators(QDir.cleanPath(pathToQml))
                vlayer.loadNamedStyle(qml)
        
        if not vlayer.isValid():
            print "Layer failed to load!"        
            return False
        else:
            QgsMapLayerRegistry.instance().addMapLayer(vlayer)
            
        iface.legendInterface().setLayerVisible(vlayer, False)      
        iface.mapCanvas().refresh()   
            
        legendTree = iface.mainWindow().findChild(QDockWidget,"Legend").findChild(QTreeWidget)   
        legendTree.collapseItem(legendTree.currentItem())
        
        # furchtbares Gebastel....
        grpList = iface.legendInterface().groups()
        grpIdx = grpList.indexOf(group)

        if grpIdx >= 0:
            grpIdxAbs = self.getGroupIndex( iface, group )
            if grpIdxAbs <> 0:
                iface.legendInterface().moveLayer(vlayer, grpIdx)
                #iface.legendInterface().setLayerVisible(vlayer, False)
                iface.legendInterface().setGroupExpanded(grpIdx-1,  False)
                #iface.legendInterface().setGroupVisible(grpIdx-1,  False)                
        else:
            grpIdx = iface.legendInterface().addGroup(group)
            iface.legendInterface().moveLayer(vlayer, grpIdx)
   
        #iface.legendInterface().setLayerVisible(vlayer,  False)
        iface.legendInterface().setGroupExpanded(grpIdx,  False)
        #iface.legendInterface().setGroupVisible(grpIdx,  False)            
            

        return vlayer
            
#        except KeyError:
#            message = sys.exc_info()[0]                                        
#            QMessageBox.critical(None, "QGeoApp.Utils",  QCoreApplication.translate("QGeoApp.Utils", "Key not found in layer definition. \nCannot load layer. \n\n") + str(message))                
#            return False

        
    def getGroupIndex(self, iface, groupName):
        relationList = iface.legendInterface().groupLayerRelationship()
        i = 0
        for item in relationList:
            if item[0] == groupName:
                i = i  + 1
                return i
            i = i + 1
        return 0


    # Return QgsVectorLayer from a layer name (as string)
    # (c) Carson Farmer / fTools
    def getVectorLayerByName(self, myName):
        layermap = QgsMapLayerRegistry.instance().mapLayers()
        for name, layer in layermap.iteritems():
            if layer.type() == QgsMapLayer.VectorLayer and layer.name() == myName:
                if layer.isValid():
                    return layer
                else:
                    return None  


    # Return QgsVectorLayer from a layer id (as string)
    def getVectorLayerByLayerId(self, layerId):
        layermap = QgsMapLayerRegistry.instance().mapLayers()
        for name, layer in layermap.iteritems():
            if layer.type() == QgsMapLayer.VectorLayer and layer.id() == layerId:
                if layer.isValid():
                    return layer
                else:
                    return None  

                    
    # Return list of names of all layers in QgsMapLayerRegistry
    # (c) Carson Farmer / fTools
    def getLayerNames(self, vTypes):
        layermap = QgsMapLayerRegistry.instance().mapLayers()
        layerlist = []
        if vTypes == "all":
            for name, layer in layermap.iteritems():
                layerlist.append(unicode( layer.name()))
        else:
            for name, layer in layermap.iteritems():
                if layer.type() == QgsMapLayer.VectorLayer:
                    if layer.geometryType() in vTypes:
                        layerlist.append(unicode(layer.name()))
                elif layer.type() == QgsMapLayer.RasterLayer:
                    if "Raster" in vTypes:
                        layerlist.append(unicode(layer.name()))
        return sorted(layerlist, cmp=locale.strcoll)

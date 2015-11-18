# -*- coding: utf8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtXml
from qgis.core import *
from qgis.gui import *

import time, os, json, locale

class QVerisoUtils: 
    def getChecks(self, submodule, topicName = None):
        checks = []
        filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/modules/qveriso/submodules/"+submodule+"/gui/checks.xml"))
        try:
            file = open(filename,"r")
            xml = file.read()
            
            doc = QtXml.QDomDocument()
            doc.setContent(xml, True)  
            
            root = doc.documentElement()
            if root.tagName() != "checks":
                return
                
            node = root.firstChild()
            while not node.isNull():
                if node.toElement() and node.nodeName() == "check":
                    check = {}
                    id = node.toElement().attribute("id","")
                    title = node.toElement().attribute("title",  "")
                    group = node.toElement().attribute("group",  "")
                    topic = node.toElement().attribute("topic",  "")
                    type = node.toElement().attribute("type",  "")                
                    check["id"] = id
                    check["title"] = unicode(title)
                    check["group"] = group
                    check["topic"] = topic
                    check["type"] = type
                    
                    if topic <> topicName and topicName <> None:
                        node = node.nextSibling()
                        continue
                    
                    layers = []
                    infoNode = node.toElement().firstChild()
                    while not infoNode.isNull():
                        if infoNode.toElement() and infoNode.nodeName() == "layer":
                            layer = {}
                            # Da wir die Layer einzeln hinzüfügen und die
                            # normale doShowSimpleLayer-Funktion 
                            # benützen, müssen wir die Gruppe auch den
                            # Layer-Infos hinzufügen.
                            layer["group"] = group
                            layernode = infoNode.toElement().firstChild()
                            while not layernode.isNull():
                                layer[str(layernode.nodeName())] = layernode.toElement().text()
                                layernode = layernode.nextSibling()
                            layers.append( layer )
                            
                        elif infoNode.toElement() and infoNode.nodeName() == "file":
                            complexFile = infoNode.toElement().text()
                            check["file"] = complexFile
                            
                        elif infoNode.toElement() and infoNode.nodeName() == "shortcut":
                            shortcut = infoNode.toElement().text()
                            check["shortcut"] = shortcut
                            
                        infoNode = infoNode.nextSibling()
                    if type == "simple":
                        check["layers"] = layers
                
                checks.append( check ) 
                node = node.nextSibling()
                
        except IOError:
            print "error opening checks.xml"        
            return None
            
        return checks

    
    def getCheckTopicsName(self, submodule):
        availableCheckTopics = []
        filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/modules/qveriso/submodules/"+submodule+"/gui/checks.xml"))
        try:
            file = open(filename,"r")
            xml = file.read()
            
            doc = QtXml.QDomDocument()
            doc.setContent(xml,  True)  
            
            root = doc.documentElement()
            if root.tagName() != "checks":
                return
                
            node = root.firstChild()
            while not node.isNull():
                if node.toElement() and node.nodeName() == "check":
                    topic = node.toElement().attribute("topic",  "")
                    availableCheckTopics.append(str(topic))
                    
                node = node.nextSibling()
                
        except IOError:
            print "error opening checks.xml"        
            #messagebox
            return None
            
        # remove duplicates
        u = []
        for x in availableCheckTopics:
            if x not in u:
                u.append(x)
        return u

    
    def getBaselayers(self, submodule):
        baselayers = []
        filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/modules/qveriso/submodules/"+submodule+"/gui/baselayers.xml"))
        try:
            layersfile = open(filename,"r")
            layersxml = layersfile.read()
            
            doc = QtXml.QDomDocument()
            doc.setContent(layersxml,  True)  
            
            root = doc.documentElement()
            if root.tagName() != "baselayers":
                return
                
            node = root.firstChild()
            while not node.isNull():
                if node.toElement() and node.nodeName() == "baselayer":
                    baselayer = {}
                    id = node.toElement().attribute("id","")
                    title = node.toElement().attribute("title",  "")
                    type = node.toElement().attribute("type",  "")
                    baselayer["id"] = id
                    baselayer["title"] = unicode(title)
                    baselayer["type"] = type

                    infoNode = node.toElement().firstChild()
                    while not infoNode.isNull():
                        baselayer[str(infoNode.nodeName())] = infoNode.toElement().text()
                        infoNode = infoNode.nextSibling()
                
                baselayers.append(baselayer)
                node = node.nextSibling()
                
        except IOError:
            print "error opening baselayers.xml"        
            # messagebox
            return None
            
        return baselayers


    def getTopics(self, submodule):
        topics = []
        filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/modules/qveriso/submodules/"+submodule+"/gui/topics.xml"))
        try:
            file = open(filename,"r")
            xml = file.read()
            
            doc = QtXml.QDomDocument()
            doc.setContent(xml,  True)  
            
            root = doc.documentElement()
            if root.tagName() != "topics":
                return
                
            node = root.firstChild()
            while not node.isNull():
                if node.toElement() and node.nodeName() == "topic":
                    topic = {}
                    id = node.toElement().attribute("id","")
                    title = node.toElement().attribute("title",  "")
                    group = node.toElement().attribute("group",  "")
                    topic["id"] = id
                    topic["title"] = title
                    topic["group"] = group
                    
                    tables = []
                    infoNode = node.toElement().firstChild()
                    while not infoNode.isNull():
                        if infoNode.toElement() and infoNode.nodeName() == "table":
                            table = {}
                            tablenode = infoNode.toElement().firstChild()
                            while not tablenode.isNull():
                                table[str(tablenode.nodeName())] = tablenode.toElement().text()
                                tablenode = tablenode.nextSibling()
                            tables.append( table )
                        infoNode = infoNode.nextSibling()
                    topic["tables"] = tables
                    topics.append(topic)
                node = node.nextSibling()
                
        except IOError:
            print "error opening topics.xml"
            # messagebox
            return None
        
        return topics

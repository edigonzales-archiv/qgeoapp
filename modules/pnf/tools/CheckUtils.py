# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtXml
from qgis.core import *
from qgis.gui import *

import time, os, json, locale, sys

import collections

class CheckUtils: 

    def getVerificationTopics(self):
        settings = QSettings("CatAIS","QGeoApp")
        module_name = (settings.value("project/active/module")).toString()
        print module_name
        
        filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/modules/pnf/"+str(module_name)+"/verification/verification.json"))
        
        if not filename:
            QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "No verification file found."))
            return        
            
        try:
            try:
                verifications = json.load(open(filename), object_pairs_hook=collections.OrderedDict) 
            except:
                verifications = json.load(open(filename)) 
            return verifications["verification"]
        except Exception, e:
            print "Couldn't do it: %s" % e        
            QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Failed to load verification file."))
            return

    def getVerifications(self, verificationfile):
        settings = QSettings("CatAIS","QGeoApp")
        module_name = (settings.value("project/active/module")).toString()
    
        filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/modules/pnf/"+module_name+"/verification/"+verificationfile+".json"))
        
        if not filename:
            QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "No verification file found."))
            return        
        
        try:
            try:
                verifications = json.load(open(filename), object_pairs_hook=collections.OrderedDict) 
            except:
                verifications = json.load(open(filename)) 
            return verifications["verification"]
        except Exception, e:
            print "Couldn't do it: %s" % e        
            QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "Failed to load verification file."))
            return

    def getTopics(self):
        filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/modules/pnf/gui/checks.json"))
        
        if filename == "" or filename == None:
            QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "No check file found."))
            return False        
            
        try:
            checks = json.load(open(filename)) 
        except:
            return False

        sortedChecks= sorted(checks["checks"], key=lambda k: str(k['topic_order'])) 

        try:
            topics = {}
            topicNames = []
            for check in sortedChecks:
                topic = check["topic"]
                if topics.has_key(topic):
                    continue
                topics[topic] = topic
                topicNames.append(topic)
        
            return topicNames
        except:
            return False


    def getChecksByTopic(self, topic):
        filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/modules/pnf/gui/checks.json"))
        
        if filename == "" or filename == None:
            QMessageBox.warning(None, "QGeoAppModule.PNF",  QCoreApplication.translate("QGeoAppModule.PNF", "No check file found."))
            return False        
            
        try:
            checks = json.load(open(filename)) 
        except:
            return False
            
        sortedChecks= sorted(checks["checks"], key=lambda k: str(k['order']))             
            
        try:
            topicChecks = []
            for check in sortedChecks:
                if topic == check["topic"]:
                    topicChecks.append(check)
                
            return topicChecks
        except:
            return False
            

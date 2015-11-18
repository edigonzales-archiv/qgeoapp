 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from qgis.core import *
from qgis.gui import *
from qgeoapp.modules.qveriso.tools.qverisoutils import QVerisoUtils


def featureFormInit(dialog, layerid, featureid): 
    
    settings = QSettings("CatAIS","QGeoApp")
    submodule = str(settings.value("project/active/submodule").toString())
    
    vutils = QVerisoUtils()
    topics = vutils.getTopics(submodule)
    
    ebene  = dialog.findChild(QComboBox,  "ebene")
    for i in range(len(topics)):
        ebene.insertItem( i, topics[i]["title"] )
    
    ebene.insertItem(0,  "--------------------")
    ebene.setCurrentIndex(0)
    
    dateWidget = dialog.findChild(QDateEdit, "dateEdit")
    dateWidget.setDate(QDateTime.currentDateTime().date())
        

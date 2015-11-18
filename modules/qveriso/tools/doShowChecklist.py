# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from doChecklist import ChecklistDialog

import time, os, shutil

class ShowChecklist(QObject):
    def __init__(self, iface, projectId, projectRootPath, submodule):
        self.iface = iface
        self.projectId = projectId
        self.projectRootPath = projectRootPath
        self.submodule = submodule


    def run(self):
        try:
            # Pruefen ob Checkliste bereits existiert.
            checklistdir =  QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + '/python/plugins/qgeoapp/modules/qveriso/submodules/'+self.submodule+'/checklists/'))
            print checklistdir
            checklisthtml =  self.projectId + ".html"
            
            print checklistdir + os.sep + checklisthtml
            
            if os.path.isfile(checklistdir + os.sep + checklisthtml):
                print "Checklist found."
            else: 
                shutil.copy(checklistdir + os.sep+ 'default.html', checklistdir + os.sep + checklisthtml)
            
            d = ChecklistDialog(self.iface.mainWindow(), checklistdir, checklisthtml, self.projectId, self.projectRootPath)
            d.resize(1000,700);     
            d.show()
        
        except IOError:
            print "VeriSO: checkliste copy error"
            #messagebox

        

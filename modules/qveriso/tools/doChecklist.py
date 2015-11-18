# -*- coding: latin1 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from Ui_checklist import Ui_Checklist
import os, time

class ChecklistDialog(QDialog, QObject, Ui_Checklist):
    def __init__(self, iface, checklistDir, checklistHtml, projectId, projectRootPath):
        QDialog.__init__(self, iface)
        self.iface = iface
        self.setupUi(self)
                
        self.checklistHtml = checklistHtml
        self.projectId = projectId
        self.projectRootPath = projectRootPath
        
        self.webView.settings().enablePersistentStorage()
        self.webView.load(QUrl(checklistDir + os.sep + checklistHtml))      
        print str(checklistDir + os.sep + checklistHtml)
    
    @pyqtSignature("on_btnPDF_clicked()")    
    def on_btnPDF_clicked(self):
        tempdir = self.projectRootPath + os.sep + self.projectId
    
        printer = QPrinter()
        printer.setPageSize(QPrinter.A4)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(tempdir + os.sep + self.checklistHtml.replace("html", "pdf"))

        self.webView.print_(printer)
        print "Pdf generated"
        
        if os.path.isfile( tempdir + os.sep + self.checklistHtml.replace("html", "pdf") ):
            QMessageBox.information( None, "", "Checkliste erzeugt: " + tempdir + os.sep + self.checklistHtml.replace("html", "pdf"))
        else:
             QMessageBox.warning( None, "", "Fehler beim Erzeugen des PDF.")


    @pyqtSignature("on_btnClose_clicked()")    
    def on_btnClose_clicked(self):
        self.close()

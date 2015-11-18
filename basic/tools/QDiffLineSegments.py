# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtXml
from qgis.core import *
from qgis.gui import *
from QLineSegment import QLineSegment

class QDiffLineSegments(QObject): 
    def __init__(self, iface, vlayer1, vlayer2):
        QObject.__init__(self, iface.mainWindow())        
        self.vlayer1 = vlayer1
        self.vlayer2 = vlayer2
        self.edges = {}
        
    def run(self):
        self.getEdges(self.vlayer1)
        
        print len(self.edges.keys())

    def getEdges(self, vlayer):
        print "getEdges"
        provider = vlayer.dataProvider()
        feat = QgsFeature()
        allAttrs = provider.attributeIndexes()
        provider.select(allAttrs)
        
        while provider.nextFeature(feat):
            geom = feat.geometry()
            wkbtype=geom.wkbType()
            if wkbtype in [QGis.WKBLineString,QGis.WKBLineString25D]:
                self.splitline(geom.asPolyline())
            if wkbtype in [QGis.WKBMultiLineString,QGis.WKBMultiLineString25D]:
                for line in geom.asMultiPolyline():
                    self.splitline(line)
            if wkbtype in [QGis.WKBPolygon,QGis.WKBPolygon25D]:
                for line in geom.asPolygon():
                    self.splitline(line)
            if wkbtype in [QGis.WKBMultiPolygon,QGis.WKBMultiPolygon25D]:
                for poly in geom.asMultiPolygon():
                    for line in poly:
                        self.splitline(line)
                        
    
    def splitline(self, line):
        for i in range(1, len(line)):
            myLine = line[i-1:i+1]
            p1 = myLine[0]
            p2 = myLine[1]
                        
            if p1.x() > p2.x():
                pt = QgsPoint(p1.x(), p1.y())
                p1 = QgsPoint(p2.x(), p2.y())
                p2 = QgsPoint(pt.x(), pt.y())
                
#            newline = QgsGeometry.fromPolyline([p1, p2])
            
            segment = QLineSegment(p1, p2)



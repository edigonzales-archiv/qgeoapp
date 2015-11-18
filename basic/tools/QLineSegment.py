# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtXml
from qgis.core import *
from qgis.gui import *

class QLineSegment(): 
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def __hash__(self):
        return hash((self.p1.x(), self.p1.y(), self.p2.x(), self.p2.y()))
        
    def __eq__(self, other):
        dx1 = abs(self.p1.x() - other.p1.x())
        dy1 = abs(self.p1.y() - other.p1.y())
        dx2 = abs(self.p2.x() - other.p2.x())
        dy2 = abs(self.p2.y() - other.p2.y())
        
#        if dx1 == 0:
#            print "dx1"
#        
#        if dy1 == 0:
#            print "dy1"
#
#        if dx2 == 0:
#            print "dx2"
#
#        if dy1 == 0:
#            print "dy2"
            
#        if dx1 == 0 and dy1 == 0 and dx2 == 0 and dy2 == 0:
#            print "true"
#            return True
#        else:
#            print "false"
#            return False
        return (dx1, dy1, dx2, dy2) == (0, 0, 0, 0)
        


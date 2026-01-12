# -*- coding: utf-8 -*-
"""
@author: msardar2

PFAS_SAT
"""
try:
    from .GUI.PFAS_SAT_run import MyQtApp
    from PySide6 import QtWidgets
    from PySide6.QtGui import QGuiApplication
except ImportError:
    print("GUI is not imported")
import sys

# Import Main
from PFAS_SAT.Project import Project
from PFAS_SAT.MCResults import MCResults


__all__ = ['MyQtApp',
           'PFAS_SAT',
           'Project',
           'MCResults']

__version__ = '0.3.2'


class PFAS_SAT():
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.qt_app = MyQtApp()
        # Use modern screen API instead of deprecated desktop()
        screen = QGuiApplication.primaryScreen()
        availableGeometry = screen.availableGeometry()
        self.qt_app.resize(int(availableGeometry.width() * 2 / 3), int(availableGeometry.height() * 2.85 / 3))
        self.qt_app.show()
        self.app.exec()

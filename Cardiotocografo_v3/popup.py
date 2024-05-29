# -*- coding: utf-8 -*-
#
#@author: Juan Darío Muñoz Soto
#
#@version: 2.0 
#
#@date: 02-01-2014
#
#@summary: Clase UI_Dialog donde se definen y inicializa la interfaz grafica 
#
#@note: Modelos matematicos por: Curso 'Identificación de modelos parametricos' - Magister en Ingeniería UACh
#
#@copyright: Todos los derechos reservados por Laboratorio I+D, Alfredo Illanes, Francisco Guerra, etc
#
#@warning: All changes made in this file will be lost!
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class emergente(object):
    def setup_ventana(self, Ventana):
        Ventana.setObjectName(_fromUtf8("Ventana"))
        Ventana.resize(400, 300)
        Ventana.setMouseTracking(False)
        Ventana.setWindowIcon(QtGui.QIcon('fetal_icon.png'))
        
        self.label_p1 = QtGui.QLineEdit(Ventana)
        self.label_p1.setGeometry(QtCore.QRect(100, 15, 100, 20))
        
        self.linea = QtGui.QLineEdit(Ventana)
        self.linea.setGeometry(QtCore.QRect(100, 100, 100, 20))
        self.boton = QtGui.QPushButton(Ventana)
        self.boton.setGeometry(QtCore.QRect(150, 160, 101, 41))
        
        self.retranslateUi(Ventana)
        QtCore.QMetaObject.connectSlotsByName(Ventana)

    def retranslateUi(self, Ventana):
        Ventana.setWindowTitle(_translate("Ventana", "Estado final", None))   
        
        self.label_p1(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Amplitud Variabilidad:</span></p></body></html>", None))
        self.boton.setText(_translate("Ventana", "Mostrar", None))
        

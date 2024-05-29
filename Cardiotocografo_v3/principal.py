# -*- coding: utf-8 -*-
#
#@author: Juan Darío Muñoz Soto
#
#@version: 2.0 
#
#@date: 02-01-2014
#
#@summary: Clase principal GUIForm que contiene metodos para graficar y metodos de Interfaz Humano Computador
#
#@note: Modelos matematicos por: Curso 'Identificación de modelos parametricos' - Magister en Ingeniería UACh
#
#@copyright: Todos los derechos reservados por Laboratorio I+D, Alfredo Illanes, Francisco Guerra, etc
#
#@warning: All changes made in this file will be lost!
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from __future__ import division
import sys 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PlotGuiFinal5 import *
from popup import *
from functools import partial
import numpy as np
import scipy as sc
import numpy.fft
import ctypes
import time
import sip
import pyqtgraph as pg
from scipy.special import _ufuncs_cxx
from scipy.sparse.csgraph import _validation
import six
import funciones_FHR
import funciones_CU
import funciones_DIP
import threading
import logging
import numbers
import ctypes

myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class MyPopupDialog(QtGui.QDialog):
    
    '''Metodo Inicial de la clase'''
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui2 = emergente()
        self.ui2.setup_ventana(self)
        sip.setdestroyonexit(False)
        self.setWindowFlags( QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowMinMaxButtonsHint | QtCore.Qt.WindowCloseButtonHint )

    def get_popup(self):
        word = self.ui2.linea.text()
        return word

class GUIForm(QtGui.QDialog):
    
    '''Metodo inicial de la clase********************************************************************************************************'''

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        sip.setdestroyonexit(False)
        self.setWindowFlags( QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowMinMaxButtonsHint | QtCore.Qt.WindowCloseButtonHint )
        self.setWindowState(QtCore.Qt.WindowMaximized)
  
        
        #user32 = ctypes.windll.user32
        #screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        #print screensize
        #QtCore.QObject.connect(self.ui.graphicsView, QtCore.SIGNAL('onCLick()'), self.sizeGrafico)
        
        QtCore.QObject.connect(self.ui.pushButton_s1, QtCore.SIGNAL('clicked()'), self.popup)
        
        QtCore.QObject.connect(self.ui.pushButton_s2, QtCore.SIGNAL('clicked()'), self.impulso)
        QtCore.QObject.connect(self.ui.horizontalSlider_s1, QtCore.SIGNAL('valueChanged(int)'), self.agregar)
        
        '''funcion habilitaLineEdit para cada contraccion'''
        QtCore.QObject.connect(self.ui.comboBox_s1, QtCore.SIGNAL('activated(QString)'), self.habilitaLineEdit)
        QtCore.QObject.connect(self.ui.comboBox_s2, QtCore.SIGNAL('activated(QString)'), self.habilitaLineEdit)
        QtCore.QObject.connect(self.ui.comboBox_s3, QtCore.SIGNAL('activated(QString)'), self.habilitaLineEdit)
        QtCore.QObject.connect(self.ui.comboBox_s4, QtCore.SIGNAL('activated(QString)'), self.habilitaLineEdit)
        QtCore.QObject.connect(self.ui.comboBox_s5, QtCore.SIGNAL('activated(QString)'), self.habilitaLineEdit)
        QtCore.QObject.connect(self.ui.comboBox_s6, QtCore.SIGNAL('activated(QString)'), self.habilitaLineEdit)
        QtCore.QObject.connect(self.ui.comboBox_s7, QtCore.SIGNAL('activated(QString)'), self.habilitaLineEdit)
        QtCore.QObject.connect(self.ui.comboBox_s8, QtCore.SIGNAL('activated(QString)'), self.habilitaLineEdit)
        
        QtCore.QObject.connect(self.ui.comboBox_s9, QtCore.SIGNAL('activated(QString)'), self.combo_chosen)
        #QtCore.QObject.connect(self.ui.comboBox_hrstd, QtCore.SIGNAL('activated(QString)'), self.combo_hrstd)
        '''Ahora no existe combo_hrstd sino escribeLabel'''
        QtCore.QObject.connect(self.ui.lineEdit_s4, QtCore.SIGNAL(("textChanged(QString)")), self.combo_hrstd)
        
        
        #QtCore.QObject.connect(self.ui.lineEdit_s13, QtCore.SIGNAL(("textChanged(QString)")), self.gravedadDip,"1")
        QtCore.QObject.connect(self.ui.lineEdit_s13, QtCore.SIGNAL(("textChanged(QString)")), partial(self.gravedadDip,1))
        QtCore.QObject.connect(self.ui.lineEdit_s14, QtCore.SIGNAL(("textChanged(QString)")), partial(self.gravedadDip,2))
        QtCore.QObject.connect(self.ui.lineEdit_s15, QtCore.SIGNAL(("textChanged(QString)")), partial(self.gravedadDip,3))
        QtCore.QObject.connect(self.ui.lineEdit_s16, QtCore.SIGNAL(("textChanged(QString)")), partial(self.gravedadDip,4))
        QtCore.QObject.connect(self.ui.lineEdit_s17, QtCore.SIGNAL(("textChanged(QString)")), partial(self.gravedadDip,5))
        QtCore.QObject.connect(self.ui.lineEdit_s18, QtCore.SIGNAL(("textChanged(QString)")), partial(self.gravedadDip,6))
        QtCore.QObject.connect(self.ui.lineEdit_s19, QtCore.SIGNAL(("textChanged(QString)")), partial(self.gravedadDip,7))
        QtCore.QObject.connect(self.ui.lineEdit_s20, QtCore.SIGNAL(("textChanged(QString)")), partial(self.gravedadDip,8))
        
        
        QtCore.QObject.connect(self.ui.lineEdit_s21, QtCore.SIGNAL(("textChanged(QString)")), partial(self.gravedadDip,1))
        QtCore.QObject.connect(self.ui.lineEdit_s22, QtCore.SIGNAL(("textChanged(QString)")), partial(self.gravedadDip,2))
        QtCore.QObject.connect(self.ui.lineEdit_s23, QtCore.SIGNAL(("textChanged(QString)")), partial(self.gravedadDip,3))
        QtCore.QObject.connect(self.ui.lineEdit_s24, QtCore.SIGNAL(("textChanged(QString)")), partial(self.gravedadDip,4))
        QtCore.QObject.connect(self.ui.lineEdit_s25, QtCore.SIGNAL(("textChanged(QString)")), partial(self.gravedadDip,5))
        QtCore.QObject.connect(self.ui.lineEdit_s26, QtCore.SIGNAL(("textChanged(QString)")), partial(self.gravedadDip,6))
        QtCore.QObject.connect(self.ui.lineEdit_s27, QtCore.SIGNAL(("textChanged(QString)")), partial(self.gravedadDip,7))
        QtCore.QObject.connect(self.ui.lineEdit_s28, QtCore.SIGNAL(("textChanged(QString)")), partial(self.gravedadDip,8))
        
        QtCore.QObject.connect(self.ui.checkBox_s3, QtCore.SIGNAL('clicked()'), self.pulsaCheckMF)
        QtCore.QObject.connect(self.ui.checkBox_s4, QtCore.SIGNAL('clicked()'), self.pulsaCheckCU)
        QtCore.QObject.connect(self.ui.checkBox_s2, QtCore.SIGNAL('clicked()'), self.cambiaCmMin)
        QtCore.QObject.connect(self.ui.checkBox_s1, QtCore.SIGNAL('clicked()'), self.pulsaCheckDinamic)
        QtCore.QObject.connect(self.ui.radioButton_s3, QtCore.SIGNAL("toggled(bool)"), self.call_Consult)
        QtCore.QObject.connect(self.ui.radioButton_s4, QtCore.SIGNAL("toggled(bool)"), self.call_Consult)
        QtCore.QObject.connect(self.ui.radioButton_s3, QtCore.SIGNAL("toggled(bool)"), self.call_Consult)
        QtCore.QObject.connect(self.ui.radioButton_s5, QtCore.SIGNAL("toggled(bool)"), self.call_Consult)
        
        ticks1 = []
        ticks2 = []
        subticks = []
        subtickscu = []
        
        for i in range(0, 1200+1,30):
            tupla = (i,'')
            ticks2.append(tupla)
        
        for i in range(0, 1200+1,180):
            tupla = (i,'')
            ticks1.append(tupla)
        
        for i in range(30,240+1,10):
            if((i%30)!=0):
                subtupla = (i,'')
                subticks.append(subtupla)
        
        for i in range(5,100+1,5):
            if((i%25)!=0):
                subtupla = (i,'')
                subtickscu.append(subtupla)
        
        self.w1 = self.ui.graphicsView.addPlot()
        #self.w1.plot(self.t,HRV, pen=pg.mkColor(0,0,0))
        #self.curveHRV = self.w1.plot(pen=pg.mkColor(0,0,0))
        self.w1.setXRange(0, 1200, padding=0)
        self.w1.setYRange(30, 240, padding=0)
        self.w1.showGrid(x=True, y=True)
        self.w1.getAxis('left').setPen('r')
        self.w1.getAxis('bottom').setPen('r')
        self.w1.setMouseEnabled(y = False)
        self.w1.getAxis('bottom').setTicks([ticks1, ticks2])
        
        self.w1.getAxis('left').setTicks([[(30,'30'),(60,'60'),(90,'90'),(120,'120'),(150,'150'),(180,'180'),(210,'210'),(240,'240')],subticks])
        self.w1.getAxis('left').setWidth(30)
        self.ui.graphicsView.nextRow()
        
        self.w2 = self.ui.graphicsView.addPlot()
        #self.w2.plot(ttot,piu, pen=pg.mkColor(0,0,0))
        #self.curveCON = self.w2.plot(pen=pg.mkColor(0,0,0))
        self.w2.setXRange(0, 1200, padding=0)
        self.w2.setYRange(0, 100, padding=0)
        self.w2.showGrid(x=True, y=True)
        self.w2.getAxis('left').setPen('r')
        self.w2.getAxis('bottom').setPen('r')
        self.w2.setMouseEnabled(y = False)
        
        self.w2.getAxis('bottom').setTicks([ticks1,ticks2])
        #self.w2.getAxis('left').setTicks([[(0,'0'),(25,'25'),(50,'50'),(75,'75'),(100,'100')],[(10,''),(20,''),(40,''),(50,''),(70,''),(10,'')],subtickscu])
        self.w2.getAxis('left').setTicks([[(0,'0'),(25,'25'),(50,'50'),(75,'75'),(100,'100')],subtickscu])
        self.w2.getAxis('left').setWidth(30)
        for i in range(1,9):
            exec("self.ui.comboBox_s"+str(i)+".addItems(['Ninguna','Temprana', 'Tardia', 'Variable', 'Prolongada'])")
        
        for i in range(1,9):
            exec("self.ui.label_s1"+str(i)+".hide()")
            exec("self.ui.comboBox_s"+str(i)+".hide()")
            exec("self.ui.lineEdit_s"+str(i+4)+".hide()")
            exec("self.ui.lineEdit_s"+str(i+12)+".hide()")
            exec("self.ui.lineEdit_s"+str(i+20)+".hide()")
            exec("self.ui.label_s"+str(i+25)+".hide()")
        
        for i in range(1,9):
            exec("self.ui.lineEdit_s"+str(i+12)+".setEnabled(False)")
            exec("self.ui.lineEdit_s"+str(i+20)+".setEnabled(False)")
        
        
        self.ui.comboBox_s9.addItems(["1x","2x","4x","8x",'16x'])
        #self.ui.comboBox_hrstd.addItems(['Indetectable','Disminuida','Moderada','Marcada'])
        self.ui.progressBar.setProperty("value", 0)
        self.ui.progressBar.hide()
        self.mostrados = 0
        self.ui.pushButton_s2.setEnabled(False)
        self.ui.pushButton_s2.hide()
        self.ui.comboBox_s9.setEnabled(False) 
        
        self.Timpulso = 0
        self.Tscu = 0
        self.tiempo = 0
        self.veloc = self.asignar(self.ui.comboBox_s9.currentIndex())
        self.hrstd = 0
        self.generated = 0
        self.contHRV=0
        self.ui.checkBox_s2.setEnabled(False)
        self.tsimforcm = 0
        self.hrmean = 0
        
    
    '''**************************************************************************************************************************************'''
    def popup(self):
        self.ventana_pop = MyPopupDialog()
        QtCore.QObject.connect(self.ventana_pop.ui2.boton, QtCore.SIGNAL('clicked()'), self.get_popup)
        self.ventana_pop.show()
        #self.ventana_pop.exec_()
        
    def get_popup(self):
        word = self.ventana_pop.get_popup()
        print word
    
    '''Funcion que escucha cuando cambia el combobox de la velocidad ************************************************************************'''
    def combo_chosen(self):
        a = self.ui.comboBox_s9.currentIndex()
        self.veloc = self.asignar(a)
        self.timer.start(self.veloc)
        
    '''Función para cambiar la grilla de 1cm/min a 3cm/min y viceversa'''
    def cambiaCmMin(self):
        if self.ui.checkBox_s2.isChecked():
            self.ui.label_s24.setText('3 cm/min')
            ticks1 = []
            ticks2 = []
            
            for i in range(0, self.tsimforcm+1,180):
                tupla = (i,'')
                ticks1.append(tupla)
            
            for i in range(0, self.tsimforcm+1,10):
                tupla = (i,'')
                ticks2.append(tupla)
            
            self.w1.setXRange(0, 240, padding=0)
            self.w2.setXRange(0, 240, padding=0)
            self.w1.getAxis('bottom').setTicks([ticks1,ticks2])
            self.w2.getAxis('bottom').setTicks([ticks1,ticks2])
            
        else:
            self.ui.label_s24.setText('1 cm/min')
            ticks1 = []
            ticks2 = []
            
            for i in range(0, self.tsimforcm+1,180):
                tupla = (i,'')
                ticks1.append(tupla)
            
            for i in range(0, self.tsimforcm+1,30):
                tupla = (i,'')
                ticks2.append(tupla)
            
            self.w1.getAxis('bottom').setTicks([ticks1,ticks2])
            self.w2.getAxis('bottom').setTicks([ticks1,ticks2]) 
            self.w1.setXRange(0, 1200, padding=0)
            self.w2.setXRange(0, 1200, padding=0)
        
    '''Funcion que modifica el label segun las profundidad de la dip ******************************************************'''
    def gravedadDip(self,j):
        desa = 0
        dura = ""
        profu = ""
        exec("desa = self.ui.comboBox_s"+str(j)+".currentIndex()")
        #exec("dura = self.ui.lineEdit_s"+str(j+12)+".text()")
        #exec("profu = self.ui.lineEdit_s"+str(j+20)+".text()")
        
        if(desa == 1 or desa == 0):
            exec("self.ui.label_s"+str(j+25)+".setText('        ')")
        #Obtiene la duración de las Dip que generan las contracciones
        
        if ( desa == 2 or desa == 4):
            exec("profu = self.ui.lineEdit_s"+str(j+20)+".text()")
            
            try:
                profu = int(profu)
                self.hrmean = self.ui.lineEdit_s3.text()
                des = int(self.hrmean) - profu
                if (des > 0 and des < 15):
                    exec("self.ui.label_s"+str(j+25)+".setText('leve')")
                elif(des > 15 and des <45):
                    exec("self.ui.label_s"+str(j+25)+".setText('moderada')")
                elif(des > 45):
                    exec("self.ui.label_s"+str(j+25)+".setText('severa')")
            except:
                exec("self.ui.label_s"+str(j+25)+".setText('        ')")
                
        if ( desa == 3 ):
            exec("dura = self.ui.lineEdit_s"+str(j+12)+".text()")
            exec("profu = self.ui.lineEdit_s"+str(j+20)+".text()")
            print dura, profu
            try:
                dura = int(dura)
                profu = int(profu)
                
                if (dura > 0 and dura < 30 ):
                    exec("self.ui.label_s"+str(j+25)+".setText('leve')")
                elif (dura >= 30 and dura < 60):
                    if(profu > 70 ):
                        exec("self.ui.label_s"+str(j+25)+".setText('leve')")
                    else:
                        exec("self.ui.label_s"+str(j+25)+".setText('moderada')")
                        print "estoy"
                if (dura >= 60 and dura < 120 ):
                    if(profu > 80 ):
                        exec("self.ui.label_s"+str(j+25)+".setText('leve')")
                    elif(profu >= 70 and profu <= 80):
                        exec("self.ui.label_s"+str(j+25)+".setText('moderada')")
                    elif (profu < 70):
                        exec("self.ui.label_s"+str(j+25)+".setText('severa')")
            except:
                exec("self.ui.label_s"+str(j+25)+".setText('        ')")
    
    
    '''Funcion que escucha cuando cambia el combobox de la amplitud de la variabilidad ******************************************************'''
    def combo_hrstd(self):
        self.hrstd  = self.ui.lineEdit_s4.text()
        if self.hrstd == "": 
            return "Ingrese Variabilidad"
        else:
            try:
                #verifica que sea un número
                self.hrstd = float(self.hrstd)
                if (self.hrstd >= 0 and self.hrstd < 2):
                    self.ui.label_s5.setText("Indetectable")
                elif (self.hrstd >= 2 and self.hrstd < 5):
                    self.ui.label_s5.setText("Minima")
                elif (self.hrstd >= 5 and self.hrstd <= 25):
                    self.ui.label_s5.setText("Moderada")
                elif(self.hrstd > 25 and self.hrstd < 51):
                    self.ui.label_s5.setText("Marcada")
                else:
                    self.ui.label_s5.setText("")
            except:
                return "Ingrese un numero valido para Variabilidad"
        
        #self.hrstd = self.ui.comboBox_hrstd.currentIndex()
        
    '''Funcion que hace aparecer las horizontalSliders de las desaceleraciones *****************************************************************'''        
    def habilitaLineEdit(self):
        if self.ui.comboBox_s1.currentIndex() > 1:
            self.ui.lineEdit_s21.setEnabled(True)
            if self.ui.comboBox_s1.currentIndex() > 2:
                self.ui.lineEdit_s13.setEnabled(True)
            else:
                self.ui.lineEdit_s13.setEnabled(False)
        else:
            self.ui.lineEdit_s13.setEnabled(False)
            self.ui.lineEdit_s21.setEnabled(False)
        
        if self.ui.comboBox_s2.currentIndex() > 1:
            self.ui.lineEdit_s22.setEnabled(True)
            if self.ui.comboBox_s2.currentIndex() > 2:
                self.ui.lineEdit_s14.setEnabled(True)
            else:
                self.ui.lineEdit_s14.setEnabled(False)
        else:
            self.ui.lineEdit_s14.setEnabled(False)
            self.ui.lineEdit_s22.setEnabled(False)
            
        if self.ui.comboBox_s3.currentIndex() > 1:
            self.ui.lineEdit_s23.setEnabled(True)
            if self.ui.comboBox_s3.currentIndex() > 2:
                self.ui.lineEdit_s15.setEnabled(True)
            else:
                self.ui.lineEdit_s15.setEnabled(False)
        else:
            self.ui.lineEdit_s15.setEnabled(False)
            self.ui.lineEdit_s23.setEnabled(False)
            
        if self.ui.comboBox_s4.currentIndex() > 1:
            self.ui.lineEdit_s24.setEnabled(True)
            if self.ui.comboBox_s4.currentIndex() > 2:
                self.ui.lineEdit_s16.setEnabled(True)
            else:
                self.ui.lineEdit_s16.setEnabled(False)
        else:
            self.ui.lineEdit_s16.setEnabled(False)
            self.ui.lineEdit_s24.setEnabled(False)
            
        if self.ui.comboBox_s5.currentIndex() > 1:
            self.ui.lineEdit_s25.setEnabled(True)
            if self.ui.comboBox_s5.currentIndex() > 2:
                self.ui.lineEdit_s17.setEnabled(True)
            else:
                self.ui.lineEdit_s17.setEnabled(False)
        else:
            self.ui.lineEdit_s17.setEnabled(False)
            self.ui.lineEdit_s25.setEnabled(False)
            
        if self.ui.comboBox_s6.currentIndex() > 1:
            self.ui.lineEdit_s26.setEnabled(True)
            if self.ui.comboBox_s6.currentIndex() > 2:
                self.ui.lineEdit_s18.setEnabled(True)
            else:
                self.ui.lineEdit_s18.setEnabled(False)
        else:
            self.ui.lineEdit_s18.setEnabled(False)
            self.ui.lineEdit_s26.setEnabled(False)
            
        if self.ui.comboBox_s7.currentIndex() > 1:
            self.ui.lineEdit_s27.setEnabled(True)
            if self.ui.comboBox_s7.currentIndex() > 2:
                self.ui.lineEdit_s19.setEnabled(True)
            else:
                self.ui.lineEdit_s19.setEnabled(False)
        else:
            self.ui.lineEdit_s19.setEnabled(False)
            self.ui.lineEdit_s27.setEnabled(False)
            
        if self.ui.comboBox_s8.currentIndex() > 1:
            self.ui.lineEdit_s28.setEnabled(True)
            if self.ui.comboBox_s8.currentIndex() > 2:
                self.ui.lineEdit_s20.setEnabled(True)
            else:
                self.ui.lineEdit_s20.setEnabled(False)
        else:
            self.ui.lineEdit_s20.setEnabled(False)
            self.ui.lineEdit_s28.setEnabled(False)
        
        
        
        
    '''Funciones asociados a los checkBoxs y radioButtons para que aparezcan o desaparezacan segun la simulacion que se lance ***************'''        
    def pulsaCheckDinamic(self):
        if self.ui.checkBox_s1.isChecked() == False:
            self.ui.checkBox_s3.setEnabled(True)
            self.ui.checkBox_s4.setEnabled(True)
            if self.ui.checkBox_s4.isChecked():
                self.ui.radioButton_s1.setEnabled(True)
                self.ui.radioButton_s2.setEnabled(True)
                self.ui.radioButton_s3.setEnabled(True)
                self.ui.radioButton_s4.setEnabled(True)
                self.ui.radioButton_s5.setEnabled(True)
                if self.ui.radioButton_s2.isChecked() == False:
                    self.ui.lineEdit_s29.setEnabled(True)
                    self.ui.label_s22.setEnabled(True)
                    self.ui.lineEdit_s30.setEnabled(True)
                    self.ui.label_s23.setEnabled(True)
                    
        else:
            self.ui.checkBox_s3.setEnabled(False)
            self.ui.checkBox_s4.setEnabled(False)
            if self.ui.checkBox_s4.isChecked():
                self.ui.radioButton_s1.setEnabled(False)
                self.ui.radioButton_s2.setEnabled(False)
                self.ui.radioButton_s3.setEnabled(False)
                self.ui.radioButton_s4.setEnabled(False)
                self.ui.radioButton_s5.setEnabled(False)
                if self.ui.radioButton_3.isChecked() == False:
                    self.ui.lineEdit_s29.setEnabled(False)
                    self.ui.label_s22.setEnabled(False)
                    self.ui.lineEdit_s30.setEnabled(False)
                    self.ui.label_s23.setEnabled(False)
                        
        
    def pulsaCheckMF(self):
        if (self.ui.checkBox_s3.isChecked()):
            self.ui.checkBox_s4.setChecked(False)
            self.ui.radioButton_s1.hide()
            self.ui.radioButton_s2.hide()
            self.ui.radioButton_s3.hide()
            self.ui.radioButton_s4.hide()
            self.ui.radioButton_s5.hide()
            self.ui.lineEdit_s29.hide()
            self.ui.label_s22.hide()
            self.ui.lineEdit_s30.hide()
            self.ui.label_s23.hide()
            self.ui.pushButton_s2.show()
            
            
    def pulsaCheckCU(self):
        if (self.ui.checkBox_s4.isChecked()):
            self.ui.checkBox_s3.setChecked(False)
            self.ui.checkBox_s3.setEnabled(True)
            self.ui.radioButton_s1.show()
            self.ui.radioButton_s2.show()
            self.ui.radioButton_s3.show()
            self.ui.radioButton_s4.show()
            self.ui.radioButton_s5.show()
            self.ui.pushButton_s2.show()
            self.ui.radioButton_s1.setChecked(True)
    
    def call_Consult(self):
        if self.ui.radioButton_s1.isChecked() | self.ui.radioButton_s2.isChecked():
            self.ui.lineEdit_s29.hide()
            self.ui.label_s22.hide()
            self.ui.lineEdit_s30.hide()
            self.ui.label_s23.hide()
        elif self.ui.radioButton_s3.isChecked():
            self.ui.lineEdit_s29.setEnabled(False)
            self.ui.lineEdit_s29.show()
            self.ui.label_s22.show()
            self.ui.lineEdit_s30.show()
            self.ui.label_s23.show()
        else:
            self.ui.lineEdit_s29.show()
            self.ui.lineEdit_s29.setEnabled(True)
            self.ui.label_s22.show()
            self.ui.lineEdit_s30.show()
            self.ui.label_s23.show()
    
    '''Funcion que retorna el identificador de la desaceleracion en el radioButton'''    
    def getDip(self):
        if self.ui.radioButton_s2.isChecked():
            return 1
        elif self.ui.radioButton_s3.isChecked():
            return 2
        elif self.ui.radioButton_s4.isChecked():
            return 3
        elif self.ui.radioButton_s5.isChecked():
            return 4
        elif self.ui.radioButton_s1.isChecked():
            return 0
        
    '''Funcion que escucha cuando cambia el horizontalSlider que agrega contracciones******************************************************'''
    def agregar(self):
        self.cant = self.ui.horizontalSlider_s1.value()
        self.ui.label_s25.setText(str(self.cant))
        if self.cant >= self.mostrados:
            for i in range(0,self.cant):
                exec("self.ui.label_s1"+str(i+1)+".show()")
                exec("self.ui.lineEdit_s"+str(i+5)+".show()")
                exec("self.ui.comboBox_s"+str(i+1)+".show()")
                exec("self.ui.lineEdit_s"+str(i+13)+".show()")
                exec("self.ui.lineEdit_s"+str(i+21)+".show()")
                exec("self.ui.label_s"+str(i+26)+".show()")
                
                #exec("self.ui.horizontalSlider_"+str(i)+".show()")
                #exec("self.ui.label_"+str(i+4)+".show()")
            
                
        else:
            for i in range(self.cant,self.mostrados):
                exec("self.ui.label_s1"+str(i+1)+".hide()")
                exec("self.ui.lineEdit_s"+str(i+5)+".hide()")
                exec("self.ui.comboBox_s"+str(i+1)+".hide()")
                exec("self.ui.lineEdit_s"+str(i+13)+".hide()")
                exec("self.ui.lineEdit_s"+str(i+21)+".hide()")
                exec("self.ui.label_s"+str(i+26)+".hide()")
                
                #exec("self.ui.horizontalSlider_"+str(i)+".hide()")
                #exec("self.ui.label_"+str(i+4)+".hide()")
        self.mostrados = self.cant
        
    '''**************************************************************************************************************************************'''

            
    
    '''Funcion que asigna la velocidad segun el indice del combobox ************************************************************************'''

    def asignar(self,num):
        if (num == 0):
            return 1000
        elif (num == 1):
            return 500
        elif (num == 2):
            return 250
        elif (num ==3):
            return 125
        elif (num ==4):
            return 62.5
    
    '''Función que lanza la Simulacion preguntando primeramente si es Dinamica o Estática'''
    def impulso(self):
        if self.ui.checkBox_s3.isChecked():
            self.impulsoMF()
        else:
            self.impulsoCU()
    
    
    '''Funcion de un movimiento fetal generado por usuario, esta obtiene los datos y los suma a la señal original *******************''' 
    def impulsoMF(self):  
        try:
            print self.contHRV/250, 'tiempo'
            instante = self.contHRV/250
            entrega = funciones_FHR.mov_fetal(self.contHRV, 250)
            l = len(entrega)
            self.Timpulso = np.round(l/250)
            print self.Timpulso, 'self.Timpulso'
            self.HRV[self.contHRV:self.contHRV+l] = self.HRV[self.contHRV:self.contHRV+l] + entrega
            
            mf =np.array([instante])
            
            piu = funciones_CU.CuMf(mf,self.ttot,self.mfstd,self.fm, self.desv,self.u)
            
            self.piu = self.piu + piu
            
            return 0
        except:
            ctypes.windll.user32.MessageBoxA(0, 'Fin de simulacion! Movimiento fetal no realizado', "Alert", 1)
    
    
   
    '''Funcion contraccion generada por usuario, el mismo mecanismo que un Mov. Fetal *******************************************************'''
    def impulsoCU(self):
        try:
            instante = self.contCON/250
                
            scu = funciones_CU.con_user(self.u,self.desv,self.ad,self.fm)
            s = scu[0]
            D = np.array([(scu[1])])
            A = np.array([(scu[2])])
            Aprom = scu[3]
            l = len(s)
            self.Tscu = np.round(l/250)
            self.piu[self.contCON:self.contCON+l] = self.piu[self.contCON:self.contCON+l] + s
            
            T = np.array([instante])
            Ttipo = np.array([self.getDip()])
            if Ttipo[0] == 1:
                Tprof = np.array([])
                Tdur = np.array([])
                
            if Ttipo[0] == 2:
                Tprof = np.array([int(self.ui.lineEdit_s30.text())])
                Tdur = np.array([])
                
            if Ttipo[0] > 2:
                Tdur = np.array([int(self.ui.lineEdit_s29.text())])
                Tprof = np.array([int(self.ui.lineEdit_s30.text())])
            
            if Ttipo[0] != 0:
                generaDip=funciones_DIP.DIPgenerator(T,Ttipo,D,A,Aprom,self.t,self.fm, Tdur, Tprof,self.hrmean)
                dips = generaDip[0]
                dips=funciones_DIP.analisiswav(dips,'db4')
                self.HRV = self.HRV + dips
            return 0
        except:
            ctypes.windll.user32.MessageBoxA(0, 'Fin de simulacion! Contraccion no realizada', "Alert", 1)
    
    '''**************************************************************************************************************************************'''
    

    
    '''Funcion que obtiene los datos de las contracciones ingresadas por el usuario en la pestaña "contracciones" 
    intante, tipo de DIP que generan y la profundidad de cada DIP ***************************************************************************'''
    
    def getLineEdit(self):
        inputCon = self.mostrados
        instante=np.array([])
        tipo = np.array([])
        duracion = np.array([])
        prof = np.array([])
        line1 = ""
        line2 = ""
        line3 = ""
        for i in range (1,inputCon+1):
            #Obtiene los instantes de las contracciones
            exec("line1 = self.ui.lineEdit_s"+str(i+4)+".text()")
            if line1 == "":
                return 'Falta ingresar un instante en el menu contracciones'
            else:
                try:
                    line1 = int(line1)*60
                    instante = np.append(instante, line1)
                except:
                    return 'Ingrese un numero valido para la contraccion'
                    break
            #exec("T = np.append(T,int(self.ui.lineEdit_"+str(i)+".text()))")
            exec("tipo = np.append(tipo,self.ui.comboBox_s"+str(i)+".currentIndex())")
            
            if(tipo[i-1] == 1 or tipo[i-1] == 0):
                duracion = np.append(duracion, 0)
                prof = np.append(prof, 0)
            #Obtiene la duración de las Dip que generan las contracciones
            
            if ( tipo[i-1] == 2 ):
                duracion = np.append(duracion, 0)
                #Obtiene la Profundidad de las Dip que generan las contracciones
                exec("line3 = self.ui.lineEdit_s"+str(i+20)+".text()")
                if line3 == "":
                    return 'Falta ingresar la profundidad en el menu Duracion'
                else:
                    try:
                        line3 = int(line3)
                        prof = np.append(prof, line3)
                    except:
                        return 'Ingrese un numero valido para la profundidad del tipo de dip'
                        break
                
            elif(tipo[i-1] > 2):
                exec("line2 = self.ui.lineEdit_s"+str(i+12)+".text()")
                if line2 == "":
                    return 'Falta ingresar la duracion en el menu contraccion'
                else:
                    try:
                        line2 = int(line2)
                        duracion = np.append(duracion, line2)
                    except:
                        return 'Ingrese un numero valido para la Duracion del tipo de dip'
                        break
                    
                #Obtiene la Profundidad de las Dip que generan las contracciones
                exec("line3 = self.ui.lineEdit_s"+str(i+20)+".text()")
                if line3 == "":
                    return 'Falta ingresar la profundidad en el menu Duracion'
                else:
                    try:
                        line3 = int(line3)
                        prof = np.append(prof, line3)
                    except:
                        return 'Ingrese un numero valido para la profundidad del tipo de dip'
                        break
        
        return np.array([instante, tipo, duracion, prof])
    
    '''Funcion que llama a las funciones que grafican las señales dinamicamente o estaticamente *********************************************'''
    def StaticDinamic(self):
        
        if(self.ui.checkBox_s1.isChecked()):
            self.StaticPlot()
            self.ui.checkBox_s2.setEnabled(True)
            self.ui.pushButton_s2.setEnabled(False)
            
        else:
            self.DinamicPlot()
            self.ui.comboBox_s9.setEnabled(True)
            self.ui.pushButton_s2.setEnabled(True)
            self.ui.checkBox_s2.setEnabled(True)

    '''Funcion que inicializa las variables principales que deben ser ocupadas nuevamente ***************************************************'''       
    def inicializar(self):
        self.w1.setXRange(0, 1200, padding=0)
        self.w1.setYRange(30, 240, padding=0)
        self.w2.setXRange(0, 1200, padding=0)
        self.w2.setYRange(0, 100, padding=0)
        self.t = np.array([])
        self.HRV = np.array([])
        self.ttot = np.array([])
        self.piu = np.array([])
        self.w1.clear()
        self.w2.clear()
        self.ui.comboBox_s9.setCurrentIndex(0)
        self.ui.lcdNumber.display(str(0))
        
    '''Funcion que cambia el valor del label (lo que se muestra en la interfaz) de las profundidad de las desaceleraciones **********************'''
    def getModo(self, mod):
        if (mod == 1):
            return 'Leve'
        elif (mod == 2):
            return 'Moderada'
        else:
            return 'Severa'
    
    '''Funcion para que la progressBar vaya incrementando*****************************************'''  
    def barraProgreso(self):  
        def progress():
            tsim =int(self.ui.lineEdit_s1.text())*60
            x = (2.45626)*np.exp(0.000705*tsim)
            x = x/100
            self.tprogress = 0
            self.ui.progressBar.show()
            #time_ao = time.time()
            #def tiempoTimer():
            while(self.tprogress < 102):
                if(self.tprogress < 101):
                    self.ui.progressBar.setProperty("value", self.tprogress)
                    self.tprogress = self.tprogress + 1
                    time.sleep(x)
                else:
                    self.tprogress = self.tprogress + 1
                    self.ui.progressBar.hide()
                    #break
                    #self.timerProgress.deleteLater()
                        
            
            
        '''self.timerProgress = QtCore.QTimer()
        self.timerProgress.timeout.connect(tiempoTimer)
        self.timerProgress.start(x*100)'''
        
        d = threading.Thread(target=progress, name='Daemon')

        d.setDaemon(True)

        d.start()
        
        return d.isAlive()
    
    
    '''Funcion que cambia el modo(leve, moderada, severa) de las profundidades de las DIPs *************************************'''
    '''def cambiarModo(self):
        self.ui.label_5.setText(self.getModo(self.ui.horizontalSlider_1.value()))
        self.ui.label_6.setText(self.getModo(self.ui.horizontalSlider_2.value()))
        self.ui.label_7.setText(self.getModo(self.ui.horizontalSlider_3.value()))
        self.ui.label_8.setText(self.getModo(self.ui.horizontalSlider_4.value()))
        self.ui.label_9.setText(self.getModo(self.ui.horizontalSlider_5.value()))
        self.ui.label_10.setText(self.getModo(self.ui.horizontalSlider_6.value()))
        self.ui.label_11.setText(self.getModo(self.ui.horizontalSlider_7.value()))
        self.ui.label_12.setText(self.getModo(self.ui.horizontalSlider_8.value()))
        self.ui.label_14.setText(self.getModo(self.ui.horizontalSlider_uni.value()))'''
        
    '''Funcion que obtiene los valores de los campos de la pestaña "Frecuencia Cardiaca" '''
    def getParametros(self):
        
        def rampa2(x, x0):
            if x <= x0:
                y = 0
            else:
                y= x - x0
            return y
        
        param = np.array([]) #array que retorna la funcion
        tsim1 =self.ui.lineEdit_s1.text() # obtiene lo que contiene el campo
        NMF = self.ui.lineEdit_s2.text()
        self.hrmean = self.ui.lineEdit_s3.text()
        hrstd = self.ui.lineEdit_s4.text()
        #verifica que no sea vacío
        if tsim1 == "": 
            return "Ingrese tiempo de registro"
        else:
            try:
                #verifica que sea un número
                tsim1 = int(tsim1)*60
                
                param = np.append(param, tsim1)
            except:
                return "Ingrese un numero valido para Tiempo de registro"
            
        
        if(NMF == ""):
            return "Ingrese numero de Mov. Fetales"
        else:
            try:
                NMF = int(NMF)
                param = np.append(param, NMF)
            except:
                return "Ingrese un numero valido para Mov.Fetales"
        
        if (self.hrmean == ""):
            return "Ingrese linea Basal"
        else:
            try:
                self.hrmean = int(self.hrmean)
                param = np.append(param, self.hrmean)
            except:
                return "Ingrese un numero valido para Basal"
            
            
        if (hrstd == ""):
            return "Ingrese variabilidad"
        else:
            try:
                hrstd = (1 + 0.05*(1.1*rampa2(float(hrstd), 18) + 0.5*rampa2(float(hrstd), 30)))*0.8*(float(hrstd))**0.5
                
                if (hrstd >= 0 and hrstd < 51):
                    print hrstd, "hrstd"
                    param = np.append(param, hrstd)
            except:
                return "Ingrese un numero valido para variabilidad entre 1 y 50"
        
        return param #retorna todos los parametros
        
    '''Funcion IMPORTANTE, hace los calculos de la simulacion *************************************************'''    
        
    def calcular(self,fs,tsim,NMF,hrstd,hrmean,T,Ttipo, Tdur, Tprof):
        
        # Parametros internos a simulacion (reemplazan salidad de bloques no implementados)
        #print tsim
        Lt=len(np.arange(tsim[0],tsim[1] + 1,1/fs))
        CUif = np.zeros(Lt) # % no ocurren contracciones importantes que eviten un mf
        sigmahrv = 2.6*np.ones(Lt) #% seï¿½al de variabilidad de hrv con variabilidad de 2.6
        
        fs=250 #frecuencia de muestreo
        tstart=tsim[0] #tiempo de partida de simulacion (en segundos) 
        tend=tsim[1] #tiempo de termino de simulacion (en segundos) 
        
        #PARAMETROS GENERADOR DE CONTRACCION UTERINA
        
        self.u=np.array([10, 100])
        self.desv=np.array([1., 3., 3.])
        self.ad=0.5
        rstd=2
        bandpass=np.array([0, 0.1])
        self.fm=fs
        self.mfstd=np.array([10., 10., 5., 10.])
        
        tsim=np.array([tstart, tend])
        
        N=self.hrmean*tend/60
        N=round(N+0.05*N)
        
        #se calculan los parametros de los movimientos fetales
        mov =funciones_FHR.MF(tsim[1], CUif, sigmahrv, NMF, fs)
        #mov = [Imf, Dmf, Tmf] 
        Tmf = mov[0] #array de instantes en que comenzarán los mov. fetales
        Dmf = mov[1] #array de duraciones de los mov. fetales
        Imf = mov[2] #array de intensidades de los mov. fetales
        
        #se crea el vector de la basal de la frec. cardiaca del feto
        senal = funciones_FHR.HRV(fs,tsim,self.hrmean,hrstd)
        #[t,sigmaHRV,HRV0,self.hrmean]
        t = senal[0] #vector tiempo
        sigmaHRV = senal[1]
        HRV0 = senal[2] #vector con los valores del pulso cardiaco por cada elemento de t
        self.hrmeani = senal[3]
        
        
        #se genera el vector campanas de cada mov. fetal
        spf = funciones_FHR.campanas(tend-tstart,Tmf,Dmf,Imf,self.fm)
        spf=np.concatenate([spf,np.zeros(len(HRV0)-len(spf))])
        
        #Se generan las contracciones uterinas de la madre ingresadas por el usuario (al menos 1)
        # T --> vector de instantes donde comienza cada contraccion
        con=funciones_CU.contraccion(T,tsim,self.u,self.desv,self.ad,rstd,self.fm,bandpass,Tmf,self.mfstd)
        
        #[piu,ttot,D,A,Aprom]
        piu = con[0] #vector de presion intraUterina
        piu = piu.real #transforma la data desde complejos a reales para poder graficarse
        ttot = con[1] #vector del tiempo total de simulacion
        D = con[2] #vector con las duraciones de cada contraccion
        A = con[3] #vector con las amplitududes de cada contraccion 
        Aprom = con[4]
        
        
        #Se generan las desaceleraciones pasandole los instantes, el tipo, la duracion, amplitud, y la profundidad
        generaDip=funciones_DIP.DIPgenerator(T,Ttipo,D,A,Aprom,t,fs,Tdur,Tprof,self.hrmean)
        
        #print generaDip[1]
        #[dips,h]
        dips = generaDip[0]
        h = generaDip[1]
        
        #el vector dips se modifica aplicandole la funcion wavelets
        dips=funciones_DIP.analisiswav(dips,'db4')
        h=h*(hrstd-1.)+1.
        HRV0mean=np.mean(HRV0)
        HRV0=((HRV0-HRV0mean)/h)+HRV0mean
        
        #generacion de hrv con inclusion de movimientos fetales y las desaceleraciones(dips)
        
        HRV = spf + HRV0 + dips
        
        #HRV = spf + HRV0 + dips
        #generacion de hrv final y linea de tiempo en segundos
        
        
        a=np.where(t==tend)[0]
        HRV=HRV[0:(a[0])]
        t=t[0:(a[0])]
        
        return np.array([t,HRV,ttot,piu]) #Retorno del tiempo y el HRV para la grafica 1 y tiempo y PresionIntraUterina para la grafica 2
    
    '''Grafica la funcion Dinamicamente **********************************************************************'''
    
    def DinamicPlot(self):
        
        self.inicializar() #Se inicial los parametros principales
        
                
        print("Comienzo de Simulacion")
        
        param = self.getParametros() #Obtiene los parametros para el HRV
        valCon = self.getLineEdit() #Obtiene los parametros para las contracciones
        
        print param
        
        if not isinstance(param, basestring):
            if not isinstance(valCon, basestring):
                
                pro =self.barraProgreso()
                
                fs = 250
                tsim = np.array([0, int(param[0])]) 
                NMF = param[1]
                self.hrmean = param[2]
                hrstd = param[3]
                
                self.tsimforcm = tsim[1]
                
                T=valCon[0]
                Ttipo = valCon[1]
                Tdur = valCon[2]
                Tprof = valCon[3]
                
                print T, 'instantes'
                print Ttipo, 'tipos'
                print Tdur, 'dif'
                print Tprof, 'dif'
                
                signals = self.calcular(fs,tsim,NMF,hrstd,self.hrmean,T,Ttipo, Tdur, Tprof)
                
                while (True):
                    if (self.ui.progressBar.value() == 100):
                        break
                    
                self.t = signals[0]
                self.HRV = signals[1]
                self.ttot = signals[2]
                self.piu = signals[3]
                
                #print len(self.t), len(self.HRV), len(self.ttot), len(self.piu)
                #print self.t[-1], self.HRV[-1], self.ttot[-1], self.piu[-1]
                
                if self.generated > 0:
                    if self.contHRV < len(self.t):
                        self.timer.stop()
                        self.timer.deleteLater()
                        self.generated = self.generated + 1
                        self.timer = QtCore.QTimer()
                else:
                    self.timer = QtCore.QTimer()
                    self.generated = self.generated + 1
                    
                print self.generated
                
                '''Función que genera los graficos junto con sus ejes y la grilla'''
                
                ticks1 = []
                ticks2 = []
                
                for i in range(0, tsim[1]+1,30):
                    tupla = (i,'')
                    ticks2.append(tupla)
                
                for i in range(0, tsim[1]+1,180):
                    tupla = (i,'')
                    ticks1.append(tupla)
                
                self.curveHRV = self.w1.plot(pen=pg.mkColor(0,0,0))
                self.w1.getAxis('bottom').setTicks([ticks1,ticks2])
                 
                '''Funcion que grafica dinamicamente, actualiza los puntos del HRV y se especifica cual es el paso temporal en numero de muestras'''
                
                self.contHRV=0
                self.x1 = np.array([])
                self.y1 = np.array([])
                
                #Funcion que actualiza la grafica de la frecuencia cardiaca
                def updateHRV():
                    if (self.Timpulso > 0):
                        self.ui.pushButton_s2.setEnabled(False)
                        self.Timpulso = self.Timpulso - 1
                    else:
                        self.ui.pushButton_s2.setEnabled(True)
                    
                    if self.contHRV > len(self.t):
                        print 'stop'
                        self.timer.stop()
                    elif self.contHRV == len(self.t):
                        self.x1 = np.append(self.x1, self.t[self.contHRV-1])
                        self.y1 = np.append(self.y1, self.HRV[self.contHRV-1])
                        self.curveHRV.setData(self.x1, self.y1)
                        self.contHRV = self.contHRV + 250
                    else:
                        self.x1 = np.append(self.x1, self.t[self.contHRV])
                        self.y1 = np.append(self.y1, self.HRV[self.contHRV])
                        self.curveHRV.setData(self.x1, self.y1)
                        self.contHRV = self.contHRV + 250
                    
                
                self.curveCON = self.w2.plot(pen=pg.mkColor(0,0,0))
                self.w2.getAxis('bottom').setTicks([ticks1,ticks2])
                 
                self.contCON=0
                self.x2 = np.array([])
                self.y2 = np.array([])
                self.digito = 1
                
                #Funcion que actualiza la grafica de la presionIntrauterina
                def updateCON():
                    if (self.Tscu > 0):
                        self.ui.pushButton_s2.setEnabled(False)
                        self.Tscu = self.Tscu - 1
                    else:
                        self.ui.pushButton_s2.setEnabled(True)
                    #print self.digito
                    self.ui.lcdNumber.display(str(self.digito))
                    self.digito = self.digito + 1
                    if self.contCON > len(self.t):
                        print 'stop'
                        self.timer.stop()
                    elif self.contCON == len(self.t):
                        self.x2 = np.append(self.x2, self.ttot[self.contCON-1])
                        self.y2 = np.append(self.y2, self.piu[self.contCON-1])
                        self.curveCON.setData(self.x2, self.y2)
                        self.contCON = self.contCON + 250
                    else:
                        self.x2 = np.append(self.x2, self.ttot[self.contCON])
                        self.y2 = np.append(self.y2, self.piu[self.contCON])
                        self.curveCON.setData(self.x2, self.y2)
                        self.contCON = self.contCON + 250
                
                self.timer.timeout.connect(updateHRV)
                self.timer.timeout.connect(updateCON)
                self.timer.start(1000)
        
                
                
                
                '''Función que hace mover los dos gráficos al mismo tiempo----------------------------------------------------------------------'''
                self.vb1 = self.w1.vb
                self.vb2 = self.w2.vb
                
                def mouseMoved(pos):
                    if self.w1.sceneBoundingRect().contains(pos):
                        mousePoint = self.vb1.mapSceneToView(pos)
                        index = int(mousePoint.x())
                        if index > 0 and index < tsim[1]:
                            rangos = (self.vb1.viewRange())
                            minX = (rangos[0])[0]
                            maxX = (rangos[0])[1]
                            if (int(minX) < 0):
                                self.w1.setMouseEnabled(x = False)
                                if self.ui.checkBox_s2.isChecked():
                                    self.w1.setXRange(0, 240, padding=0)
                                    self.w2.setXRange(0, 240, padding=0)
                                else:
                                    self.w1.setXRange(0, 1200, padding=0)
                            elif (int(maxX) > tsim[1]):
                                self.w1.setMouseEnabled(x = False)
                                if self.ui.checkBox_s4.isChecked():
                                    self.w1.setXRange(tsim[1] - 240, tsim[1], padding=0)
                                else:
                                    self.w1.setXRange(tsim[1] - 1200, tsim[1], padding=0)
                            else:
                                self.w1.setMouseEnabled(x = True)
                                self.w2.setXRange(minX, maxX, padding=0)
                                
                    if self.w2.sceneBoundingRect().contains(pos):
                        mousePoint = self.vb2.mapSceneToView(pos)
                        index = int(mousePoint.x())
                        if index > 0 and index < tsim[1]:
                            self.w2.setMouseEnabled(x = True)
                            rangos = (self.vb2.viewRange())
                            minX = (rangos[0])[0]
                            maxX = (rangos[0])[1]
                            if (int(minX) < 0):
                                self.w2.setMouseEnabled(x = False)
                                if self.ui.checkBox_s2.isChecked():
                                    self.w1.setXRange(0, 240, padding=0)
                                    self.w2.setXRange(0, 240, padding=0)
                                else:
                                    self.w1.setXRange(0, 1200, padding=0)
                            elif (int(maxX) > tsim[1]):
                                self.w2.setMouseEnabled(x = False)
                                if self.ui.checkBox_s2.isChecked():
                                    self.w1.setXRange(tsim[1] - 240, tsim[1], padding=0)
                                else:
                                    self.w1.setXRange(tsim[1] - 1200, tsim[1], padding=0)
                            else:
                                self.w2.setMouseEnabled(x = True)
                                self.w1.setXRange(minX, maxX, padding=0)
        
                self.ui.graphicsView.scene().sigMouseMoved.connect(mouseMoved)
            else:
                ctypes.windll.user32.MessageBoxA(0, valCon, "Alert", 1)
        else:
            ctypes.windll.user32.MessageBoxA(0, param, "Alert", 1)
        
    '''Función para graficar estaticamente ************************************************************************'''
        
    def StaticPlot(self):
        
        self.inicializar()
        
        print("Simulacion")
        
        param = self.getParametros()
        valCon = self.getLineEdit()
        
        if not isinstance(param, basestring):
            if not isinstance(valCon, basestring):
                
                pro =self.barraProgreso()
                
                fs = 250
                tsim = np.array([0, int(param[0])]) 
                NMF = param[1]
                self.hrmean = param[2]
                hrstd = param[3]
                
                self.tsimforcm = tsim[1]
                
                #valCon = self.getLineEdit()
                T=valCon[0]
                Ttipo = valCon[1]
                Tdur = valCon[2]
                Tprof = valCon[3]
                
                print T, 'instantes'
                print Ttipo, 'tipos'
                print Tdur, 'dif'
                print Tprof, 'dif'
        
                
                signals = self.calcular(fs,tsim,NMF,hrstd,self.hrmean,T,Ttipo,Tdur, Tprof)
                
                while (True):
                    if (self.ui.progressBar.value() == 100):
                        break
                
                    
                self.t = signals[0]
                self.HRV = signals[1]
                self.ttot = signals[2]
                self.piu = signals[3]
                
                if self.generated > 0:
                    self.timer.stop()
                    self.timer.deleteLater()
                    self.generated = 0
                
                '''Función que genera los graficos junto con sus ejes y la grilla'''
                
                
                ticks1 = []
                ticks2 = []
                #subticks = []
                
                #subtickscu = []
                
                for i in range(0, tsim[1]+1,30):
                    tupla = (i,'')
                    ticks2.append(tupla)
                
                for i in range(0, tsim[1]+1,180):
                    tupla = (i,'')
                    ticks1.append(tupla)
                
                self.w1.plot(self.t,self.HRV, pen=pg.mkColor(0,0,0))
                self.w1.getAxis('bottom').setTicks([ticks1,ticks2])
                self.w2.plot(self.ttot,self.piu, pen=pg.mkColor(0,0,0))
                self.w2.getAxis('bottom').setTicks([ticks1,ticks2])
                '''Función que hace mover los dos gráficos al mismo tiempo----------------------------------------------------------------------'''
                
                self.vb1 = self.w1.vb
                self.vb2 = self.w2.vb
                
                def mouseMoved(pos):
                    if self.w1.sceneBoundingRect().contains(pos):
                        mousePoint = self.vb1.mapSceneToView(pos)
                        index = int(mousePoint.x())
                        if index > 0 and index < tsim[1]:
                            rangos = (self.vb1.viewRange())
                            minX = (rangos[0])[0]
                            maxX = (rangos[0])[1]
                            if (int(minX) < 0):
                                self.w1.setMouseEnabled(x = False)
                                if self.ui.checkBox_s2.isChecked():
                                    self.w1.setXRange(0, 240, padding=0)
                                    self.w2.setXRange(0, 240, padding=0)
                                else:
                                    self.w1.setXRange(0, 1200, padding=0)
                            elif (int(maxX) > tsim[1]):
                                self.w1.setMouseEnabled(x = False)
                                if self.ui.checkBox_s2.isChecked():
                                    self.w1.setXRange(tsim[1] - 240, tsim[1], padding=0)
                                else:
                                    self.w1.setXRange(tsim[1] - 1200, tsim[1], padding=0)
                            else:
                                self.w1.setMouseEnabled(x = True)
                                self.w2.setXRange(minX, maxX, padding=0)
                                
                    if self.w2.sceneBoundingRect().contains(pos):
                        mousePoint = self.vb2.mapSceneToView(pos)
                        index = int(mousePoint.x())
                        if index > 0 and index < tsim[1]:
                            self.w2.setMouseEnabled(x = True)
                            rangos = (self.vb2.viewRange())
                            minX = (rangos[0])[0]
                            maxX = (rangos[0])[1]
                            if (int(minX) < 0):
                                self.w2.setMouseEnabled(x = False)
                                if self.ui.checkBox_s2.isChecked():
                                    self.w1.setXRange(0, 240, padding=0)
                                    self.w2.setXRange(0, 240, padding=0)
                                else:
                                    self.w1.setXRange(0, 1200, padding=0)
                            elif (int(maxX) > tsim[1]):
                                self.w2.setMouseEnabled(x = False)
                                if self.ui.checkBox_s2.isChecked():
                                    self.w1.setXRange(tsim[1] - 240, tsim[1], padding=0)
                                else:
                                    self.w1.setXRange(tsim[1] - 1200, tsim[1], padding=0)
                            else:
                                self.w2.setMouseEnabled(x = True)
                                self.w1.setXRange(minX, maxX, padding=0)
        
                self.ui.graphicsView.scene().sigMouseMoved.connect(mouseMoved)
                    
            else:
                ctypes.windll.user32.MessageBoxA(0, valCon, "Alert", 1)
        else:
            ctypes.windll.user32.MessageBoxA(0, param, "Alert", 1)
        
    '''**************************************************************************************************************************************'''
    
 
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = GUIForm()
    myapp.show()
    sys.exit(app.exec_())
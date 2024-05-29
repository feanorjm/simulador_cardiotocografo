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
from PlotGuiFinal3 import *
import numpy as np
import scipy as sc
import numpy.fft
import ctypes
import time
import sip

import pyqtgraph as pg

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



 
class GUIForm(QtGui.QDialog):
    
    '''Metodo principal********************************************************************************************************'''

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        sip.setdestroyonexit(False)
        self.setWindowFlags( Qt.CustomizeWindowHint | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint )
        
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'), self.StaticDinamic)
        #QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT("quit()"))
        QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL('clicked()'), self.impulso)
        QtCore.QObject.connect(self.ui.horizontalSlider, QtCore.SIGNAL('valueChanged(int)'), self.agregar)
        '''horizontals'''
        QtCore.QObject.connect(self.ui.horizontalSlider_1, QtCore.SIGNAL('valueChanged(int)'), self.cambiarModo)
        QtCore.QObject.connect(self.ui.horizontalSlider_2, QtCore.SIGNAL('valueChanged(int)'), self.cambiarModo)
        QtCore.QObject.connect(self.ui.horizontalSlider_3, QtCore.SIGNAL('valueChanged(int)'), self.cambiarModo)
        QtCore.QObject.connect(self.ui.horizontalSlider_4, QtCore.SIGNAL('valueChanged(int)'), self.cambiarModo)
        QtCore.QObject.connect(self.ui.horizontalSlider_5, QtCore.SIGNAL('valueChanged(int)'), self.cambiarModo)
        QtCore.QObject.connect(self.ui.horizontalSlider_6, QtCore.SIGNAL('valueChanged(int)'), self.cambiarModo)
        QtCore.QObject.connect(self.ui.horizontalSlider_7, QtCore.SIGNAL('valueChanged(int)'), self.cambiarModo)
        QtCore.QObject.connect(self.ui.horizontalSlider_8, QtCore.SIGNAL('valueChanged(int)'), self.cambiarModo)
        QtCore.QObject.connect(self.ui.horizontalSlider_uni, QtCore.SIGNAL('valueChanged(int)'), self.cambiarModo)
        '''fin horizontals'''
        
        QtCore.QObject.connect(self.ui.comboBox_2, QtCore.SIGNAL('activated(QString)'), self.apareceBarra)
        QtCore.QObject.connect(self.ui.comboBox_3, QtCore.SIGNAL('activated(QString)'), self.apareceBarra)
        QtCore.QObject.connect(self.ui.comboBox_4, QtCore.SIGNAL('activated(QString)'), self.apareceBarra)
        QtCore.QObject.connect(self.ui.comboBox_5, QtCore.SIGNAL('activated(QString)'), self.apareceBarra)
        QtCore.QObject.connect(self.ui.comboBox_6, QtCore.SIGNAL('activated(QString)'), self.apareceBarra)
        QtCore.QObject.connect(self.ui.comboBox_7, QtCore.SIGNAL('activated(QString)'), self.apareceBarra)
        QtCore.QObject.connect(self.ui.comboBox_8, QtCore.SIGNAL('activated(QString)'), self.apareceBarra)
        QtCore.QObject.connect(self.ui.comboBox_9, QtCore.SIGNAL('activated(QString)'), self.apareceBarra)
        
        QtCore.QObject.connect(self.ui.comboBox, QtCore.SIGNAL('activated(QString)'), self.combo_chosen)
        QtCore.QObject.connect(self.ui.comboBox_hrstd, QtCore.SIGNAL('activated(QString)'), self.combo_hrstd)
        QtCore.QObject.connect(self.ui.lineEdit_hrstd, QtCore.SIGNAL(("textChanged(QString)")), self.combo_hrstd)
        
        QtCore.QObject.connect(self.ui.checkBox_2, QtCore.SIGNAL('clicked()'), self.pulsaCheckMF)
        QtCore.QObject.connect(self.ui.checkBox_3, QtCore.SIGNAL('clicked()'), self.pulsaCheckCU)
        QtCore.QObject.connect(self.ui.checkBox_4, QtCore.SIGNAL('clicked()'), self.cambiaCmMin)
        QtCore.QObject.connect(self.ui.checkBox, QtCore.SIGNAL('clicked()'), self.pulsaCheckDinamic)
        QtCore.QObject.connect(self.ui.radioButton_3, QtCore.SIGNAL("toggled(bool)"), self.call_Consult)
        QtCore.QObject.connect(self.ui.radioButton_6, QtCore.SIGNAL("toggled(bool)"), self.call_Consult)
        
        ticks1 = []
        ticks2 = []
        subticks = []
        subtickscu = []
        
        for i in range(0, 720+1,30):
            tupla = (i,'')
            ticks2.append(tupla)
        
        for i in range(0, 720+1,180):
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
        self.w1.setXRange(0, 720, padding=0)
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
        self.w2.setXRange(0, 720, padding=0)
        self.w2.setYRange(0, 100, padding=0)
        self.w2.showGrid(x=True, y=True)
        self.w2.getAxis('left').setPen('r')
        self.w2.getAxis('bottom').setPen('r')
        self.w2.setMouseEnabled(y = False)
        
        self.w2.getAxis('bottom').setTicks([ticks1,ticks2])
        #self.w2.getAxis('left').setTicks([[(0,'0'),(25,'25'),(50,'50'),(75,'75'),(100,'100')],[(10,''),(20,''),(40,''),(50,''),(70,''),(10,'')],subtickscu])
        self.w2.getAxis('left').setTicks([[(0,'0'),(25,'25'),(50,'50'),(75,'75'),(100,'100')],subtickscu])
        self.w2.getAxis('left').setWidth(30)
        for i in range(2,10):
            exec("self.ui.comboBox_"+str(i)+".addItems(['Ninguna','Temprana', 'Tardia', 'Variable', 'Prolongada'])")
        
        for i in range(2,9):
            exec("self.ui.label_num_"+str(i)+".hide()")
            exec("self.ui.comboBox_"+str(i+1)+".hide()")
            exec("self.ui.lineEdit_"+str(i)+".hide()")
            exec("self.ui.horizontalSlider_"+str(i)+".hide()")
            exec("self.ui.label_"+str(i+4)+".hide()")
        
        
        self.ui.comboBox.addItems(["1x","2x","4x","8x",'16x'])
        self.ui.comboBox_hrstd.addItems(['Indetectable','Disminuida','Moderada','Marcada'])
        self.ui.progressBar.setProperty("value", 0)
        self.ui.progressBar.hide()
        self.mostrados = 1
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_4.hide()
        
        self.Timpulso = 0
        self.Tscu = 0
        self.tiempo = 0
        self.veloc = self.asignar(self.ui.comboBox.currentIndex())
        self.hrstd = 0
        self.generated = 0
        self.contHRV=0
        self.ui.checkBox_4.setEnabled(False)
        self.tsimforcm = 0
        self.hrmean = 0
        
    
    '''**************************************************************************************************************************************'''
    
    
    '''Funcion que escucha cuando cambia el combobox de la velocidad ************************************************************************'''
    def combo_chosen(self):
        a = self.ui.comboBox.currentIndex()
        self.veloc = self.asignar(a)
        self.timer.start(self.veloc)
        
    '''Función para cambiar la grilla de 1cm/min a 3cm/min y viceversa'''
    def cambiaCmMin(self):
        if self.ui.checkBox_4.isChecked():
            self.ui.label_15.setText('3 cm/min')
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
            self.ui.label_15.setText('1 cm/min')
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
            self.w1.setXRange(0, 720, padding=0)
            self.w2.setXRange(0, 720, padding=0)
        
    
    '''Funcion que escucha cuando cambia el combobox de la amplitud de la variabilidad ******************************************************'''
    def combo_hrstd(self):
        self.hrstd  = self.ui.lineEdit_hrstd.text()
        if self.hrstd == "": 
            return "Ingrese tiempo de registro"
        else:
            try:
                #verifica que sea un número
                self.hrstd = float(self.hrstd)
                if (self.hrstd > 0 and self.hrstd < 3):
                    print "Indetectable"
                elif (self.hrstd > 2 and self.hrstd < 5):
                    print "Disminuida"
                elif (self.hrstd > 4 and self.hrstd < 26):
                    print "Moderada"
                elif(self.hrstd > 25 and self.hrstd < 51):
                    print "Marcada"
            except:
                return "Ingrese un numero valido para Tiempo de registro"
        
        #self.hrstd = self.ui.comboBox_hrstd.currentIndex()
        
    '''Funcion que hace aparecer las horizontalSliders de las desaceleraciones *****************************************************************'''        
    def apareceBarra(self):
        if self.ui.comboBox_2.currentIndex() > 1:
            self.ui.horizontalSlider_1.show()
            self.ui.label_5.show()
            self.ui.label_3.show() #muestra label y cambia el otro
            self.ui.label_prof.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Profundidad</span></p></body></html>", None))
        else:
            self.ui.horizontalSlider_1.hide()
            self.ui.label_5.hide()
            self.ui.label_3.hide() #esconde label y cambia el otro
            self.ui.label_prof.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Desaceleración</span></p></body></html>", None))
        if self.ui.comboBox_3.currentIndex() > 1:
            self.ui.horizontalSlider_2.show()
            self.ui.label_6.show()
        else:
            self.ui.horizontalSlider_2.hide()
            self.ui.label_6.hide()
        if self.ui.comboBox_4.currentIndex() > 1:
            self.ui.horizontalSlider_3.show()
            self.ui.label_7.show()
        else:
            self.ui.horizontalSlider_3.hide()
            self.ui.label_7.hide()
        if self.ui.comboBox_5.currentIndex() > 1:
            self.ui.horizontalSlider_4.show()
            self.ui.label_8.show()
        else:
            self.ui.horizontalSlider_4.hide()
            self.ui.label_8.hide()
        if self.ui.comboBox_6.currentIndex() > 1:
            self.ui.horizontalSlider_5.show()
            self.ui.label_9.show()
        else:
            self.ui.horizontalSlider_5.hide()
            self.ui.label_9.hide()
        if self.ui.comboBox_7.currentIndex() > 1:
            self.ui.horizontalSlider_6.show()
            self.ui.label_10.show()
        else:
            self.ui.horizontalSlider_6.hide()
            self.ui.label_10.hide()
        if self.ui.comboBox_8.currentIndex() > 1:
            self.ui.horizontalSlider_7.show()
            self.ui.label_11.show()
        else:
            self.ui.horizontalSlider_7.hide()
            self.ui.label_11.hide()
        if self.ui.comboBox_9.currentIndex() > 1:
            self.ui.horizontalSlider_8.show()
            self.ui.label_12.show()
        else:
            self.ui.horizontalSlider_8.hide()
            self.ui.label_12.hide()
        
        
    '''Funciones asociados a los checkBoxs y radioButtons para que aparezcan o desaparezacan segun la simulacion que se lance ***************'''        
    def pulsaCheckDinamic(self):
        if self.ui.checkBox.isChecked() == False:
            self.ui.checkBox_2.setEnabled(True)
            self.ui.checkBox_3.setEnabled(True)
            if self.ui.checkBox_3.isChecked():
                self.ui.radioButton_2.setEnabled(True)
                self.ui.radioButton_3.setEnabled(True)
                self.ui.radioButton_4.setEnabled(True)
                self.ui.radioButton_5.setEnabled(True)
                self.ui.radioButton_6.setEnabled(True)
                if self.ui.radioButton_3.isChecked() == False:
                    self.ui.horizontalSlider_uni.setEnabled(True)
                    self.ui.label_14.setEnabled(True)
                    
        else:
            self.ui.checkBox_2.setEnabled(False)
            self.ui.checkBox_3.setEnabled(False)
            if self.ui.checkBox_3.isChecked():
                self.ui.radioButton_2.setEnabled(False)
                self.ui.radioButton_3.setEnabled(False)
                self.ui.radioButton_4.setEnabled(False)
                self.ui.radioButton_5.setEnabled(False)
                self.ui.radioButton_6.setEnabled(False)
                if self.ui.radioButton_3.isChecked() == False:
                    self.ui.horizontalSlider_uni.setEnabled(False)
                    self.ui.label_14.setEnabled(False)
                        
        
    def pulsaCheckMF(self):
        if (self.ui.checkBox_2.isChecked()):
            self.ui.checkBox_3.setChecked(False)
            self.ui.radioButton_2.hide()
            self.ui.radioButton_3.hide()
            self.ui.radioButton_4.hide()
            self.ui.radioButton_5.hide()
            self.ui.radioButton_6.hide()
            self.ui.horizontalSlider_uni.hide()
            self.ui.label_14.hide()
            self.ui.pushButton_4.show()
            
            
    def pulsaCheckCU(self):
        if (self.ui.checkBox_3.isChecked()):
            self.ui.checkBox_2.setChecked(False)
            self.ui.checkBox_2.setEnabled(True)
            self.ui.radioButton_2.show()
            self.ui.radioButton_3.show()
            self.ui.radioButton_4.show()
            self.ui.radioButton_5.show()
            self.ui.radioButton_6.show()
            self.ui.pushButton_4.show()
            self.ui.radioButton_6.setChecked(True)
    
    def call_Consult(self):
        if self.ui.radioButton_3.isChecked() | self.ui.radioButton_6.isChecked():
            self.ui.horizontalSlider_uni.hide()
            self.ui.label_14.hide()
        else:
            self.ui.horizontalSlider_uni.show()
            self.ui.label_14.show()
    
    '''Funcion que retorna el identificador de la desaceleracion en el radioButton'''    
    def getDip(self):
        if self.ui.radioButton_3.isChecked():
            return 1
        elif self.ui.radioButton_2.isChecked():
            return 2
        elif self.ui.radioButton_4.isChecked():
            return 3
        elif self.ui.radioButton_5.isChecked():
            return 4
        elif self.ui.radioButton_6.isChecked():
            return 0
        
    '''Funcion que escucha cuando cambia el horizontalSlider que agrega contracciones******************************************************'''
    def agregar(self):
        self.cant = self.ui.horizontalSlider.value()
        self.ui.label_4.setText(str(self.cant))
        if self.cant >= self.mostrados:
            for i in range(1,self.cant+1):
                exec("self.ui.label_num_"+str(i)+".show()")
                exec("self.ui.comboBox_"+str(i+1)+".show()")
                exec("self.ui.lineEdit_"+str(i)+".show()")
                #exec("self.ui.horizontalSlider_"+str(i)+".show()")
                #exec("self.ui.label_"+str(i+4)+".show()")
            
                
        else:
            for i in range(self.cant+1,self.mostrados+1):
                exec("self.ui.label_num_"+str(i)+".hide()")
                exec("self.ui.comboBox_"+str(i+1)+".hide()")
                exec("self.ui.lineEdit_"+str(i)+".hide()")
                exec("self.ui.horizontalSlider_"+str(i)+".hide()")
                exec("self.ui.label_"+str(i+4)+".hide()")
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
        if self.ui.checkBox_2.isChecked():
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
            Tprof = np.array([self.ui.horizontalSlider_uni.value()])
            
            if Ttipo[0] != 0:
                generaDip=funciones_DIP.DIPgenerator(T,Ttipo,D,A,Aprom,self.t,self.fm, Tprof,self.hrmean)
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
        T=np.array([])
        Ttipo = np.array([])
        Tprof = np.array([])
        line = ""
        for i in range (1,inputCon+1):
            exec("line = self.ui.lineEdit_"+str(i)+".text()")
            if line == "":
                return 'Falta ingresar un instante en el menu contracciones'
            else:
                try:
                    line = int(line)
                    T = np.append(T, line)
                except:
                    return 'Ingrese un numero valido para la contraacion'
                    break
            #exec("T = np.append(T,int(self.ui.lineEdit_"+str(i)+".text()))")
            exec("Ttipo = np.append(Ttipo,self.ui.comboBox_"+str(i+1)+".currentIndex())")
            exec("Tprof = np.append(Tprof,self.ui.horizontalSlider_"+str(i)+".value())")
        
        return np.array([T, Ttipo, Tprof])
    
    '''Funcion que llama a las funciones que grafican las señales dinamicamente o estaticamente *********************************************'''
    def StaticDinamic(self):
        
        if(self.ui.checkBox.isChecked()):
            self.StaticPlot()
            self.ui.checkBox_4.setEnabled(True)
            self.ui.pushButton_4.setEnabled(False)
            
        else:
            self.DinamicPlot()
            self.ui.comboBox.setEnabled(True)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.checkBox_4.setEnabled(True)

    '''Funcion que inicializa las variables principales que deben ser ocupadas nuevamente ***************************************************'''       
    def inicializar(self):
        self.w1.setXRange(0, 720, padding=0)
        self.w1.setYRange(30, 240, padding=0)
        self.w2.setXRange(0, 720, padding=0)
        self.w2.setYRange(0, 100, padding=0)
        self.t = np.array([])
        self.HRV = np.array([])
        self.ttot = np.array([])
        self.piu = np.array([])
        self.w1.clear()
        self.w2.clear()
        self.ui.comboBox.setCurrentIndex(0)
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
            tsim =int(self.ui.lineEdit_tsim.text())*60
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
    def cambiarModo(self):
        self.ui.label_5.setText(self.getModo(self.ui.horizontalSlider_1.value()))
        self.ui.label_6.setText(self.getModo(self.ui.horizontalSlider_2.value()))
        self.ui.label_7.setText(self.getModo(self.ui.horizontalSlider_3.value()))
        self.ui.label_8.setText(self.getModo(self.ui.horizontalSlider_4.value()))
        self.ui.label_9.setText(self.getModo(self.ui.horizontalSlider_5.value()))
        self.ui.label_10.setText(self.getModo(self.ui.horizontalSlider_6.value()))
        self.ui.label_11.setText(self.getModo(self.ui.horizontalSlider_7.value()))
        self.ui.label_12.setText(self.getModo(self.ui.horizontalSlider_8.value()))
        self.ui.label_14.setText(self.getModo(self.ui.horizontalSlider_uni.value()))
        
    '''Funcion que obtiene los valores de los campos de la pestaña "Frecuencia Cardiaca" '''
    def getParametros(self):
        param = np.array([]) #array que retorna la funcion
        tsim1 =self.ui.lineEdit_tsim.text() # obtiene lo que contiene el campo
        NMF = self.ui.lineEdit_nmf.text()
        self.hrmean = self.ui.lineEdit_hrm.text()
        
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
            
            
        if (self.hrstd == ""):
            return "Ingrese variabilidad"
        elif(self.hrstd > 0 and self.hrstd <=50):
            try:
                self.hrstd = (float(self.hrstd))**0.5
                print self.hrstd, "self.hrstd"
                param = np.append(param, self.hrstd)
            except:
                return "Ingrese un numero valido para variabilidad entre 1 y 50"
        elif(self.hrstd > 50):
            return "Ingrese un numero para variabilidad entre 1 y 50"
        
        #segun el indice del comboBox se modifica el hrstd que sirve para calcaular la variabilidad
        '''if self.hrstd == 0:
            hrstd = 1 + np.random.rand()*0.2
        elif self.hrstd == 1:
            hrstd = (np.random.rand()*4.7 + 0.5)**0.5
        elif self.hrstd == 2:
            hrstd = (np.random.rand()*20 + 5)**0.5
        else:
            hrstd = np.random.rand()*3 + 6.5
            
        param = np.append(param, hrstd)'''
        
        return param #retorna todos los parametros
        
    '''Funcion IMPORTANTE, hace los calculos de la simulacion *************************************************'''    
        
    def calcular(self,fs,tsim,NMF,hrstd,hrmean,T,Ttipo, Tprof):
        
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
        generaDip=funciones_DIP.DIPgenerator(T,Ttipo,D,A,Aprom,t,fs,Tprof,self.hrmean)
        
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
                Tprof = valCon[2]
                
                print T, 'instantes'
                print Ttipo, 'tipos'
                print Tprof, 'dif'
                
                signals = self.calcular(fs,tsim,NMF,hrstd,self.hrmean,T,Ttipo, Tprof)
                
                while (True):
                    if (self.ui.progressBar.value() == 100):
                        break
                    
                self.t = signals[0]
                self.HRV = signals[1]
                self.ttot = signals[2]
                self.piu = signals[3]
                
                print len(self.t), len(self.HRV), len(self.ttot), len(self.piu)
                print self.t[-1], self.HRV[-1], self.ttot[-1], self.piu[-1]
                
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
                        self.ui.pushButton_4.setEnabled(False)
                        self.Timpulso = self.Timpulso - 1
                    else:
                        self.ui.pushButton_4.setEnabled(True)
                    
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
                        self.ui.pushButton_4.setEnabled(False)
                        self.Tscu = self.Tscu - 1
                    else:
                        self.ui.pushButton_4.setEnabled(True)
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
                                if self.ui.checkBox_4.isChecked():
                                    self.w1.setXRange(0, 240, padding=0)
                                    self.w2.setXRange(0, 240, padding=0)
                                else:
                                    self.w1.setXRange(0, 720, padding=0)
                            elif (int(maxX) > tsim[1]):
                                self.w1.setMouseEnabled(x = False)
                                if self.ui.checkBox_4.isChecked():
                                    self.w1.setXRange(tsim[1] - 240, tsim[1], padding=0)
                                else:
                                    self.w1.setXRange(tsim[1] - 720, tsim[1], padding=0)
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
                                if self.ui.checkBox_4.isChecked():
                                    self.w1.setXRange(0, 240, padding=0)
                                    self.w2.setXRange(0, 240, padding=0)
                                else:
                                    self.w1.setXRange(0, 720, padding=0)
                            elif (int(maxX) > tsim[1]):
                                self.w2.setMouseEnabled(x = False)
                                if self.ui.checkBox_4.isChecked():
                                    self.w1.setXRange(tsim[1] - 240, tsim[1], padding=0)
                                else:
                                    self.w1.setXRange(tsim[1] - 720, tsim[1], padding=0)
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
                
                valCon = self.getLineEdit()
                T=valCon[0]
                Ttipo = valCon[1]
                Tprof = valCon[2]
                
                print T, 'instantes'
                print Ttipo, 'tipos'
                print Tprof, 'dif'
        
                
                signals = self.calcular(fs,tsim,NMF,hrstd,self.hrmean,T,Ttipo, Tprof)
                
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
                                if self.ui.checkBox_4.isChecked():
                                    self.w1.setXRange(0, 240, padding=0)
                                    self.w2.setXRange(0, 240, padding=0)
                                else:
                                    self.w1.setXRange(0, 720, padding=0)
                            elif (int(maxX) > tsim[1]):
                                self.w1.setMouseEnabled(x = False)
                                if self.ui.checkBox_4.isChecked():
                                    self.w1.setXRange(tsim[1] - 240, tsim[1], padding=0)
                                else:
                                    self.w1.setXRange(tsim[1] - 720, tsim[1], padding=0)
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
                                if self.ui.checkBox_4.isChecked():
                                    self.w1.setXRange(0, 240, padding=0)
                                    self.w2.setXRange(0, 240, padding=0)
                                else:
                                    self.w1.setXRange(0, 720, padding=0)
                            elif (int(maxX) > tsim[1]):
                                self.w2.setMouseEnabled(x = False)
                                if self.ui.checkBox_4.isChecked():
                                    self.w1.setXRange(tsim[1] - 240, tsim[1], padding=0)
                                else:
                                    self.w1.setXRange(tsim[1] - 720, tsim[1], padding=0)
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
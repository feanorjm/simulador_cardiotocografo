# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\JUAN\Dropbox\workspaceAptana\Cardio2.7\PlotGuiFinal6.ui'
#
# Created: Tue Jul 29 20:16:07 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1360, 706)
        Dialog.setMouseTracking(False)
        self.tabWidget_s1 = QtGui.QTabWidget(Dialog)
        self.tabWidget_s1.setGeometry(QtCore.QRect(20, 490, 531, 211))
        self.tabWidget_s1.setObjectName(_fromUtf8("tabWidget_s1"))
        self.tab_s1 = QtGui.QWidget()
        self.tab_s1.setObjectName(_fromUtf8("tab_s1"))
        self.label_s3 = QtGui.QLabel(self.tab_s1)
        self.label_s3.setGeometry(QtCore.QRect(10, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_s3.setFont(font)
        self.label_s3.setObjectName(_fromUtf8("label_s3"))
        self.lineEdit_s3 = QtGui.QLineEdit(self.tab_s1)
        self.lineEdit_s3.setGeometry(QtCore.QRect(200, 70, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_s3.setFont(font)
        self.lineEdit_s3.setObjectName(_fromUtf8("lineEdit_s3"))
        self.lineEdit_s1 = QtGui.QLineEdit(self.tab_s1)
        self.lineEdit_s1.setGeometry(QtCore.QRect(200, 10, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_s1.setFont(font)
        self.lineEdit_s1.setObjectName(_fromUtf8("lineEdit_s1"))
        self.label_s1 = QtGui.QLabel(self.tab_s1)
        self.label_s1.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_s1.setFont(font)
        self.label_s1.setObjectName(_fromUtf8("label_s1"))
        self.label_s4 = QtGui.QLabel(self.tab_s1)
        self.label_s4.setGeometry(QtCore.QRect(10, 100, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_s4.setFont(font)
        self.label_s4.setObjectName(_fromUtf8("label_s4"))
        self.lineEdit_s2 = QtGui.QLineEdit(self.tab_s1)
        self.lineEdit_s2.setGeometry(QtCore.QRect(200, 40, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_s2.setFont(font)
        self.lineEdit_s2.setObjectName(_fromUtf8("lineEdit_s2"))
        self.label_s2 = QtGui.QLabel(self.tab_s1)
        self.label_s2.setGeometry(QtCore.QRect(10, 40, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_s2.setFont(font)
        self.label_s2.setObjectName(_fromUtf8("label_s2"))
        self.lineEdit_s4 = QtGui.QLineEdit(self.tab_s1)
        self.lineEdit_s4.setGeometry(QtCore.QRect(200, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_s4.setFont(font)
        self.lineEdit_s4.setObjectName(_fromUtf8("lineEdit_s4"))
        self.label_s5 = QtGui.QLabel(self.tab_s1)
        self.label_s5.setGeometry(QtCore.QRect(300, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_s5.setFont(font)
        self.label_s5.setObjectName(_fromUtf8("label_s5"))
        self.tabWidget_s1.addTab(self.tab_s1, _fromUtf8(""))
        self.tab_s2 = QtGui.QWidget()
        self.tab_s2.setObjectName(_fromUtf8("tab_s2"))
        self.label_s6 = QtGui.QLabel(self.tab_s2)
        self.label_s6.setGeometry(QtCore.QRect(30, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_s6.setFont(font)
        self.label_s6.setScaledContents(False)
        self.label_s6.setWordWrap(True)
        self.label_s6.setObjectName(_fromUtf8("label_s6"))
        self.horizontalSlider_s1 = QtGui.QSlider(self.tab_s2)
        self.horizontalSlider_s1.setGeometry(QtCore.QRect(190, 10, 160, 19))
        self.horizontalSlider_s1.setMinimum(1)
        self.horizontalSlider_s1.setMaximum(8)
        self.horizontalSlider_s1.setSingleStep(1)
        self.horizontalSlider_s1.setPageStep(2)
        self.horizontalSlider_s1.setProperty("value", 1)
        self.horizontalSlider_s1.setTracking(False)
        self.horizontalSlider_s1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_s1.setInvertedControls(False)
        self.horizontalSlider_s1.setTickPosition(QtGui.QSlider.TicksAbove)
        self.horizontalSlider_s1.setTickInterval(1)
        self.horizontalSlider_s1.setObjectName(_fromUtf8("horizontalSlider_s1"))
        self.lineEdit_s5 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s5.setGeometry(QtCore.QRect(40, 100, 71, 22))
        self.lineEdit_s5.setText(_fromUtf8(""))
        self.lineEdit_s5.setObjectName(_fromUtf8("lineEdit_s5"))
        self.comboBox_s1 = QtGui.QComboBox(self.tab_s2)
        self.comboBox_s1.setGeometry(QtCore.QRect(140, 100, 69, 20))
        self.comboBox_s1.setObjectName(_fromUtf8("comboBox_s1"))
        self.label_11 = QtGui.QLabel(self.tab_s2)
        self.label_11.setGeometry(QtCore.QRect(20, 101, 16, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_s7 = QtGui.QLabel(self.tab_s2)
        self.label_s7.setGeometry(QtCore.QRect(50, 80, 61, 16))
        self.label_s7.setObjectName(_fromUtf8("label_s7"))
        self.label_s8 = QtGui.QLabel(self.tab_s2)
        self.label_s8.setGeometry(QtCore.QRect(130, 80, 91, 16))
        self.label_s8.setObjectName(_fromUtf8("label_s8"))
        self.label_s12 = QtGui.QLabel(self.tab_s2)
        self.label_s12.setGeometry(QtCore.QRect(20, 128, 16, 16))
        self.label_s12.setObjectName(_fromUtf8("label_s12"))
        self.comboBox_s2 = QtGui.QComboBox(self.tab_s2)
        self.comboBox_s2.setGeometry(QtCore.QRect(140, 127, 69, 20))
        self.comboBox_s2.setObjectName(_fromUtf8("comboBox_s2"))
        self.lineEdit_s6 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s6.setGeometry(QtCore.QRect(40, 127, 71, 21))
        self.lineEdit_s6.setText(_fromUtf8(""))
        self.lineEdit_s6.setObjectName(_fromUtf8("lineEdit_s6"))
        self.label_s13 = QtGui.QLabel(self.tab_s2)
        self.label_s13.setGeometry(QtCore.QRect(20, 154, 16, 16))
        self.label_s13.setObjectName(_fromUtf8("label_s13"))
        self.comboBox_s3 = QtGui.QComboBox(self.tab_s2)
        self.comboBox_s3.setGeometry(QtCore.QRect(140, 153, 69, 20))
        self.comboBox_s3.setObjectName(_fromUtf8("comboBox_s3"))
        self.lineEdit_s7 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s7.setGeometry(QtCore.QRect(40, 153, 71, 22))
        self.lineEdit_s7.setText(_fromUtf8(""))
        self.lineEdit_s7.setObjectName(_fromUtf8("lineEdit_s7"))
        self.label_s14 = QtGui.QLabel(self.tab_s2)
        self.label_s14.setGeometry(QtCore.QRect(20, 181, 16, 16))
        self.label_s14.setObjectName(_fromUtf8("label_s14"))
        self.comboBox_s4 = QtGui.QComboBox(self.tab_s2)
        self.comboBox_s4.setGeometry(QtCore.QRect(140, 180, 69, 20))
        self.comboBox_s4.setObjectName(_fromUtf8("comboBox_s4"))
        self.lineEdit_s8 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s8.setGeometry(QtCore.QRect(40, 180, 71, 21))
        self.lineEdit_s8.setText(_fromUtf8(""))
        self.lineEdit_s8.setObjectName(_fromUtf8("lineEdit_s8"))
        self.label_s15 = QtGui.QLabel(self.tab_s2)
        self.label_s15.setGeometry(QtCore.QRect(20, 207, 16, 16))
        self.label_s15.setObjectName(_fromUtf8("label_s15"))
        self.comboBox_s5 = QtGui.QComboBox(self.tab_s2)
        self.comboBox_s5.setGeometry(QtCore.QRect(140, 206, 69, 20))
        self.comboBox_s5.setObjectName(_fromUtf8("comboBox_s5"))
        self.lineEdit_s9 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s9.setGeometry(QtCore.QRect(40, 206, 71, 22))
        self.lineEdit_s9.setText(_fromUtf8(""))
        self.lineEdit_s9.setObjectName(_fromUtf8("lineEdit_s9"))
        self.label_s16 = QtGui.QLabel(self.tab_s2)
        self.label_s16.setGeometry(QtCore.QRect(20, 234, 16, 16))
        self.label_s16.setObjectName(_fromUtf8("label_s16"))
        self.comboBox_s6 = QtGui.QComboBox(self.tab_s2)
        self.comboBox_s6.setGeometry(QtCore.QRect(140, 233, 69, 20))
        self.comboBox_s6.setObjectName(_fromUtf8("comboBox_s6"))
        self.lineEdit_s10 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s10.setGeometry(QtCore.QRect(40, 233, 71, 22))
        self.lineEdit_s10.setText(_fromUtf8(""))
        self.lineEdit_s10.setObjectName(_fromUtf8("lineEdit_s10"))
        self.label_s17 = QtGui.QLabel(self.tab_s2)
        self.label_s17.setGeometry(QtCore.QRect(20, 261, 16, 16))
        self.label_s17.setObjectName(_fromUtf8("label_s17"))
        self.comboBox_s7 = QtGui.QComboBox(self.tab_s2)
        self.comboBox_s7.setGeometry(QtCore.QRect(140, 260, 69, 20))
        self.comboBox_s7.setObjectName(_fromUtf8("comboBox_s7"))
        self.lineEdit_s11 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s11.setGeometry(QtCore.QRect(40, 260, 71, 21))
        self.lineEdit_s11.setText(_fromUtf8(""))
        self.lineEdit_s11.setObjectName(_fromUtf8("lineEdit_s11"))
        self.comboBox_s8 = QtGui.QComboBox(self.tab_s2)
        self.comboBox_s8.setGeometry(QtCore.QRect(140, 286, 69, 20))
        self.comboBox_s8.setObjectName(_fromUtf8("comboBox_s8"))
        self.lineEdit_s12 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s12.setGeometry(QtCore.QRect(40, 286, 71, 22))
        self.lineEdit_s12.setText(_fromUtf8(""))
        self.lineEdit_s12.setObjectName(_fromUtf8("lineEdit_s12"))
        self.label_s18 = QtGui.QLabel(self.tab_s2)
        self.label_s18.setGeometry(QtCore.QRect(20, 287, 16, 16))
        self.label_s18.setObjectName(_fromUtf8("label_s18"))
        self.label_s25 = QtGui.QLabel(self.tab_s2)
        self.label_s25.setGeometry(QtCore.QRect(360, 10, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_s25.setFont(font)
        self.label_s25.setText(_fromUtf8(""))
        self.label_s25.setObjectName(_fromUtf8("label_s25"))
        self.lineEdit_s15 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s15.setGeometry(QtCore.QRect(240, 153, 71, 22))
        self.lineEdit_s15.setText(_fromUtf8(""))
        self.lineEdit_s15.setObjectName(_fromUtf8("lineEdit_s15"))
        self.lineEdit_s18 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s18.setGeometry(QtCore.QRect(240, 233, 71, 22))
        self.lineEdit_s18.setText(_fromUtf8(""))
        self.lineEdit_s18.setObjectName(_fromUtf8("lineEdit_s18"))
        self.lineEdit_s17 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s17.setGeometry(QtCore.QRect(240, 206, 71, 22))
        self.lineEdit_s17.setText(_fromUtf8(""))
        self.lineEdit_s17.setObjectName(_fromUtf8("lineEdit_s17"))
        self.label_s9 = QtGui.QLabel(self.tab_s2)
        self.label_s9.setGeometry(QtCore.QRect(250, 80, 61, 16))
        self.label_s9.setObjectName(_fromUtf8("label_s9"))
        self.lineEdit_s13 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s13.setGeometry(QtCore.QRect(240, 100, 71, 22))
        self.lineEdit_s13.setText(_fromUtf8(""))
        self.lineEdit_s13.setObjectName(_fromUtf8("lineEdit_s13"))
        self.lineEdit_s20 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s20.setGeometry(QtCore.QRect(240, 286, 71, 22))
        self.lineEdit_s20.setText(_fromUtf8(""))
        self.lineEdit_s20.setObjectName(_fromUtf8("lineEdit_s20"))
        self.lineEdit_s16 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s16.setGeometry(QtCore.QRect(240, 180, 71, 21))
        self.lineEdit_s16.setText(_fromUtf8(""))
        self.lineEdit_s16.setObjectName(_fromUtf8("lineEdit_s16"))
        self.lineEdit_s19 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s19.setGeometry(QtCore.QRect(240, 260, 71, 21))
        self.lineEdit_s19.setText(_fromUtf8(""))
        self.lineEdit_s19.setObjectName(_fromUtf8("lineEdit_s19"))
        self.lineEdit_s14 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s14.setGeometry(QtCore.QRect(240, 127, 71, 21))
        self.lineEdit_s14.setText(_fromUtf8(""))
        self.lineEdit_s14.setObjectName(_fromUtf8("lineEdit_s14"))
        self.lineEdit_s23 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s23.setGeometry(QtCore.QRect(330, 153, 71, 22))
        self.lineEdit_s23.setText(_fromUtf8(""))
        self.lineEdit_s23.setObjectName(_fromUtf8("lineEdit_s23"))
        self.lineEdit_s26 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s26.setGeometry(QtCore.QRect(330, 233, 71, 22))
        self.lineEdit_s26.setText(_fromUtf8(""))
        self.lineEdit_s26.setObjectName(_fromUtf8("lineEdit_s26"))
        self.lineEdit_s25 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s25.setGeometry(QtCore.QRect(330, 206, 71, 22))
        self.lineEdit_s25.setText(_fromUtf8(""))
        self.lineEdit_s25.setObjectName(_fromUtf8("lineEdit_s25"))
        self.label_s10 = QtGui.QLabel(self.tab_s2)
        self.label_s10.setGeometry(QtCore.QRect(331, 80, 81, 16))
        self.label_s10.setObjectName(_fromUtf8("label_s10"))
        self.lineEdit_s21 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s21.setGeometry(QtCore.QRect(330, 100, 71, 22))
        self.lineEdit_s21.setText(_fromUtf8(""))
        self.lineEdit_s21.setObjectName(_fromUtf8("lineEdit_s21"))
        self.lineEdit_s28 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s28.setGeometry(QtCore.QRect(330, 286, 71, 22))
        self.lineEdit_s28.setText(_fromUtf8(""))
        self.lineEdit_s28.setObjectName(_fromUtf8("lineEdit_s28"))
        self.lineEdit_s24 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s24.setGeometry(QtCore.QRect(330, 180, 71, 21))
        self.lineEdit_s24.setText(_fromUtf8(""))
        self.lineEdit_s24.setObjectName(_fromUtf8("lineEdit_s24"))
        self.lineEdit_s27 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s27.setGeometry(QtCore.QRect(330, 260, 71, 21))
        self.lineEdit_s27.setText(_fromUtf8(""))
        self.lineEdit_s27.setObjectName(_fromUtf8("lineEdit_s27"))
        self.lineEdit_s22 = QtGui.QLineEdit(self.tab_s2)
        self.lineEdit_s22.setGeometry(QtCore.QRect(330, 127, 71, 21))
        self.lineEdit_s22.setText(_fromUtf8(""))
        self.lineEdit_s22.setObjectName(_fromUtf8("lineEdit_s22"))
        self.label_s26 = QtGui.QLabel(self.tab_s2)
        self.label_s26.setGeometry(QtCore.QRect(420, 101, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_s26.setFont(font)
        self.label_s26.setObjectName(_fromUtf8("label_s26"))
        self.label_s27 = QtGui.QLabel(self.tab_s2)
        self.label_s27.setGeometry(QtCore.QRect(420, 128, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_s27.setFont(font)
        self.label_s27.setObjectName(_fromUtf8("label_s27"))
        self.label_s28 = QtGui.QLabel(self.tab_s2)
        self.label_s28.setGeometry(QtCore.QRect(420, 154, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_s28.setFont(font)
        self.label_s28.setObjectName(_fromUtf8("label_s28"))
        self.label_s29 = QtGui.QLabel(self.tab_s2)
        self.label_s29.setGeometry(QtCore.QRect(420, 181, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_s29.setFont(font)
        self.label_s29.setObjectName(_fromUtf8("label_s29"))
        self.label_s30 = QtGui.QLabel(self.tab_s2)
        self.label_s30.setGeometry(QtCore.QRect(420, 207, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_s30.setFont(font)
        self.label_s30.setObjectName(_fromUtf8("label_s30"))
        self.label_s31 = QtGui.QLabel(self.tab_s2)
        self.label_s31.setGeometry(QtCore.QRect(420, 234, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_s31.setFont(font)
        self.label_s31.setObjectName(_fromUtf8("label_s31"))
        self.label_s32 = QtGui.QLabel(self.tab_s2)
        self.label_s32.setGeometry(QtCore.QRect(420, 261, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_s32.setFont(font)
        self.label_s32.setObjectName(_fromUtf8("label_s32"))
        self.label_s33 = QtGui.QLabel(self.tab_s2)
        self.label_s33.setGeometry(QtCore.QRect(420, 287, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_s33.setFont(font)
        self.label_s33.setObjectName(_fromUtf8("label_s33"))
        self.tabWidget_s1.addTab(self.tab_s2, _fromUtf8(""))
        self.graphicsView = GraphicsLayoutWidget(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(20, 10, 841, 461))
        self.graphicsView.setMouseTracking(False)
        self.graphicsView.setStyleSheet(_fromUtf8(""))
        self.graphicsView.setLineWidth(5)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(360, 240, 141, 41))
        self.progressBar.setProperty("value", 50)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(730, 490, 231, 211))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton_s2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_s2.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.radioButton_s2.setObjectName(_fromUtf8("radioButton_s2"))
        self.label_s21 = QtGui.QLabel(self.groupBox)
        self.label_s21.setGeometry(QtCore.QRect(10, 42, 46, 13))
        self.label_s21.setObjectName(_fromUtf8("label_s21"))
        self.checkBox_s4 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_s4.setGeometry(QtCore.QRect(140, 40, 81, 17))
        self.checkBox_s4.setObjectName(_fromUtf8("checkBox_s4"))
        self.radioButton_s4 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_s4.setGeometry(QtCore.QRect(10, 130, 82, 17))
        self.radioButton_s4.setObjectName(_fromUtf8("radioButton_s4"))
        self.checkBox_s3 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_s3.setGeometry(QtCore.QRect(60, 40, 70, 17))
        self.checkBox_s3.setObjectName(_fromUtf8("checkBox_s3"))
        self.radioButton_s3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_s3.setGeometry(QtCore.QRect(10, 110, 82, 17))
        self.radioButton_s3.setObjectName(_fromUtf8("radioButton_s3"))
        self.line_s1 = QtGui.QFrame(self.groupBox)
        self.line_s1.setGeometry(QtCore.QRect(0, 24, 230, 16))
        self.line_s1.setFrameShape(QtGui.QFrame.HLine)
        self.line_s1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_s1.setObjectName(_fromUtf8("line_s1"))
        self.radioButton_s1 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_s1.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_s1.setObjectName(_fromUtf8("radioButton_s1"))
        self.lcdNumber = QtGui.QLCDNumber(self.groupBox)
        self.lcdNumber.setGeometry(QtCore.QRect(170, 7, 51, 21))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.label_s20 = QtGui.QLabel(self.groupBox)
        self.label_s20.setGeometry(QtCore.QRect(111, 6, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_s20.setFont(font)
        self.label_s20.setObjectName(_fromUtf8("label_s20"))
        self.radioButton_s5 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_s5.setGeometry(QtCore.QRect(10, 150, 82, 17))
        self.radioButton_s5.setObjectName(_fromUtf8("radioButton_s5"))
        self.pushButton_s2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_s2.setGeometry(QtCore.QRect(110, 160, 101, 41))
        self.pushButton_s2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_s2.setObjectName(_fromUtf8("pushButton_s2"))
        self.checkBox_s2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_s2.setGeometry(QtCore.QRect(10, 10, 101, 17))
        self.checkBox_s2.setObjectName(_fromUtf8("checkBox_s2"))
        self.lineEdit_s29 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_s29.setGeometry(QtCore.QRect(110, 90, 51, 21))
        self.lineEdit_s29.setText(_fromUtf8(""))
        self.lineEdit_s29.setObjectName(_fromUtf8("lineEdit_s29"))
        self.lineEdit_s30 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_s30.setGeometry(QtCore.QRect(110, 130, 51, 22))
        self.lineEdit_s30.setText(_fromUtf8(""))
        self.lineEdit_s30.setObjectName(_fromUtf8("lineEdit_s30"))
        self.label_s22 = QtGui.QLabel(self.groupBox)
        self.label_s22.setGeometry(QtCore.QRect(110, 70, 61, 16))
        self.label_s22.setObjectName(_fromUtf8("label_s22"))
        self.label_s23 = QtGui.QLabel(self.groupBox)
        self.label_s23.setGeometry(QtCore.QRect(110, 110, 81, 16))
        self.label_s23.setObjectName(_fromUtf8("label_s23"))
        self.label_s24 = QtGui.QLabel(Dialog)
        self.label_s24.setGeometry(QtCore.QRect(70, 20, 71, 16))
        self.label_s24.setObjectName(_fromUtf8("label_s24"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(565, 490, 151, 211))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.checkBox_s1 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_s1.setGeometry(QtCore.QRect(30, 70, 91, 20))
        self.checkBox_s1.setObjectName(_fromUtf8("checkBox_s1"))
        self.pushButton_s1 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_s1.setGeometry(QtCore.QRect(10, 10, 131, 51))
        self.pushButton_s1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_s1.setObjectName(_fromUtf8("pushButton_s1"))
        self.label_s19 = QtGui.QLabel(self.groupBox_2)
        self.label_s19.setGeometry(QtCore.QRect(90, 130, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_s19.setFont(font)
        self.label_s19.setObjectName(_fromUtf8("label_s19"))
        self.comboBox_s9 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_s9.setGeometry(QtCore.QRect(90, 110, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_s9.setFont(font)
        self.comboBox_s9.setEditable(False)
        self.comboBox_s9.setObjectName(_fromUtf8("comboBox_s9"))

        self.retranslateUi(Dialog)
        self.tabWidget_s1.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_s3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Basal:</span></p></body></html>", None))
        self.lineEdit_s3.setText(_translate("Dialog", "140", None))
        self.lineEdit_s1.setText(_translate("Dialog", "1000", None))
        self.label_s1.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tiempo de registro:</span></p></body></html>", None))
        self.label_s4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Amplitud de la variabilidad</span></p></body></html>", None))
        self.lineEdit_s2.setText(_translate("Dialog", "5", None))
        self.label_s2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Movimientos fetales/10 min:</span></p></body></html>", None))
        self.lineEdit_s4.setText(_translate("Dialog", "140", None))
        self.label_s5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Basal:</span></p></body></html>", None))
        self.tabWidget_s1.setTabText(self.tabWidget_s1.indexOf(self.tab_s1), _translate("Dialog", "Frecuencia Cardiaca", None))
        self.label_s6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Nº de Contracciones</span></p></body></html>", None))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">1</span></p></body></html>", None))
        self.label_s7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Instante</span></p></body></html>", None))
        self.label_s8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Desaceleración</span></p></body></html>", None))
        self.label_s12.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">2</span></p></body></html>", None))
        self.label_s13.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">3</span></p></body></html>", None))
        self.label_s14.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">4</span></p></body></html>", None))
        self.label_s15.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">5</span></p></body></html>", None))
        self.label_s16.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">6</span></p></body></html>", None))
        self.label_s17.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">7</span></p></body></html>", None))
        self.label_s18.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">8</span></p></body></html>", None))
        self.label_s9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Duración</span></p></body></html>", None))
        self.label_s10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Profundidad</span></p></body></html>", None))
        self.label_s26.setText(_translate("Dialog", "Label_s26", None))
        self.label_s27.setText(_translate("Dialog", "Label_s27", None))
        self.label_s28.setText(_translate("Dialog", "Label_s28", None))
        self.label_s29.setText(_translate("Dialog", "Label_s29", None))
        self.label_s30.setText(_translate("Dialog", "Label_s30", None))
        self.label_s31.setText(_translate("Dialog", "Label_s31", None))
        self.label_s32.setText(_translate("Dialog", "Label_s32", None))
        self.label_s33.setText(_translate("Dialog", "Label_s33", None))
        self.tabWidget_s1.setTabText(self.tabWidget_s1.indexOf(self.tab_s2), _translate("Dialog", "Contracción Uterina", None))
        self.radioButton_s2.setText(_translate("Dialog", "Precoz", None))
        self.label_s21.setText(_translate("Dialog", "Generar:", None))
        self.checkBox_s4.setText(_translate("Dialog", "Contracción", None))
        self.radioButton_s4.setText(_translate("Dialog", "Variable", None))
        self.checkBox_s3.setText(_translate("Dialog", "Mov. Fetal", None))
        self.radioButton_s3.setText(_translate("Dialog", "Tardía", None))
        self.radioButton_s1.setText(_translate("Dialog", "Ninguna", None))
        self.label_s20.setText(_translate("Dialog", "Tiempo (s)", None))
        self.radioButton_s5.setText(_translate("Dialog", "Prolongada", None))
        self.pushButton_s2.setText(_translate("Dialog", "Generar", None))
        self.checkBox_s2.setText(_translate("Dialog", "1 cm/min", None))
        self.label_s22.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Duración</span></p></body></html>", None))
        self.label_s23.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Profundidad</span></p></body></html>", None))
        self.label_s24.setText(_translate("Dialog", "TextLabel", None))
        self.checkBox_s1.setText(_translate("Dialog", "Señal estática", None))
        self.pushButton_s1.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>", None))
        self.pushButton_s1.setText(_translate("Dialog", "Simulación", None))
        self.label_s19.setText(_translate("Dialog", "Velocidad", None))

from pyqtgraph import GraphicsLayoutWidget

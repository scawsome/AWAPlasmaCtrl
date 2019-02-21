# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlasmaCtrlDlg.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import logging
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread, QTimer
#import visa

import VisaHandler

class Ui_PlasmaCtrlDlg(object):
    mytimer=QTimer()
    def setupUi(self, PlasmaCtrlDlg):
        PlasmaCtrlDlg.setObjectName("PlasmaCtrlDlg")
        PlasmaCtrlDlg.setWindowModality(QtCore.Qt.ApplicationModal)
        PlasmaCtrlDlg.resize(602, 444)
        self.dummybutton = QtWidgets.QPushButton(PlasmaCtrlDlg)
        self.dummybutton.setGeometry(QtCore.QRect(480, 400, 94, 27))
        self.dummybutton.setObjectName("dummybutton")        
        self.InitalizeButton = QtWidgets.QPushButton(PlasmaCtrlDlg)
        self.InitalizeButton.setGeometry(QtCore.QRect(480, 400, 94, 27))
        self.InitalizeButton.setObjectName("InitalizeButton")
        self.IonGaugeCtrl = QtWidgets.QGroupBox(PlasmaCtrlDlg)
        self.IonGaugeCtrl.setGeometry(QtCore.QRect(390, 30, 191, 171))
        self.IonGaugeCtrl.setFlat(False)
        self.IonGaugeCtrl.setObjectName("IonGaugeCtrl")
        self.label = QtWidgets.QLabel(self.IonGaugeCtrl)
        self.label.setGeometry(QtCore.QRect(10, 50, 31, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.IonGaugeCtrl)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 31, 20))
        self.label_2.setObjectName("label_2")
        self.IONGauge = QtWidgets.QLineEdit(self.IonGaugeCtrl)
        self.IONGauge.setGeometry(QtCore.QRect(50, 40, 131, 31))
        self.IONGauge.setObjectName("IONGauge")
        self.GaugeA = QtWidgets.QLineEdit(self.IonGaugeCtrl)
        self.GaugeA.setGeometry(QtCore.QRect(50, 70, 131, 31))
        self.GaugeA.setObjectName("GaugeA")
        self.GaugeB = QtWidgets.QLineEdit(self.IonGaugeCtrl)
        self.GaugeB.setGeometry(QtCore.QRect(50, 100, 131, 31))
        self.GaugeB.setObjectName("GaugeB")
        self.label_15 = QtWidgets.QLabel(self.IonGaugeCtrl)
        self.label_15.setGeometry(QtCore.QRect(10, 110, 31, 19))
        self.label_15.setObjectName("label_15")
        self.DCR55_180T = QtWidgets.QGroupBox(PlasmaCtrlDlg)
        self.DCR55_180T.setGeometry(QtCore.QRect(20, 10, 251, 131))
        self.DCR55_180T.setObjectName("DCR55_180T")
        self.label_3 = QtWidgets.QLabel(self.DCR55_180T)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 21, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.DCR55_180T)
        self.label_4.setGeometry(QtCore.QRect(50, 30, 64, 19))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.DCR55_180T)
        self.label_5.setGeometry(QtCore.QRect(150, 30, 64, 19))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.DCR55_180T)
        self.label_6.setGeometry(QtCore.QRect(23, 90, 16, 20))
        self.label_6.setObjectName("label_6")
        self.DCR55VSet = QtWidgets.QLineEdit(self.DCR55_180T)
        self.DCR55VSet.setGeometry(QtCore.QRect(40, 50, 81, 31))
        self.DCR55VSet.setObjectName("DCR55VSet")
        self.DCR55ISet = QtWidgets.QLineEdit(self.DCR55_180T)
        self.DCR55ISet.setGeometry(QtCore.QRect(40, 80, 81, 31))
        self.DCR55ISet.setObjectName("DCR55ISet")
        self.DCR55VRead = QtWidgets.QLineEdit(self.DCR55_180T)
        self.DCR55VRead.setGeometry(QtCore.QRect(130, 50, 91, 31))
        self.DCR55VRead.setObjectName("DCR55VRead")
        self.DCR55IRead = QtWidgets.QLineEdit(self.DCR55_180T)
        self.DCR55IRead.setGeometry(QtCore.QRect(130, 80, 91, 31))
        self.DCR55IRead.setObjectName("DCR55IRead")
        self.DCR55_180T_2 = QtWidgets.QGroupBox(PlasmaCtrlDlg)
        self.DCR55_180T_2.setGeometry(QtCore.QRect(20, 150, 251, 131))
        self.DCR55_180T_2.setObjectName("DCR55_180T_2")
        self.label_7 = QtWidgets.QLabel(self.DCR55_180T_2)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 21, 19))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.DCR55_180T_2)
        self.label_8.setGeometry(QtCore.QRect(50, 30, 64, 19))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.DCR55_180T_2)
        self.label_9.setGeometry(QtCore.QRect(150, 30, 64, 19))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.DCR55_180T_2)
        self.label_10.setGeometry(QtCore.QRect(23, 90, 16, 20))
        self.label_10.setObjectName("label_10")
        self.HEATERVSet = QtWidgets.QLineEdit(self.DCR55_180T_2)
        self.HEATERVSet.setGeometry(QtCore.QRect(40, 50, 81, 31))
        self.HEATERVSet.setObjectName("HEATERVSet")
        self.HEATERISet = QtWidgets.QLineEdit(self.DCR55_180T_2)
        self.HEATERISet.setGeometry(QtCore.QRect(40, 80, 81, 31))
        self.HEATERISet.setObjectName("HEATERISet")
        self.HEATERVRead = QtWidgets.QLineEdit(self.DCR55_180T_2)
        self.HEATERVRead.setGeometry(QtCore.QRect(130, 50, 91, 31))
        self.HEATERVRead.setObjectName("HEATERVRead")
        self.HEATERIRead = QtWidgets.QLineEdit(self.DCR55_180T_2)
        self.HEATERIRead.setGeometry(QtCore.QRect(130, 80, 91, 31))
        self.HEATERIRead.setObjectName("HEATERIRead")
        self.DCR55_180T_3 = QtWidgets.QGroupBox(PlasmaCtrlDlg)
        self.DCR55_180T_3.setGeometry(QtCore.QRect(20, 290, 251, 131))
        self.DCR55_180T_3.setObjectName("DCR55_180T_3")
        self.label_11 = QtWidgets.QLabel(self.DCR55_180T_3)
        self.label_11.setGeometry(QtCore.QRect(20, 60, 21, 19))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.DCR55_180T_3)
        self.label_12.setGeometry(QtCore.QRect(50, 30, 64, 19))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.DCR55_180T_3)
        self.label_13.setGeometry(QtCore.QRect(150, 30, 64, 19))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.DCR55_180T_3)
        self.label_14.setGeometry(QtCore.QRect(23, 90, 16, 20))
        self.label_14.setObjectName("label_14")
        self.DISCHARGEVSet = QtWidgets.QLineEdit(self.DCR55_180T_3)
        self.DISCHARGEVSet.setGeometry(QtCore.QRect(40, 50, 81, 31))
        self.DISCHARGEVSet.setObjectName("DISCHARGEVSet")
        self.DISCHARGEISet = QtWidgets.QLineEdit(self.DCR55_180T_3)
        self.DISCHARGEISet.setGeometry(QtCore.QRect(40, 80, 81, 31))
        self.DISCHARGEISet.setObjectName("DISCHARGEISet")
        self.DISCHARGEVRead = QtWidgets.QLineEdit(self.DCR55_180T_3)
        self.DISCHARGEVRead.setGeometry(QtCore.QRect(130, 50, 91, 31))
        self.DISCHARGEVRead.setObjectName("DISCHARGEVRead")
        self.DISCHARGEIRead = QtWidgets.QLineEdit(self.DCR55_180T_3)
        self.DISCHARGEIRead.setGeometry(QtCore.QRect(130, 80, 91, 31))
        self.DISCHARGEIRead.setObjectName("DISCHARGEIRead")
        self.CloseButton = QtWidgets.QPushButton(PlasmaCtrlDlg)
        self.CloseButton.setGeometry(QtCore.QRect(370, 400, 94, 27))
        self.CloseButton.setObjectName("CloseButton")

        self.retranslateUi(PlasmaCtrlDlg)
        self.InitalizeButton.clicked.connect(self.OnInitializeClicked)
        self.DCR55VSet.returnPressed.connect(self.OnDCR55VSetChanged)
        self.DCR55ISet.returnPressed.connect(self.OnDCR55ISetChanged)
        self.HEATERISet.returnPressed.connect(self.OnHEATERISetChanged)
        self.HEATERVSet.returnPressed.connect(self.OnHEATERVSetChanged)
        self.DISCHARGEISet.returnPressed.connect(self.OnDISCHARGEISetChanged)
        self.DISCHARGEVSet.returnPressed.connect(self.OnDISCHARGEVSetChanged)
        self.CloseButton.clicked.connect(self.OnCloseButtonClicked)
        self.mytimer.timeout.connect(self.Update)
        QtCore.QMetaObject.connectSlotsByName(PlasmaCtrlDlg)

    def retranslateUi(self, PlasmaCtrlDlg):
        _translate = QtCore.QCoreApplication.translate
        PlasmaCtrlDlg.setWindowTitle(_translate("PlasmaCtrlDlg", "Plasma Ctrls"))
        self.InitalizeButton.setText(_translate("PlasmaCtrlDlg", "Initialize"))
        self.IonGaugeCtrl.setTitle(_translate("PlasmaCtrlDlg", "Terranova 934"))
        self.label.setText(_translate("PlasmaCtrlDlg", "IG:"))
        self.label_2.setText(_translate("PlasmaCtrlDlg", "A:"))
        self.label_15.setText(_translate("PlasmaCtrlDlg", "B:"))
        self.DCR55_180T.setTitle(_translate("PlasmaCtrlDlg", "DCR55-180T"))
        self.label_3.setText(_translate("PlasmaCtrlDlg", "V: "))
        self.label_4.setText(_translate("PlasmaCtrlDlg", "Set Val"))
        self.label_5.setText(_translate("PlasmaCtrlDlg", "RB Val"))
        self.label_6.setText(_translate("PlasmaCtrlDlg", "I:"))
        self.DCR55_180T_2.setTitle(_translate("PlasmaCtrlDlg", "Plasma Heater"))
        self.label_7.setText(_translate("PlasmaCtrlDlg", "V: "))
        self.label_8.setText(_translate("PlasmaCtrlDlg", "Set Val"))
        self.label_9.setText(_translate("PlasmaCtrlDlg", "RB Val"))
        self.label_10.setText(_translate("PlasmaCtrlDlg", "I:"))
        self.DCR55_180T_3.setTitle(_translate("PlasmaCtrlDlg", "Plasma Discharge"))
        self.label_11.setText(_translate("PlasmaCtrlDlg", "V: "))
        self.label_12.setText(_translate("PlasmaCtrlDlg", "Set Val"))
        self.label_13.setText(_translate("PlasmaCtrlDlg", "RB Val"))
        self.label_14.setText(_translate("PlasmaCtrlDlg", "I:"))
        self.CloseButton.setText(_translate("PlasmaCtrlDlg", "Close"))

    @pyqtSlot()
    def OnInitializeClicked(self):
        #open config file and initialize connections
        logging.debug("Initialize button clicked")
        self.mytimer.start(2000)

        #connections to the TDK power supplies
        #power supplies are connected via Ethernet in a chain with the heater one
        #the main one and the discharge as secondary
        #access to either one is done via the select_RS485_device() method
        
        tdk_address = '10.0.0.1'
        self.heater_RS485 = 0
        self.discharge_RS485 = 1
        
        self.TDK_PS = VisaHandler.VisaHandler(tdk_address)
        
        
        
    @pyqtSlot()
    def OnDCR55VSetChanged(self):
        #Send cmmands to DCR55 over GPIB to change voltage setting
        logging.debug("enter pressed on DCR55VSet")
        
    @pyqtSlot()
    def OnDCR55ISetChanged(self):
        #Send cmmands to DCR55 over GPIB to change Current setting
        logging.debug("enter pressed on DCR55ISet")
        
    @pyqtSlot()
    def OnHEATERVSetChanged(self):
        #Send cmmands to Heater TDK over ethernet to change voltage setting
        logging.debug("enter pressed on TDK#1VSet")
        self.TDK_PS.select_RS485_device(self.heater_RS485)
        self.TDK_PS.write(':VOLT {:3.2f}'.format(float(self.HEATERVSet.text())))
        
        
    @pyqtSlot()
    def OnHEATERISetChanged(self):
        #Send cmmands to Heater over ethernet to change current setting
        logging.debug("enter pressed on TDK#1ISet")
        self.TDK_PS.select_RS485_device(self.heater_RS485)
        self.TDK_PS.write(':CURR {:3.2f}'.format(float(self.HEATERISet.text())))
        

    @pyqtSlot()
    def OnDISCHARGEVSetChanged(self):
        #Send cmmands to Discharge over ethernet to change voltage setting
        logging.debug("enter pressed on TDK#2VSet")
        self.TDK_PS.select_RS485_device(self.discharge_RS485)
        self.TDK_PS.write(':VOLT {:3.2f}'.format(float(self.DISCHARGEVSet.text())))
        
        
    @pyqtSlot()
    def OnDISCHARGEISetChanged(self):
        #Send cmmands to TDK#2 over ethernet to change current setting
        logging.debug("enter pressed on TDK#2ISet")
        self.TDK_PS.select_RS485_device(self.discharge_RS485)
        self.TDK_PS.write(':CURR {:3.2f}'.format(float(self.HEATERISet.text())))
        
        
    @pyqtSlot()
    def OnCloseButtonClicked(self):
        #close the devices then close the ui
        logging.debug("enter pressed on Close button")
        self.mytimer.stop()
        
    @pyqtSlot()    
    def Update(self):
        logging.debug("updating timer")

        #update the values of TDIK power supplies
        self.TDK_PS.select_RS485_device(self.discharge_RS485)
        self.DISCHARGEVRead.setText(self.TDK_PS.query('MEAS:VOLT?'))
        self.DISCHARGEIRead.setText(self.TDK_PS.query('MEAS:CURR?'))

        self.TDK_PS.select_RS485_device(self.heater_RS485)
        self.HEATERVRead.setText(self.TDK_PS.query('MEAS:VOLT?'))
        self.HEATERIRead.setText(self.TDK_PS.query('MEAS:CURR?'))

        

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    
    global ui
    app = QtWidgets.QApplication(sys.argv)
    PlasmaCtrlDlg = QtWidgets.QDialog()
    ui = Ui_PlasmaCtrlDlg()
    ui.setupUi(PlasmaCtrlDlg)
    PlasmaCtrlDlg.show()
    app.exec_()
    del(ui)
    sys.exit()
        
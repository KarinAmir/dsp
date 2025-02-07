# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1028, 507)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 22))
        self.menubar.setObjectName("menubar")
        self.menuTrack = QtWidgets.QMenu(self.menubar)
        self.menuTrack.setObjectName("menuTrack")
        self.menupanel = QtWidgets.QMenu(self.menubar)
        self.menupanel.setObjectName("menupanel")
        self.menunavigation = QtWidgets.QMenu(self.menubar)
        self.menunavigation.setObjectName("menunavigation")
        self.menuprocessing = QtWidgets.QMenu(self.menubar)
        self.menuprocessing.setObjectName("menuprocessing")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_partition = QtWidgets.QAction(MainWindow)
        self.actionNew_partition.setObjectName("actionNew_partition")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionopen_2 = QtWidgets.QAction(MainWindow)
        self.actionopen_2.setObjectName("actionopen_2")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionremove = QtWidgets.QAction(MainWindow)
        self.actionremove.setObjectName("actionremove")
        self.actioninfo = QtWidgets.QAction(MainWindow)
        self.actioninfo.setObjectName("actioninfo")
        self.actionRendering_options = QtWidgets.QAction(MainWindow)
        self.actionRendering_options.setObjectName("actionRendering_options")
        self.actionMove_Left = QtWidgets.QAction(MainWindow)
        self.actionMove_Left.setObjectName("actionMove_Left")
        self.actionMove_Right = QtWidgets.QAction(MainWindow)
        self.actionMove_Right.setObjectName("actionMove_Right")
        self.actionGo_To_Beginning = QtWidgets.QAction(MainWindow)
        self.actionGo_To_Beginning.setObjectName("actionGo_To_Beginning")
        self.actionGo_To_End = QtWidgets.QAction(MainWindow)
        self.actionGo_To_End.setObjectName("actionGo_To_End")
        self.actionZoom_In = QtWidgets.QAction(MainWindow)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtWidgets.QAction(MainWindow)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionZoom_To_1_1 = QtWidgets.QAction(MainWindow)
        self.actionZoom_To_1_1.setObjectName("actionZoom_To_1_1")
        self.actionZoom_To_Fit = QtWidgets.QAction(MainWindow)
        self.actionZoom_To_Fit.setObjectName("actionZoom_To_Fit")
        self.actionNew_Panel = QtWidgets.QAction(MainWindow)
        self.actionNew_Panel.setObjectName("actionNew_Panel")
        self.actionClose_Panel = QtWidgets.QAction(MainWindow)
        self.actionClose_Panel.setObjectName("actionClose_Panel")
        self.actionMove_Up = QtWidgets.QAction(MainWindow)
        self.actionMove_Up.setObjectName("actionMove_Up")
        self.actionMove_Down = QtWidgets.QAction(MainWindow)
        self.actionMove_Down.setObjectName("actionMove_Down")
        self.actionIncrease_Hieght = QtWidgets.QAction(MainWindow)
        self.actionIncrease_Hieght.setObjectName("actionIncrease_Hieght")
        self.actionDecrease_Height = QtWidgets.QAction(MainWindow)
        self.actionDecrease_Height.setObjectName("actionDecrease_Height")
        self.actionShow_Cursor = QtWidgets.QAction(MainWindow)
        self.actionShow_Cursor.setObjectName("actionShow_Cursor")
        self.actionShow_X_Axis_Label = QtWidgets.QAction(MainWindow)
        self.actionShow_X_Axis_Label.setObjectName("actionShow_X_Axis_Label")
        self.actionSynchronize = QtWidgets.QAction(MainWindow)
        self.actionSynchronize.setObjectName("actionSynchronize")
        self.menuTrack.addAction(self.actionNew_partition)
        self.menuTrack.addAction(self.actionopen_2)
        self.menuTrack.addAction(self.actionsave)
        self.menuTrack.addAction(self.actionremove)
        self.menuTrack.addAction(self.actioninfo)
        self.menuTrack.addAction(self.actionRendering_options)
        self.menupanel.addAction(self.actionNew_Panel)
        self.menupanel.addAction(self.actionClose_Panel)
        self.menupanel.addAction(self.actionMove_Up)
        self.menupanel.addAction(self.actionMove_Down)
        self.menupanel.addAction(self.actionIncrease_Hieght)
        self.menupanel.addAction(self.actionDecrease_Height)
        self.menupanel.addAction(self.actionShow_Cursor)
        self.menupanel.addAction(self.actionShow_X_Axis_Label)
        self.menupanel.addAction(self.actionSynchronize)
        self.menunavigation.addAction(self.actionMove_Left)
        self.menunavigation.addAction(self.actionMove_Right)
        self.menunavigation.addAction(self.actionGo_To_Beginning)
        self.menunavigation.addAction(self.actionGo_To_End)
        self.menunavigation.addAction(self.actionZoom_In)
        self.menunavigation.addAction(self.actionZoom_Out)
        self.menunavigation.addAction(self.actionZoom_To_1_1)
        self.menunavigation.addAction(self.actionZoom_To_Fit)
        self.menubar.addAction(self.menuTrack.menuAction())
        self.menubar.addAction(self.menupanel.menuAction())
        self.menubar.addAction(self.menunavigation.menuAction())
        self.menubar.addAction(self.menuprocessing.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuTrack.setTitle(_translate("MainWindow", "Track"))
        self.menupanel.setTitle(_translate("MainWindow", "Panel"))
        self.menunavigation.setTitle(_translate("MainWindow", "Navigation"))
        self.menuprocessing.setTitle(_translate("MainWindow", "Processing"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_partition.setText(_translate("MainWindow", "New Partition"))
        self.actionopen.setText(_translate("MainWindow", "open "))
        self.actionopen_2.setText(_translate("MainWindow", "open"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionremove.setText(_translate("MainWindow", "remove"))
        self.actioninfo.setText(_translate("MainWindow", "info"))
        self.actionRendering_options.setText(_translate("MainWindow", "Rendering Options "))
        self.actionMove_Left.setText(_translate("MainWindow", "Move Left"))
        self.actionMove_Right.setText(_translate("MainWindow", "Move Right"))
        self.actionGo_To_Beginning.setText(_translate("MainWindow", "Go To Beginning "))
        self.actionGo_To_End.setText(_translate("MainWindow", "Go To End"))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionZoom_To_1_1.setText(_translate("MainWindow", "Zoom To 1:1"))
        self.actionZoom_To_Fit.setText(_translate("MainWindow", "Zoom To Fit"))
        self.actionNew_Panel.setText(_translate("MainWindow", "New Panel"))
        self.actionClose_Panel.setText(_translate("MainWindow", "Close Panel"))
        self.actionMove_Up.setText(_translate("MainWindow", "Move Up"))
        self.actionMove_Down.setText(_translate("MainWindow", "Move Down"))
        self.actionIncrease_Hieght.setText(_translate("MainWindow", "Increase Height"))
        self.actionDecrease_Height.setText(_translate("MainWindow", "Decrease Height"))
        self.actionShow_Cursor.setText(_translate("MainWindow", "Show Cursor"))
        self.actionShow_X_Axis_Label.setText(_translate("MainWindow", "Show X-Axis Label"))
        self.actionSynchronize.setText(_translate("MainWindow", "Synchronize"))

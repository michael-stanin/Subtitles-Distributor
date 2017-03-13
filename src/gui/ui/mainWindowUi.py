# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\Subtitles Distributor\src\gui\ui\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(320, 152)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(320, 152))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 152))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/subtitles_distributor_32_32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: #F0F8FF;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border-color: #87CEEB;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: #98FB98;\n"
"}\n"
"\n"
"QPushButton#stopBtn:disabled, #distributeBtn:disabled {\n"
"    /*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #D3D3D3, stop: 1 #f6f7fa);*/\n"
"    background-color: #D3D3D3;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 0 8px;\n"
"    background-color: #F5F5F5;\n"
"    /*background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);*/\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #87CEEB;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-color: #98FB98;\n"
"}\n"
"")
        MainWindow.setIconSize(QtCore.QSize(64, 64))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.moviesBrowseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.moviesBrowseBtn.setObjectName("moviesBrowseBtn")
        self.gridLayout.addWidget(self.moviesBrowseBtn, 0, 2, 1, 1)
        self.subtitlesBrowseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.subtitlesBrowseBtn.setObjectName("subtitlesBrowseBtn")
        self.gridLayout.addWidget(self.subtitlesBrowseBtn, 1, 2, 1, 1)
        self.moviesLine = QtWidgets.QLineEdit(self.centralwidget)
        self.moviesLine.setClearButtonEnabled(True)
        self.moviesLine.setObjectName("moviesLine")
        self.gridLayout.addWidget(self.moviesLine, 0, 0, 1, 2)
        self.subtitlesLine = QtWidgets.QLineEdit(self.centralwidget)
        self.subtitlesLine.setClearButtonEnabled(True)
        self.subtitlesLine.setObjectName("subtitlesLine")
        self.gridLayout.addWidget(self.subtitlesLine, 1, 0, 1, 2)
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopBtn.sizePolicy().hasHeightForWidth())
        self.stopBtn.setSizePolicy(sizePolicy)
        self.stopBtn.setObjectName("stopBtn")
        self.gridLayout.addWidget(self.stopBtn, 2, 2, 1, 1)
        self.distributeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.distributeBtn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distributeBtn.sizePolicy().hasHeightForWidth())
        self.distributeBtn.setSizePolicy(sizePolicy)
        self.distributeBtn.setObjectName("distributeBtn")
        self.gridLayout.addWidget(self.distributeBtn, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setToolTip("")
        self.statusbar.setToolTipDuration(1)
        self.statusbar.setStatusTip("")
        self.statusbar.setWhatsThis("")
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSoftware = QtWidgets.QAction(MainWindow)
        self.actionSoftware.setObjectName("actionSoftware")
        self.actionDefault_Movies_Folder = QtWidgets.QAction(MainWindow)
        self.actionDefault_Movies_Folder.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/movies.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDefault_Movies_Folder.setIcon(icon1)
        self.actionDefault_Movies_Folder.setObjectName("actionDefault_Movies_Folder")
        self.actionDefault_Subtitles_Folder = QtWidgets.QAction(MainWindow)
        self.actionDefault_Subtitles_Folder.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/subtitles.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDefault_Subtitles_Folder.setIcon(icon2)
        self.actionDefault_Subtitles_Folder.setObjectName("actionDefault_Subtitles_Folder")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDeveloper = QtWidgets.QAction(MainWindow)
        self.actionDeveloper.setObjectName("actionDeveloper")
        self.actionReset_Defaults = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset_Defaults.setIcon(icon3)
        self.actionReset_Defaults.setObjectName("actionReset_Defaults")
        self.actionLimitations = QtWidgets.QAction(MainWindow)
        self.actionLimitations.setObjectName("actionLimitations")
        self.actionLimitations_2 = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/limitations.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLimitations_2.setIcon(icon4)
        self.actionLimitations_2.setObjectName("actionLimitations_2")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon5)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDeveloper_2 = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/dev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeveloper_2.setIcon(icon6)
        self.actionDeveloper_2.setObjectName("actionDeveloper_2")
        self.menuSettings.addAction(self.actionDefault_Movies_Folder)
        self.menuSettings.addAction(self.actionDefault_Subtitles_Folder)
        self.menuSettings.addAction(self.actionReset_Defaults)
        self.menuSettings.addSeparator()
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionLimitations_2)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionDeveloper_2)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.moviesLine, self.moviesBrowseBtn)
        MainWindow.setTabOrder(self.moviesBrowseBtn, self.subtitlesLine)
        MainWindow.setTabOrder(self.subtitlesLine, self.subtitlesBrowseBtn)
        MainWindow.setTabOrder(self.subtitlesBrowseBtn, self.distributeBtn)
        MainWindow.setTabOrder(self.distributeBtn, self.stopBtn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Subtitles Distributor"))
        self.moviesBrowseBtn.setText(_translate("MainWindow", "Browse"))
        self.subtitlesBrowseBtn.setText(_translate("MainWindow", "Browse"))
        self.moviesLine.setPlaceholderText(_translate("MainWindow", "Movies folder location to watch."))
        self.subtitlesLine.setPlaceholderText(_translate("MainWindow", "Subtitles folder location to watch."))
        self.stopBtn.setText(_translate("MainWindow", "Stop!"))
        self.distributeBtn.setText(_translate("MainWindow", "Distribute!"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSoftware.setText(_translate("MainWindow", "Software"))
        self.actionDefault_Movies_Folder.setText(_translate("MainWindow", "Set Default Movies Folder"))
        self.actionDefault_Subtitles_Folder.setText(_translate("MainWindow", "Set Default Subtitles Folder"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDeveloper.setText(_translate("MainWindow", "Developer"))
        self.actionReset_Defaults.setText(_translate("MainWindow", "Reset Default Folders"))
        self.actionLimitations.setText(_translate("MainWindow", "Limitations"))
        self.actionLimitations_2.setText(_translate("MainWindow", "Limitations"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionDeveloper_2.setText(_translate("MainWindow", "Developer"))

from . import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


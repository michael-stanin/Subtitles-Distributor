# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\Subtitles Distributor\src\gui\ui\aboutWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("AboutWindow")
        AboutWindow.resize(372, 273)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutWindow.sizePolicy().hasHeightForWidth())
        AboutWindow.setSizePolicy(sizePolicy)
        AboutWindow.setMinimumSize(QtCore.QSize(372, 273))
        AboutWindow.setMaximumSize(QtCore.QSize(372, 273))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/subtitles_distributor_32_32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutWindow.setWindowIcon(icon)
        AboutWindow.setAutoFillBackground(False)
        AboutWindow.setStyleSheet("QDialog {\n"
"    background-color: #F0F8FF;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(AboutWindow)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_lbl = QtWidgets.QLabel(AboutWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_lbl.sizePolicy().hasHeightForWidth())
        self.logo_lbl.setSizePolicy(sizePolicy)
        self.logo_lbl.setMinimumSize(QtCore.QSize(0, 0))
        self.logo_lbl.setText("")
        self.logo_lbl.setPixmap(QtGui.QPixmap(":/icons/subtitles_distributor_64_64.png"))
        self.logo_lbl.setScaledContents(False)
        self.logo_lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.logo_lbl.setWordWrap(False)
        self.logo_lbl.setObjectName("logo_lbl")
        self.horizontalLayout_2.addWidget(self.logo_lbl)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.aboutArea = QtWidgets.QScrollArea(AboutWindow)
        self.aboutArea.setStyleSheet("background-color: #F0F8FF;")
        self.aboutArea.setWidgetResizable(True)
        self.aboutArea.setObjectName("aboutArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 257, 268))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.about_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.about_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.about_lbl.setWordWrap(True)
        self.about_lbl.setObjectName("about_lbl")
        self.gridLayout_2.addWidget(self.about_lbl, 0, 0, 1, 1)
        self.version_info_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.version_info_lbl.sizePolicy().hasHeightForWidth())
        self.version_info_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.version_info_lbl.setFont(font)
        self.version_info_lbl.setText("")
        self.version_info_lbl.setTextFormat(QtCore.Qt.RichText)
        self.version_info_lbl.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.version_info_lbl.setWordWrap(True)
        self.version_info_lbl.setObjectName("version_info_lbl")
        self.gridLayout_2.addWidget(self.version_info_lbl, 1, 0, 1, 1)
        self.build_info_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.build_info_lbl.sizePolicy().hasHeightForWidth())
        self.build_info_lbl.setSizePolicy(sizePolicy)
        self.build_info_lbl.setText("")
        self.build_info_lbl.setTextFormat(QtCore.Qt.RichText)
        self.build_info_lbl.setScaledContents(True)
        self.build_info_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.build_info_lbl.setWordWrap(True)
        self.build_info_lbl.setObjectName("build_info_lbl")
        self.gridLayout_2.addWidget(self.build_info_lbl, 2, 0, 1, 1)
        self.rights_info_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rights_info_lbl.sizePolicy().hasHeightForWidth())
        self.rights_info_lbl.setSizePolicy(sizePolicy)
        self.rights_info_lbl.setTextFormat(QtCore.Qt.RichText)
        self.rights_info_lbl.setScaledContents(True)
        self.rights_info_lbl.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.rights_info_lbl.setWordWrap(True)
        self.rights_info_lbl.setObjectName("rights_info_lbl")
        self.gridLayout_2.addWidget(self.rights_info_lbl, 3, 0, 1, 1)
        self.aboutArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.aboutArea)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "About Subtitles Distributor"))
        self.about_lbl.setText(_translate("AboutWindow", "<html><head/><body><p>Subtitles Distributor should be started <span style=\" font-weight:600; text-decoration: underline;\">before</span> any of the downloading of movies and subtitles has started. Therefore <span style=\" font-weight:600;\">please</span> provide the needed folder locations for <span style=\" font-weight:600;\">new subtitles</span> and<span style=\" font-weight:600;\"> movie files</span> and click on <span style=\" font-weight:600;\">Distribute</span>.</p><p>Subtitles Distributor will watch your subtitles and movies folders. When there is <span style=\" font-weight:600;\">new file </span>in any of those folders it expects to find <span style=\" font-weight:600;\">new file </span>in the other folder. Afterwards Subtitles Distributor extracts the subtitles into your new movie folder. </p><p>If it fails to extract the subtitles file it just copies it to the movie folder.</p></body></html>"))
        self.rights_info_lbl.setText(_translate("AboutWindow", "<html><head/><body><p>Copyright (C) 2017 Subtitles Distributor Ltd. All rights reserved.</p></body></html>"))

from . import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutWindow = QtWidgets.QDialog()
    ui = Ui_AboutWindow()
    ui.setupUi(AboutWindow)
    AboutWindow.show()
    sys.exit(app.exec_())


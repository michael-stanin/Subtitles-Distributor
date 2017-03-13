# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\Subtitles Distributor\src\gui\ui\DeveloperWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeveloperWindow(object):
    def setupUi(self, DeveloperWindow):
        DeveloperWindow.setObjectName("DeveloperWindow")
        DeveloperWindow.resize(372, 273)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DeveloperWindow.sizePolicy().hasHeightForWidth())
        DeveloperWindow.setSizePolicy(sizePolicy)
        DeveloperWindow.setMinimumSize(QtCore.QSize(372, 273))
        DeveloperWindow.setMaximumSize(QtCore.QSize(372, 273))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/subtitles_distributor_64_64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DeveloperWindow.setWindowIcon(icon)
        DeveloperWindow.setStyleSheet("QDialog {\n"
"    background-color: #F0F8FF;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(DeveloperWindow)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(DeveloperWindow)
        self.scrollArea.setStyleSheet("background-color: #F0F8FF;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 331, 262))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(DeveloperWindow)
        QtCore.QMetaObject.connectSlotsByName(DeveloperWindow)

    def retranslateUi(self, DeveloperWindow):
        _translate = QtCore.QCoreApplication.translate
        DeveloperWindow.setWindowTitle(_translate("DeveloperWindow", "Developer"))
        self.label.setText(_translate("DeveloperWindow", "<html><head/><body><p>I am <span style=\" font-weight:600;\">Michael Stanin</span>.</p><p>I am full time <span style=\" font-weight:600;\">C++ Developer</span> and I\'m strongly intrigued by the power Python provides.</p><p>I tend to watch a ton of movies and shows. This means that most of the time I need to extract subtitles to the movie folders again, and again, and again... </p><p>Then it struck me! <span style=\" font-weight:600;\">Subtitles Distributor </span>- simple application which watches two folders and when it finds new subtitles it extracts them in the new movie folder.</p><p>The application is open source: <span style=\" font-weight:600;\">Subtitles Distributor repository</span></p><p>Please do not hesitate to contact me at <span style=\" font-weight:600;\">michael.stanin@gmail.com</span> if you have any questions or concerns.</p></body></html>"))

from . import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeveloperWindow = QtWidgets.QDialog()
    ui = Ui_DeveloperWindow()
    ui.setupUi(DeveloperWindow)
    DeveloperWindow.show()
    sys.exit(app.exec_())


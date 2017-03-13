# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\Subtitles Distributor\src\gui\ui\limitationsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LimitationsWindow(object):
    def setupUi(self, LimitationsWindow):
        LimitationsWindow.setObjectName("LimitationsWindow")
        LimitationsWindow.resize(392, 293)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LimitationsWindow.sizePolicy().hasHeightForWidth())
        LimitationsWindow.setSizePolicy(sizePolicy)
        LimitationsWindow.setMinimumSize(QtCore.QSize(0, 0))
        LimitationsWindow.setMaximumSize(QtCore.QSize(392, 293))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/subtitles_distributor_64_64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LimitationsWindow.setWindowIcon(icon)
        LimitationsWindow.setStyleSheet("QDialog {\n"
"    background-color: #F0F8FF;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(LimitationsWindow)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(LimitationsWindow)
        self.scrollArea.setMinimumSize(QtCore.QSize(372, 273))
        self.scrollArea.setStyleSheet("background-color: #F0F8FF;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 351, 398))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_1.setWordWrap(True)
        self.label_1.setObjectName("label_1")
        self.gridLayout_2.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(LimitationsWindow)
        QtCore.QMetaObject.connectSlotsByName(LimitationsWindow)

    def retranslateUi(self, LimitationsWindow):
        _translate = QtCore.QCoreApplication.translate
        LimitationsWindow.setWindowTitle(_translate("LimitationsWindow", "Limitations"))
        self.label_3.setText(_translate("LimitationsWindow", "<html><head/><body><p>Subtitles Distributor supports the following file formats containing subtitles:</p><p>*.<span style=\" font-weight:600;\">zip</span>; *.<span style=\" font-weight:600;\">rar</span>; *.<span style=\" font-weight:600;\">7z</span>; *.<span style=\" font-weight:600;\">srt</span>; *.<span style=\" font-weight:600;\">sub</span></p><p><br/></p></body></html>"))
        self.label_1.setText(_translate("LimitationsWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Known Limitations</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_4.setText(_translate("LimitationsWindow", "<html><head/><body><p>Subtitles Distributor supports the following movie file formats:</p><p>*.<span style=\" font-weight:600;\">mkv</span>; *.<span style=\" font-weight:600;\">mpg</span>; *.<span style=\" font-weight:600;\">mp2</span>; *.<span style=\" font-weight:600;\">mpeg</span>; *.<span style=\" font-weight:600;\">mpe</span>; *.<span style=\" font-weight:600;\">mpv</span>; *.<span style=\" font-weight:600;\">m2v</span>; *.<span style=\" font-weight:600;\">mp4</span>; *.<span style=\" font-weight:600;\">m4p</span>; *.<span style=\" font-weight:600;\">m4v</span>; *.<span style=\" font-weight:600;\">flv</span>; *.<span style=\" font-weight:600;\">f4v</span>; *.<span style=\" font-weight:600;\">f4p</span>; *.<span style=\" font-weight:600;\">f4a</span>; *.<span style=\" font-weight:600;\">f4b</span>; *.<span style=\" font-weight:600;\">wmv</span>; *.<span style=\" font-weight:600;\">avi</span></p><p><br/></p></body></html>"))
        self.label_5.setText(_translate("LimitationsWindow", "<html><head/><body><p>Subtitles Distributor will extract the contents of an archive. With this said if the content is folder, Subtitles Distributor will only move this folder in the movie folder - it won\'t move the subtitles files from the folder from the archive to the movie folder.</p><p><br/></p></body></html>"))
        self.label_6.setText(_translate("LimitationsWindow", "<html><head/><body><p>In case you find problem or you have feature suggestions <span style=\" font-weight:600;\">please contact the Developer</span>.</p></body></html>"))

from . import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LimitationsWindow = QtWidgets.QDialog()
    ui = Ui_LimitationsWindow()
    ui.setupUi(LimitationsWindow)
    LimitationsWindow.show()
    sys.exit(app.exec_())


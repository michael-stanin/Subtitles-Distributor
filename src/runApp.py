import sys

from PyQt5 import QtWidgets

from gui.mainWindow import MainWindow

# TODO - add combo box with torrent downloaders folders
# TODO - open windows explorer when distributing is done

app = QtWidgets.QApplication(sys.argv)
playerWindow = MainWindow()
playerWindow.show()
app.aboutToQuit.connect(playerWindow.stop)
sys.exit(app.exec_())

from PyQt4 import QtCore, QtGui
import sys
from PyQt4.QtGui import QPixmap

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(True)



        self.lineEdit1 = QtGui.QLineEdit(self.page1)
        self.lineEdit1.setGeometry(QtCore.QRect(410, 340, 129, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit1.sizePolicy().hasHeightForWidth())
        self.lineEdit1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Chancery L"))
        font.setPointSize(18)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setAutoFillBackground(True)
        self.lineEdit1.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase)
        self.lineEdit1.setObjectName(_fromUtf8("lineEdit1"))
        self.label1 = QtGui.QLabel(self.page1)
        self.label1.setGeometry(QtCore.QRect(200, 320, 191, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Palladio L"))
        font.setPointSize(24)
        self.label1.setFont(font)
        self.label1.setAutoFillBackground(True)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.lineEdit1_2 = QtGui.QLineEdit(self.page1)
        self.lineEdit1_2.setGeometry(QtCore.QRect(410, 420, 129, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit1_2.sizePolicy().hasHeightForWidth())
        self.lineEdit1_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Chancery L"))
        font.setPointSize(18)
        self.lineEdit1_2.setFont(font)
        self.lineEdit1_2.setAutoFillBackground(True)
        self.lineEdit1_2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase)
        self.lineEdit1_2.setObjectName(_fromUtf8("lineEdit1_2"))
        self.label1_2 = QtGui.QLabel(self.page1)
        self.label1_2.setGeometry(QtCore.QRect(200, 390, 191, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Palladio L"))
        font.setPointSize(24)
        self.label1_2.setFont(font)
        self.label1_2.setAutoFillBackground(True)
        self.label1_2.setObjectName(_fromUtf8("label1_2"))
        self.label = QtGui.QLabel(self.page1)
        self.pixmap = QPixmap('small_400.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.setGeometry(QtCore.QRect(160, 70, 400, 233))
        self.label.setAutoFillBackground(True)
        self.label.setObjectName(_fromUtf8("label"))

        self.proceed = QtGui.QPushButton(self.page1)
        self.proceed.setGeometry(QtCore.QRect(330, 490, 121, 31))
        self.proceed.setObjectName(_fromUtf8("proceed"))





        MainWindow.setCentralWidget(self.page1)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label1.setText(_translate("MainWindow", "Interface :", None))
        self.label1_2.setText(_translate("MainWindow", "Timeout :", None))
        self.proceed.setText(_translate("MainWindow", "Proceed", None))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
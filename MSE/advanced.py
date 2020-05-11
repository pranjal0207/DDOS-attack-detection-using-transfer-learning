from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as plt
from matplotlib import style
from random import randint
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib
import sys
import threading
from time import sleep
import numpy as np

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12
color=["blue","green","red","cyan","magenta"]
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)

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

style.use('fivethirtyeight')

cur = 5

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
b=[]

for i in range(600):
    b.append(randint(1,30))

a = np.array(b)
a.resize(6,100)
print(a[0])

def clickable(widget):
    class Filter(QtCore.QObject):
    
        clicked = QtCore.pyqtSignal()
        
        def eventFilter(self, obj, event):
        
            if obj == widget:
                if event.type() == QtCore.QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True
            
            return False
    
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1500, 842)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setSpacing(30)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))

        self.w = QtGui.QWidget()
        self.b = QtGui.QLabel(self.w)
        self.b.setText("Sniffing on interface:")
        self.c = QtGui.QLabel(self.w)
        self.c.setText("Timeout Limit")
    
        self.c.move(2,30)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w.sizePolicy().hasHeightForWidth())
        self.verticalLayout_4.addWidget(self.w)

        self.fig5 = Figure(figsize=(1,1))
        self.canvas5 = FigureCanvas(self.fig5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas5.sizePolicy().hasHeightForWidth())
        clickable(self.canvas5).connect(lambda: self.swap(5))
        self.canvas5.setSizePolicy(sizePolicy)
        self.verticalLayout_4.addWidget(self.canvas5)
        
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.fig6 = Figure()
        self.canvas6 = FigureCanvas(self.fig6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas6.sizePolicy().hasHeightForWidth())
        self.canvas6.setSizePolicy(sizePolicy)
        #self.canvas6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #clickable(self.canvas6).connect(lambda: self.swap(5))
        self.horizontalLayout_2.addWidget(self.canvas6)


        self.horizontalLayout_2.setStretch(0, 24)
        self.horizontalLayout_2.setStretch(1, 76)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.fig1 = Figure(figsize=(1,1))
        self.canvas1 = FigureCanvas(self.fig1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas1.sizePolicy().hasHeightForWidth())
        self.canvas1.setSizePolicy(sizePolicy)
        self.canvas1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        clickable(self.canvas1).connect(lambda: self.swap(1))
        self.horizontalLayout.addWidget(self.canvas1)


        self.fig2 = Figure(figsize=(1,1))
        self.canvas2 = FigureCanvas(self.fig2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas2.sizePolicy().hasHeightForWidth())
        self.canvas2.setSizePolicy(sizePolicy)
        self.canvas2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        clickable(self.canvas2).connect(lambda: self.swap(2))
        self.horizontalLayout.mouseReleaseEvent = print("hey")
        self.horizontalLayout.addWidget(self.canvas2)

        self.fig3 = Figure(figsize=(1,1))
        self.canvas3 = FigureCanvas(self.fig3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas3.sizePolicy().hasHeightForWidth())
        self.canvas3.setSizePolicy(sizePolicy)
        self.canvas3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        clickable(self.canvas3).connect(lambda: self.swap(3))
        self.horizontalLayout.addWidget(self.canvas3)

        self.fig4 = Figure(figsize=(1,1))
        self.canvas4 = FigureCanvas(self.fig4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas4.sizePolicy().hasHeightForWidth())
        self.canvas4.setSizePolicy(sizePolicy)
        self.canvas4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        clickable(self.canvas4).connect(lambda: self.swap(4))
        self.horizontalLayout.addWidget(self.canvas4)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuStart = QtGui.QMenu(self.menubar)
        self.menuStart.setObjectName(_fromUtf8("menuStart"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionStart_sniffing = QtGui.QAction(MainWindow)
        self.actionStart_sniffing.setObjectName(_fromUtf8("actionStart_sniffing"))
        self.actionStart_sniffing.triggered.connect(self.plot)
        self.menuStart.addAction(self.actionStart_sniffing)
        self.menubar.addAction(self.menuStart.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def mousePressEvent(self, QMouseEvent):
        print (QMouseEvent.pos())

    def mouseReleaseEvent(self, QMouseEvent):
        cursor =QtGui.QCursor()
        print (cursor.pos()) 

    def swap(self,a):
        global cur
        cur = a


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuStart.setTitle(_translate("MainWindow", "Start", None))
        self.actionStart_sniffing.setText(_translate("MainWindow", "Start sniffing", None))


    def plot(self):
        global cur
        global a
        global color
        ax1 = self.fig1.add_subplot(111)
        ax1.clear()
        ax1.set_ylim([0,60])
        ax1.plot(a[0],linewidth=1.4,color=color[0])
        
        self.canvas1.draw()

        ax2 = self.fig2.add_subplot(111)
        ax2.clear()
        ax2.set_ylim([0,60])
        ax2.plot(a[1],linewidth=1.4,color=color[1])
        self.canvas2.draw()

        ax3 = self.fig3.add_subplot(111)
        ax3.clear()
        ax3.set_ylim([0,60])
        ax3.plot(a[2],linewidth=1.4,color=color[2])
        self.canvas3.draw()

        ax4 = self.fig4.add_subplot(111)
        ax4.clear()
        ax4.set_ylim([0,60])
        ax4.plot(a[3],linewidth=1.4,color=color[3])
        self.canvas4.draw()

        ax5 = self.fig5.add_subplot(111)
        ax5.clear()
        ax5.set_ylim([0,60])
        ax5.plot(a[4],linewidth=1.4,color=color[4])
        self.canvas5.draw()

        ax6 = self.fig6.add_subplot(111)
        ax6.clear()
        ax6.set_ylim([0,60])
        ax6.plot(a[cur-1],linewidth=3.0,color=color[cur-1])
        self.canvas6.draw()
        QtCore.QTimer.singleShot(100, self.plot)

def start_Application():
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

def start_Sniffing():
    global a
    while(1):
        a = np.delete(a, 0, axis=1)
        b = np.array([[randint(1,30)], [randint(1,30)],[randint(1,30)],[randint(1,30)], [randint(1,30)],[randint(1,30)]])
        a = np.append(a, b, axis = 1)
        sleep(0.)


if __name__ == "__main__":
    t1 = threading.Thread(target=start_Application)
    t2 = threading.Thread(target=start_Sniffing)
    t1.start()
    t2.start()

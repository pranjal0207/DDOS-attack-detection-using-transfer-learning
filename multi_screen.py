from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as plt
import python_arptable as arp
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
import pyshark
from PyQt4.QtGui import QPixmap
from keras.models import model_from_json, load_model
from sklearn.preprocessing import LabelEncoder

arp_attack = True
mac_add = "11.0.2"

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12
color=["blue","green","red","sienna","magenta"]
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

style.use(['fivethirtyeight'])

cur = 5
isListView = False
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
x_base = np.arange(100)
a = np.zeros([6,100], dtype = int)




lenOfArray = a.size

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

autoScroll = True
isListView = False
sniffingInterface = "default"
sniffingTimeOut = 5

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1500, 842)        
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(197, 197, 197)"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1500, 842))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))


        self.page1 = QtGui.QWidget()
        self.page1.setObjectName(_fromUtf8("page"))
        self.lineEdit1 = QtGui.QLineEdit(self.page1)
        self.lineEdit1.setGeometry(QtCore.QRect(810, 340, 129, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit1.sizePolicy().hasHeightForWidth())
        self.lineEdit1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Chancery L"))
        font.setPointSize(18)
        #self.lineEdit1.setStyleSheet(_fromUtf8("background-color: rgb(166, 166, 166)"))
        self.lineEdit1.setFont(font)
        self.lineEdit1.setAutoFillBackground(True)
        self.lineEdit1.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase)
        self.lineEdit1.setObjectName(_fromUtf8("lineEdit1"))
        self.label1 = QtGui.QLabel(self.page1)
        self.label1.setGeometry(QtCore.QRect(600, 320, 191, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Palladio L"))
        font.setPointSize(24)
        self.label1.setFont(font)
        self.label1.setAutoFillBackground(False)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.lineEdit1_2 = QtGui.QLineEdit(self.page1)
        self.lineEdit1_2.setGeometry(QtCore.QRect(810, 420, 129, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit1_2.sizePolicy().hasHeightForWidth())
        self.lineEdit1_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Chancery L"))
        font.setPointSize(18)
        self.lineEdit1_2.setFont(font)
        #self.lineEdit1_2.setStyleSheet(_fromUtf8("background-color: rgb(166, 166, 166)"))
        self.lineEdit1_2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase)
        self.lineEdit1_2.setObjectName(_fromUtf8("lineEdit1_2"))
        self.label1_2 = QtGui.QLabel(self.page1)
        self.label1_2.setGeometry(QtCore.QRect(600, 390, 191, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Palladio L"))
        font.setPointSize(24)
        self.label1_2.setFont(font)
        self.label1_2.setAutoFillBackground(True)
        self.label1_2.setObjectName(_fromUtf8("label1_2"))
        self.label = QtGui.QLabel(self.page1)
        self.pixmap = QPixmap('small_400.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.setGeometry(QtCore.QRect(560, 70, 400, 233))
        self.label.setAutoFillBackground(True)
        self.label.setObjectName(_fromUtf8("label"))

        self.proceed = QtGui.QPushButton(self.page1)
        #self.proceed.setStyleSheet(_fromUtf8("background-color: rgb(166, 166, 166)"))
        self.proceed.setGeometry(QtCore.QRect(730, 490, 121, 31))
        self.proceed.setObjectName(_fromUtf8("proceed"))
        self.proceed.clicked.connect(self.getInterface)

        self.stackedWidget.addWidget(self.page1)





        self.page2 = QtGui.QWidget()
        self.page2.setObjectName(_fromUtf8("page"))
        self.verticalLayout = QtGui.QVBoxLayout(self.page2)
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
        self.d = QtGui.QLabel(self.w)
        self.d.setText("ARP Table is Clean.\t\t")
        self.e = QtGui.QLabel(self.w)
        self.e.setText(".\t\t\t\t")
        self.listViewbtn = QtGui.QPushButton(self.w)
        self.listViewbtn.setGeometry(QtCore.QRect(40, 110, 75, 23))
        self.listViewbtn.setObjectName(_fromUtf8("List_View"))
        self.listViewbtn.clicked.connect(self.switchView)
    
        self.c.move(2,30)
        self.d.move(2,60)
        self.e.move(2,80)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w.sizePolicy().hasHeightForWidth())
        self.verticalLayout_4.addWidget(self.w)

        self.fig5 = Figure(figsize=(1,1))
        #self.fig5.patch.set_alpha(0.5)
        #self.ax = self.fig5.add_subplot(111)
        #self.ax.patch.set_facecolor('#ababab')
        #self.ax.patch.set_alpha(0.5)
        self.canvas5 = FigureCanvas(self.fig5)
        self.canvas5.setStyleSheet(_fromUtf8("background-color: transparent"))
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
        self.canvas6.setStyleSheet("background-color: transparent;")
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
        self.stackedWidget.addWidget(self.page2)

        #List view:
        self.page3 = QtGui.QWidget()
        self.page3.setObjectName(_fromUtf8("page"))
        self.verticalLayout_List = QtGui.QVBoxLayout(self.page3)
        self.verticalLayout_List.setObjectName(_fromUtf8("verticalLayout_List"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.cellClicked.connect(lambda:self.updateListView(self.tableWidget.currentRow()))
        print(dir(self.tableWidget.scroll))
        self.tableWidget.setColumnWidth(0,220)
        self.tableWidget.setColumnWidth(1,220)
        self.tableWidget.setColumnWidth(2,220)
        self.tableWidget.setColumnWidth(3,220)
        self.tableWidget.setColumnWidth(4,220)
        self.tableWidget.setColumnWidth(5,220)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.scrollToBottom()
        self.tableWidget.setRowCount(0)
        self.verticalLayout_List.addWidget(self.tableWidget)

        self.info = QtGui.QWidget()
        self.b1 = QtGui.QLabel(self.info)
        self.b1.setText("Sniffing on interface:")
        self.b2 = QtGui.QLabel(self.info)
        self.b2.setText("Sniffing on interface:")
        self.b2.move(0,30)
        self.b3 = QtGui.QLabel(self.info)
        self.b3.setText("Sniffing on interface:")
        self.b3.move(0,60)
        self.verticalLayout_List.addWidget(self.info)
        self.verticalLayout_List.setStretch(0, 4)
        self.verticalLayout_List.setStretch(1, 2)


        self.stackedWidget.addWidget(self.page3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.view = QtGui.QMenu(self.menubar)
        self.view.setObjectName(_fromUtf8("view")) 
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.change_View = QtGui.QAction(MainWindow)
        self.change_View.setObjectName(_fromUtf8("change_view"))
        self.change_View.triggered.connect(self.switchView)
        self.view.addAction(self.change_View)
        
        

        self.menubar.addAction(self.view.menuAction())
        


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
        self.listViewbtn.setText(_translate("List_View", "List View", None))
        self.change_View.setText(_translate("change_view", "List View", None))
        self.view.setTitle(_translate("MainWindow", "View", None))
        self.label1.setText(_translate("MainWindow", "Interface :", None))
        self.label1_2.setText(_translate("MainWindow", "Timeout :", None))
        self.proceed.setText(_translate("MainWindow", "Proceed", None))

    
    def getInterface(self):
        global sniffingInterface, sniffingTimeOut, t2
        sniffingInterface = self.lineEdit1.text()
        sniffingTimeOut = int(self.lineEdit1_2.text())
        print(sniffingInterface,sniffingTimeOut)
        self.stackedWidget.setCurrentIndex(1)
        self.plot()

    def switchView(self):
        global isListView
        if(isListView):
            self.change_View.setText("List View")
            self.stackedWidget.setCurrentIndex(1)
            isListView = False
        else:
            self.change_View.setText("Graphic View")
            self.stackedWidget.setCurrentIndex(2)
            isListView = True

    def plot(self):
        global cur
        global a
        global color
        global autoScroll
        global lenOfArray
        global x_base
        global arp_attack
        global mac_add
        
        ax1 = self.fig1.add_subplot(111)
        ax1.clear()
        ax1.set_ylim([0,60])
        ax1.fill_between(x_base,0,a[0,-100:],linewidth=1.4,color=color[0])
        
        self.canvas1.draw()

        ax2 = self.fig2.add_subplot(111)
        ax2.clear()
        ax2.set_ylim([0,60])
        ax2.fill_between(x_base,0,a[1,-100:],linewidth=1.4,color=color[1])
        self.canvas2.draw()

        ax3 = self.fig3.add_subplot(111)
        ax3.clear()
        ax3.set_ylim([0,60])
        ax3.fill_between(x_base,0,a[2,-100:],linewidth=1.4,color=color[2])
        self.canvas3.draw()

        ax4 = self.fig4.add_subplot(111)
        ax4.clear()
        ax4.set_ylim([0,60])
        ax4.fill_between(x_base,0,a[3,-100:],linewidth=1.4,color=color[3])
        self.canvas4.draw()

        ax5 = self.fig5.add_subplot(111)
        ax5.clear()
        ax5.set_ylim([0,60])
        ax5.fill_between(x_base,0,a[4,-100:],linewidth=1.4,color=color[4])
        self.canvas5.draw()

        ax6 = self.fig6.add_subplot(111)
        ax6.clear()
        ax6.set_ylim([0,60])
        ax6.fill_between(x_base,0,a[cur-1,-100:],linewidth=3.0,color=color[cur-1])
        self.canvas6.draw()
        if(lenOfArray<a.size):
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            for i in range(6):
                self.x = self.tableWidget.rowCount()
                self.tableWidget.setRowCount(self.x)
                self.tableWidget.setItem(self.x-1,i,QtGui.QTableWidgetItem(str(a[i,int(lenOfArray/6)])))
            if(autoScroll):
                self.tableWidget.scrollToBottom()   
            lenOfArray += 6  
        QtCore.QTimer.singleShot(1, self.plot)
        
        if(arp_attack):
            self.d.setText("ARP spoof detected")
            self.d.setStyleSheet(_fromUtf8("background-color: rgb(255, 10, 10)"))
            self.e.setText("Suspicious mac address: "+mac_add)
            self.e.setStyleSheet(_fromUtf8("background-color: rgb(255, 10, 10)"))
    

    def updateListView(self, x):
        global autoScroll
        autoScroll = False
        
        self.b1.setText("data"+str(a[0,x+100]))
        self.b2.setText("data"+str(a[1,x+100]))
        self.b3.setText("data"+str(a[2,x+100]))
        print(a[:,x+2])

def start_Application():
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())



##pyshark
def start_Sniping():
    global a, arp_attack
    capture = pyshark.LiveCapture(interface="eth0")
    """ capture.set_debug() """
    i = 0
    while(1):
        packet = pyshark.LiveCapture(interface= "eth0" )
        for cap in packet.sniff_continuously(packet_count=1):
            data = []
            if (i == 0) :
                pack_time = 0
                time = float(cap.sniff_timestamp)
                i = 1
            pack_time = float(cap.sniff_timestamp) - time
            time = float(cap.sniff_timestamp)
            size = cap.length
            packet = 1
            prot = cap.transport_layer
            
            if hasattr(cap, 'tcp'):
                port = cap.tcp.dstport
            if hasattr(cap, 'udp'):
                port = cap.udp.dstport
            print (pack_time, "\t", size, "\t", packet, "\t", prot, "\t", port)
            data.append(pack_time)
            data.append(packet)
            data.append(prot)
            data.append(port)
            start_Detection(data)
        b = np.array([[randint(1,30)], [randint(1,30)],[randint(1,30)],[randint(1,30)], [randint(1,30)],[randint(1,30)]])
        a = np.append(a, b, axis = 1)
        arp_tab = arp.get_arp_table()
        b,c = [],[]
        for i in range(len(arp_tab)):
            b.append(arp_tab[i]["IP address"])
            c.append(arp_tab[i]["HW address"])
        if(len(set(b))>len(set(c))):
            arp_attack = True
            
def start_Detection(data):
    
    encoder = LabelEncoder()

    encoder = LabelEncoder()
    encoder.classes_ = numpy.load('label.npy')
    data_np = np.array(data)
    
    data_np = encoder.transform(data_np)
    
    
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    # print("Loaded model from disk")


if __name__ == "__main__":
    t1 = threading.Thread(target=start_Application)
    t1.start()
    start_Sniping()
    
    
    
    
    
    
    

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from random import randint
import sys
from PyQt4 import QtGui,QtCore
import threading
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from time import sleep

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
a=[]
for i in range(100):
    a.append(randint(1,30))


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


class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        self.canvas.resize(800,500)
        # this is the Navigation widget
        # it takes the Canvas widget and a parent

        # Just some button connected to `plot` method
        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        # set the layout
        layout = QtGui.QVBoxLayout()
        self.canvas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        clickable(self.canvas).connect(self.swap)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def f(self):
        ani = animation.FuncAnimation(fig, self.plot, interval=100)

    def plot(self):
        ''' plot some random stuff '''
        # random data

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.clear()

        # plot data
        
        ax.plot(a, '*-')

        # refresh canvas
        self.canvas.draw()
        QtCore.QTimer.singleShot(100, self.plot)

def start_app():
    app = QtGui.QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())

def start_Modification():
    while(1):
        del a[0]
        a.append(randint(1,30))
        sleep(0.1)

if __name__ == '__main__':
    t1 = threading.Thread(target=start_app) 
    t2 = threading.Thread(target=start_Modification) 
    t1.start()
    t2.start()
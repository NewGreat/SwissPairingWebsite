import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Battle Plan")
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit",self)
        btn.clicked.connect(self.close_appication)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,0)
        self.show()

    def close_appication(self):
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
    


import sys
import os
from PyQt4 import QtCore, QtGui

from res import open_cast as Ui_Form
from src import find_ip as ip

class MyForm(QtGui.QMainWindow,):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form.Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.strstop.setEnabled(False)
        self.ui.strprev.setEnabled(False)
        self.ui.recstop.setEnabled(False)
        self.ui.strlabl.setVisible(False)
        self.ui.reclabl.setVisible(False)
######  Slots and connectors


        self.ui.strstart.clicked.connect(self.stream_start)
        self.ui.recstart.clicked.connect(self.rec_start)
        self.ui.strstop.clicked.connect(self.stream_stop)
        self.ui.recstop.clicked.connect(self.rec_stop)
        self.ui.actionExit.triggered.connect(self.custom_exit)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.strprev.clicked.connect(self.preview)

#######  custom stuff 
    def preview(self,e):
        newpid = os.fork()
        if newpid == 0:
           os.execl('src/Stream','Stream')
    def stream_start(self,e):
        self.ui.strstop.setEnabled(True)
        self.ui.strprev.setEnabled(True)
        self.ui.strstart.setEnabled(False)
        self.ui.strlabl.setVisible(True)
        str1=ip.get_ip_address('wlan0')
        msg="Streaming at rtsp://"+str1+":8554/test"
        self.ui.strlabl.setText(msg)
        newpid = os.fork()
        if newpid == 0:
           newpid = os.fork()
           if newpid == 0:
               os.execl('src/record','record')
           os.execl('src/rtsp','rtsp')

    def rec_start(self,e):
        self.ui.recstop.setEnabled(True)
        self.ui.recstart.setEnabled(False)
        self.ui.reclabl.setVisible(True)
        if self.ui.gwin.isChecked():
            newpid = os.fork()
            if newpid == 0:
                  os.execl('/usr/bin/python','python','src/open_rec.py','1')
        else:
            newpid = os.fork()
            if newpid == 0:
                  os.execl('/usr/bin/python','python','src/open_rec.py','0')

    def stream_stop(self,e):
        self.ui.strlabl.setVisible(False)
        self.ui.strstop.setEnabled(False)
        self.ui.strprev.setEnabled(False)
        self.ui.strstart.setEnabled(True)
        newpid = os.fork()
        if newpid == 0:
           newpid = os.fork()
           if newpid == 0:
              os.execl('/usr/bin/killall','killall','rtsp')
           os.execl('/usr/bin/killall','killall','record')

    def rec_stop(self,e):
        self.ui.reclabl.setVisible(False)
        self.ui.recstop.setEnabled(False)
        self.ui.recstart.setEnabled(True)
        newpid = os.fork()
        if newpid == 0:
            os.execl('/usr/bin/killall','killall','avconv')


    def about(self):
        QtGui.QMessageBox.about(self, "About Open Cast",
                "<p>The <b>Open Cast</b> service is created " \
                "to enable people to easily record and cast their screens " \
                "to devices connected in the same network .</p> " \
                "<p> This program comes with ABSOLUTELY NO WARRANTY </p>")

    def custom_exit(self):
        #print "sorks"
        sys.exit(app.exec_())

## start
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

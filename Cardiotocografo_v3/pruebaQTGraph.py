import sys
from PyQt4 import QtGui, QtCore

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)

        scrolllayout = QtGui.QVBoxLayout()

        scrollwidget = QtGui.QWidget()
        scrollwidget.setLayout(scrolllayout)

        scroll = QtGui.QScrollArea()
        scroll.setWidgetResizable(True)  # Set to make the inner widget resize with scroll area
        scroll.setWidget(scrollwidget)

        self.groupboxes = []  # Keep a reference to groupboxes for later use
        for i in range(8):    # 8 groupboxes with textedit in them
            groupbox = QtGui.QGroupBox('%d' % i)
            grouplayout = QtGui.QHBoxLayout()
            grouptext = QtGui.QTextEdit()
            grouplayout.addWidget(grouptext)
            groupbox.setLayout(grouplayout)
            scrolllayout.addWidget(groupbox)
            self.groupboxes.append(groupbox)

        self.buttonbox = QtGui.QDialogButtonBox()
        self.buttonbox.setOrientation(QtCore.Qt.Vertical)
        self.buttonbox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)

        layout = QtGui.QHBoxLayout()
        layout.addWidget(scroll)
        #layout.addWidget(self.buttonbox)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
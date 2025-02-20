import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

# GUI FILE
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.setWindowTitle("Association Rule Application")

        ## TOGGLE MENU
        ########################################################################
        self.ui.btn_nav.clicked.connect(lambda: self.ui.toggleMenu(70, 150))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.btnPageClicked(self.ui.page_1, self.ui.btn_page_1))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.btnPageClicked(self.ui.page_2, self.ui.btn_page_2))

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.btnPageClicked(self.ui.page_3, self.ui.btn_page_3))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

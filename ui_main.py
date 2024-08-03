import csv
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem

from PyQt5.QtCore import (QCoreApplication, 
                          QMetaObject, 
                          QObject, 
                          QPoint, 
                          QPropertyAnimation, 
                          QRect, 
                          QSize, 
                          QUrl, 
                          Qt)

from PyQt5.QtGui import (QBrush, 
                         QColor, 
                         QConicalGradient, 
                         QCursor, 
                         QFont, 
                         QFontDatabase, 
                         QIcon, 
                         QLinearGradient, 
                         QPalette, 
                         QPainter, 
                         QPixmap, 
                         QRadialGradient)

from PyQt5.QtWidgets import *
from apyori import apriori

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.dataset = []
        self.dataset2 = []
        
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        
        MainWindow.setFixedSize(1000, 500)
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.col_top = QFrame(self.centralwidget)
        self.col_top.setObjectName(u"col_top")
        self.col_top.setMaximumSize(QSize(16777215, 40))
        self.col_top.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.col_top.setFrameShape(QFrame.NoFrame)
        self.col_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout = QHBoxLayout(self.col_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.frame_nav = QFrame(self.col_top)
        self.frame_nav.setObjectName(u"frame_nav")
        self.frame_nav.setMaximumSize(QSize(70, 40))
        self.frame_nav.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_nav.setFrameShape(QFrame.StyledPanel)
        self.frame_nav.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2 = QVBoxLayout(self.frame_nav)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.btn_nav = QPushButton(self.frame_nav)
        self.btn_nav.setIcon(QIcon('images/toggle1.png'))
        self.btn_nav.setIconSize(QSize(25, 25))
        self.btn_nav.setObjectName(u"btn_nav")

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_nav.sizePolicy().hasHeightForWidth())

        self.css_btn_1 = u"QPushButton {\n"\
                        "background-color: #176B87;\n"\
                        "color: #F5F5F5;\n"\
                        "border-radius : 6px;font-weight: bold }\n"\
                        "QPushButton:hover {\n"\
                        "background-color: rgb(0, 80, 110); }"

        self.btn_nav.setSizePolicy(sizePolicy)
        self.btn_nav.setStyleSheet(u"QPushButton {\n"
                                    "background-color: #176B87;\n"
                                    "border: 0px solid;\n }"
                                    "QPushButton:hover {\n"
                                    "background-color: rgb(0, 80, 110); }")

        self.verticalLayout_2.addWidget(self.btn_nav)
        self.horizontalLayout.addWidget(self.frame_nav)

        self.frm_top = QFrame(self.col_top)
        self.frm_top.setObjectName(u"frm_top")
        self.frm_top.setFrameShape(QFrame.StyledPanel)
        self.frm_top.setFrameShadow(QFrame.Raised)

        self.lbl_assoc_rule_data_anls = QtWidgets.QLabel(self.frm_top)
        self.lbl_assoc_rule_data_anls.setGeometry(QtCore.QRect(20, 11, 200, 16))
        self.lbl_assoc_rule_data_anls.setStyleSheet("color: white;\nfont-weight: bold;")
        self.lbl_assoc_rule_data_anls.setObjectName("lbl_assoc_rule_data_anls")

        self.horizontalLayout.addWidget(self.frm_top)
        self.verticalLayout.addWidget(self.col_top)

        self.col_bottom = QFrame(self.centralwidget)
        self.col_bottom.setObjectName(u"col_bottom")
        self.col_bottom.setFrameShape(QFrame.NoFrame)
        self.col_bottom.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2 = QHBoxLayout(self.col_bottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.frm_left_menu = QFrame(self.col_bottom)
        self.frm_left_menu.setObjectName(u"frm_left_menu")
        self.frm_left_menu.setMinimumSize(QSize(70, 0))
        self.frm_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frm_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frm_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frm_left_menu.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3 = QVBoxLayout(self.frm_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.frm_top_menus = QFrame(self.frm_left_menu)
        self.frm_top_menus.setObjectName(u"frm_top_menus")
        self.frm_top_menus.setFrameShape(QFrame.NoFrame)
        self.frm_top_menus.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4 = QVBoxLayout(self.frm_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.css_btn_2 = u"QPushButton {\n"\
                                        "color: rgb(255, 255, 255);\n"\
                                        "background-color: rgb(35, 35, 35);\n"\
                                        "border: 0px solid;\nfont-weight: bold"\
                                        "}\n"\
                                        "QPushButton:hover {\n"\
                                        "background-color: rgb(60, 60, 60);\n"\
                                        "}"
        self.css_btn_2h = u"QPushButton {\n"\
                                        "color: rgb(255, 255, 255);\n"\
                                        "background-color: rgb(25, 25, 25);\n"\
                                        "border: 0px solid;\nfont-weight: bold"\
                                        "}\n"\
                                        "QPushButton:hover {\n"\
                                        "background-color: rgb(60, 60, 60);\n"\
                                        "}"

        self.btn_page_1 = QPushButton(self.frm_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0,80))
        self.btn_page_1.setIcon(QIcon('images/file.png'))
        self.btn_page_1.setIconSize(QSize(40,40))
        self.btn_page_1.setStyleSheet(self.css_btn_2)
        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frm_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0,80))
        self.btn_page_2.setIcon(QIcon('images/parameter.png'))
        self.btn_page_2.setIconSize(QSize(40,40))
        self.btn_page_2.setStyleSheet(self.css_btn_2)
        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frm_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0,80))
        self.btn_page_3.setIcon(QIcon('images/table.png'))
        self.btn_page_3.setIconSize(QSize(40,40))
        self.btn_page_3.setStyleSheet(self.css_btn_2)
        self.verticalLayout_4.addWidget(self.btn_page_3)

        self.btn_pages = [self.btn_page_1, self.btn_page_2, self.btn_page_3]

        self.verticalLayout_4.addWidget(self.btn_page_3)
        self.verticalLayout_3.addWidget(self.frm_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frm_left_menu)

        self.frm_pages = QtWidgets.QFrame(self.col_bottom)
        self.frm_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_pages.setObjectName("frm_pages")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frm_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.stackedWidget = QtWidgets.QStackedWidget(self.frm_pages)
        self.stackedWidget.setObjectName("stackedWidget")

        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")

        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.widget_page_1 = QtWidgets.QWidget(self.page_1)
        self.widget_page_1.setObjectName("widget_page_1")

        self.btn_open_file = QtWidgets.QPushButton(self.widget_page_1)
        self.btn_open_file.clicked.connect(self.open_file)
        self.btn_open_file.setGeometry(QtCore.QRect(320, 390, 100, 30))
        self.btn_open_file.setStyleSheet(self.css_btn_1)
        self.btn_open_file.setObjectName("btn_open_file")

        self.btn_reset = QtWidgets.QPushButton(self.widget_page_1)
        self.btn_reset.clicked.connect(self.reset_data)
        self.btn_reset.setGeometry(QtCore.QRect(470, 390, 100, 30))
        self.btn_reset.setStyleSheet(self.css_btn_1)
        self.btn_reset.setObjectName("btn_reset")

        self.tableWidget_1 = QtWidgets.QTableWidget(self.widget_page_1)
        self.tableWidget_1.setGeometry(QtCore.QRect(30, 10, 831, 371))
        self.tableWidget_1.setObjectName("tableWidget_1")
        self.tableWidget_1.setColumnCount(0)
        self.tableWidget_1.setRowCount(0)
        self.tableWidget_1.setStyleSheet(u"QTableView { background-color:#232326; color: white; gridline-color: white; }"
                            "QTableView::item:selected { color:black; background:green; font-weight:900; }"
                            "QTableCornerButton::section { background-color:#232326; }"
                            "QHeaderView::section { color:white; background-color:#232326; outline-color: white; }")

        self.lbl_error_widget_page_1 = QtWidgets.QLabel(self.widget_page_1)
        self.lbl_error_widget_page_1.setGeometry(QtCore.QRect(260, 185, 400, 30))
        self.lbl_error_widget_page_1.setStyleSheet("color: white;font-size: 20px; background-color:#232326;")
        self.lbl_error_widget_page_1.setObjectName("lbl_error_widget_page_1")
        self.lbl_error_widget_page_1.setVisible(False)


        self.verticalLayout_7.addWidget(self.widget_page_1)
        self.stackedWidget.addWidget(self.page_1)

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")

        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.widget_2 = QtWidgets.QWidget(self.page_2)
        self.widget_2.setObjectName("widget_2")

        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(0, -10, 161, 431))
        self.widget_3.setObjectName("widget_3")

        self.hrz_sld_1 = QtWidgets.QSlider(self.widget_3)
        self.hrz_sld_1.setGeometry(QtCore.QRect(0, 100, 160, 22))
        self.hrz_sld_1.setOrientation(QtCore.Qt.Horizontal)
        self.hrz_sld_1.setObjectName("hrz_sld_1")
        self.hrz_sld_1.setRange(1, 10)
        self.hrz_sld_1.setValue(1)
        self.hrz_sld_1.valueChanged.connect(lambda: self.lbl_max_item.setText(f"Max Item per Itemset: {self.hrz_sld_1.value()}"))

        self.hrz_sld_2 = QtWidgets.QSlider(self.widget_3)
        self.hrz_sld_2.setGeometry(QtCore.QRect(0, 190, 160, 22))
        self.hrz_sld_2.setOrientation(QtCore.Qt.Horizontal)
        self.hrz_sld_2.setObjectName("hrz_sld_2")
        self.hrz_sld_2.setRange(1, 100)
        self.hrz_sld_2.setValue(1)
        self.hrz_sld_2.valueChanged.connect(lambda: self.lbl_confidence_val.setText(f"Confidence Value: {self.hrz_sld_2.value()}"))

        self.hrz_sld_3 = QtWidgets.QSlider(self.widget_3)
        self.hrz_sld_3.setGeometry(QtCore.QRect(0, 280, 160, 22))
        self.hrz_sld_3.setOrientation(QtCore.Qt.Horizontal)
        self.hrz_sld_3.setObjectName("hrz_sld_3")
        self.hrz_sld_3.setRange(1, 100)
        self.hrz_sld_3.setValue(1)
        self.hrz_sld_3.valueChanged.connect(lambda: self.lbl_support_val.setText(f"Support Value: {self.hrz_sld_3.value()}"))

        self.list_widget = QtWidgets.QListWidget(self.widget_2)
        self.list_widget.setGeometry(QtCore.QRect(185, 1, 701, 421))
        self.list_widget.setObjectName("list_widget")
        self.list_widget.setStyleSheet(" background-color:#232326; color: white; font-weight:900;")

        self.btn_start = QtWidgets.QPushButton(self.widget_3)
        self.btn_start.clicked.connect(self.run_apriori)
        self.btn_start.setGeometry(QtCore.QRect(50, 390, 75, 23))
        self.btn_start.setStyleSheet(self.css_btn_1)
        self.btn_start.setObjectName("btn_start")

        self.lbl_parameter_tuning = QtWidgets.QLabel(self.widget_3) 
        self.lbl_parameter_tuning.setGeometry(QtCore.QRect(0, 10, 121, 21))
        self.lbl_parameter_tuning.setStyleSheet("color: white;font-weight: bold;")
        self.lbl_parameter_tuning.setObjectName("lbl_parameter_tuning")


        self.lbl_max_item = QtWidgets.QLabel(self.widget_3) #max item
        self.lbl_max_item.setGeometry(QtCore.QRect(0, 80, 160, 16))
        self.lbl_max_item.setStyleSheet("color: white;")
        self.lbl_max_item.setObjectName("lbl_max_item")

        self.lbl_confidence_val = QtWidgets.QLabel(self.widget_3) #confidence
        self.lbl_confidence_val.setGeometry(QtCore.QRect(0, 170, 160, 16))
        self.lbl_confidence_val.setStyleSheet("color: white;")
        self.lbl_confidence_val.setObjectName("lbl_confidence_val")

        self.lbl_support_val = QtWidgets.QLabel(self.widget_3) #support value
        self.lbl_support_val.setGeometry(QtCore.QRect(0, 260, 160, 16))
        self.lbl_support_val.setStyleSheet("color: white;")
        self.lbl_support_val.setObjectName("lbl_support_val")

        self.verticalLayout_6.addWidget(self.widget_2)
        self.stackedWidget.addWidget(self.page_2)

        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")

        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.widget_page_3 = QtWidgets.QWidget(self.page_3)
        self.widget_page_3.setObjectName("widget_page_3")

        self.btn_save_file = QtWidgets.QPushButton(self.widget_page_3)
        self.btn_save_file.clicked.connect(self.save_csv)
        self.btn_save_file.setGeometry(QtCore.QRect(400, 390, 100, 30))
        self.btn_save_file.setStyleSheet(self.css_btn_1)
        self.btn_save_file.setObjectName("btn_save_file")

        self.tableWidget_3 = QtWidgets.QTableWidget(self.widget_page_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(30, 10, 831, 371))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.setStyleSheet(u"QTableView { background-color:#232326; color: white; gridline-color: white; }"
                            "QTableView::item:selected { color:black; background:green; font-weight:900; }"
                            "QTableCornerButton::section { background-color:#232326; }"
                            "QHeaderView::section { color:white; background-color:#232326; outline-color: white; }")

        self.lbl_error_widget_page_3 = QtWidgets.QLabel(self.widget_page_3)
        self.lbl_error_widget_page_3.setStyleSheet("color: white;font-size: 20px; background-color:#232326;")
        self.lbl_error_widget_page_3.setObjectName("lbl_error_widget_page_3")
        self.lbl_error_widget_page_3.setVisible(False)

        self.verticalLayout_8.addWidget(self.widget_page_3)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frm_pages)
        self.verticalLayout.addWidget(self.col_bottom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

        self.btn_page_1.setStyleSheet(self.css_btn_2h)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lbl_assoc_rule_data_anls.setText(_translate("MainWindow", "Association Rule Data Analysis", None))
        self.lbl_error_widget_page_1.setText('Invalid file type! Please upload a  .csv  file')
        self.lbl_error_widget_page_3.setText('Dataset is empty! Please click \"Start\" to update the dataset')
        self.btn_open_file.setText(_translate("MainWindow", "Upload Folder", None))
        self.btn_reset.setText(_translate("MainWindow", "Reset", None))
        self.btn_save_file.setText(_translate("MainWindow", "Save as CSV", None))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.lbl_parameter_tuning.setText(_translate("MainWindow", "Parameter Tuning"))
        self.lbl_max_item.setText(_translate("MainWindow", f"Max Item per Itemset: {self.hrz_sld_1.value()}"))
        self.lbl_confidence_val.setText(_translate("MainWindow", f"Confidence Value: {self.hrz_sld_2.value()}"))
        self.lbl_support_val.setText(_translate("MainWindow", f"Support Value: {self.hrz_sld_3.value()}"))
    # retranslateUi
        
    def open_file(self):
        file_dialog = QFileDialog()
        file_dialog.fileSelected.connect(self.load_csv)
        file_dialog.exec_()
        
    def load_csv(self, file):
        if file.endswith('.csv'):
            self.lbl_error_widget_page_1.setVisible(False)

            with open(file, "r") as f:
                lines = f.readlines()

            row_count = len(lines)
            column_count = len(lines[0].split(","))

            self.tableWidget_1.setRowCount(row_count)
            self.tableWidget_1.setColumnCount(column_count)

            for i, line in enumerate(lines):
                cells = line.split(",")
                row_data = []  # Create a new list to hold the values for the current row
                for j, cell in enumerate(cells):
                    item = QTableWidgetItem(cell.strip())
                    self.tableWidget_1.setItem(i, j, item)
                    row_data.append(cell.strip())  # Append the value to the row_data list
                self.dataset.append(row_data)  # Append the row_data list to the dataset list

            self.tableWidget_1.resizeColumnsToContents()
            self.tableWidget_1.resizeRowsToContents()
        else:
            self.tableWidget_1.setRowCount(0)
            self.tableWidget_1.setColumnCount(0)
            self.lbl_error_widget_page_1.setVisible(True)

    def save_csv(self):
        if len(self.dataset) == 0:
            self.lbl_error_widget_page_3.setGeometry(QtCore.QRect(250, 185, 400, 30))
            self.lbl_error_widget_page_3.setText("Dataset is empty! Please upload a  .csv  file")
            self.lbl_error_widget_page_3.setVisible(True)
        elif len(self.dataset2) == 0:
            self.lbl_error_widget_page_3.setGeometry(QtCore.QRect(180, 185, 550, 30))
            self.lbl_error_widget_page_3.setText("Dataset is empty! Please click \"Start\" to update the dataset")
            self.lbl_error_widget_page_3.setVisible(True)
        else:
            self.lbl_error_widget_page_3.setVisible(False)
            filename, _ = QFileDialog.getSaveFileName(None, "Save CSV", "", "CSV Files (*.csv)")

            if filename:
                with open(filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(self.dataset2)

    def reset_data(self):
        self.dataset.clear()
        self.dataset2.clear()
        self.tableWidget_1.setRowCount(0)
        self.tableWidget_1.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.setColumnCount(0)
        self.list_widget.clear()
        self.lbl_error_widget_page_1.setVisible(False)
        self.lbl_error_widget_page_3.setVisible(False)
        self.hrz_sld_1.setValue(1)
        self.hrz_sld_2.setValue(1)
        self.hrz_sld_3.setValue(1)
        
    def run_apriori(self):

        self.lbl_error_widget_page_3.setVisible(False)

        # Clear the result list
        self.list_widget.clear()

        # Get parameter values from sliders
        num_itemsets = self.hrz_sld_1.value()
        confidence_value = self.hrz_sld_2.value() / 100
        support_value = self.hrz_sld_3.value() / 100

        # Run Apriori algorithm using apyori library```python
        results = None
        if num_itemsets < 2:
            results = list(apriori(self.dataset, min_support=support_value, min_confidence=confidence_value, min_lift=1, min_length=2, max_length = 2))
        else:
            results = list(apriori(self.dataset, min_support=support_value, min_confidence=confidence_value, min_lift=1, min_length=num_itemsets, max_length = num_itemsets))

        # Print the result
        self.list_widget.addItem(f"Number of Itemsets: {num_itemsets}")
        self.list_widget.addItem(f"Confidence Value: {confidence_value}")
        self.list_widget.addItem(f"Support Value: {support_value}")
        self.list_widget.addItem("")  # Add an empty line

        # Dataset for 3rd page
        self.dataset2 = []

        # Display the result
        for index in range(len(results)):

            items = [item for item in results[index].items]
            support = results[index].support
            confidence = results[index].ordered_statistics[0].confidence
            lift = results[index].ordered_statistics[0].lift

            if len(items) <= num_itemsets:
                self.list_widget.addItem(f"Items: {items}")
                self.list_widget.addItem(f"Confidence: {confidence}")
                self.list_widget.addItem(f"Support: {support}")
                self.list_widget.addItem(f"Lift: {lift}")
                self.list_widget.addItem("")  # Add an empty line

            if len(items) == 2:
                list_value = []
                list_value.append(items[0])
                list_value.append(items[1])
                list_value.append(support)
                list_value.append(confidence)
                list_value.append(lift)
                self.dataset2.append(list_value)

        self.tableWidget_3.setRowCount(len(self.dataset2))
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setHorizontalHeaderLabels(['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])

        for row in range(len(self.dataset2)):
            for column in range(5):
                value = QTableWidgetItem(str(self.dataset2[row][column]))
                self.tableWidget_3.setItem(row, column, value)

        self.tableWidget_3.resizeColumnsToContents()
        self.tableWidget_3.resizeRowsToContents()

    def toggleMenu(self, standard, maxWidth):

        width = self.frm_left_menu.width()
        
        # SET MAX WIDTH
        if  width == standard:
            widthExtended = maxWidth
            self.btn_nav.setIcon(QIcon("images/toggle2.png"))
            self.btn_page_1.setText("     Folder          ")
            self.btn_page_2.setText("    Parameter ")
            self.btn_page_3.setText("     Format        ")
        else:
            widthExtended = standard
            self.btn_nav.setIcon(QIcon("images/toggle1.png"))
            self.btn_page_1.setText("")
            self.btn_page_2.setText("")
            self.btn_page_3.setText("")

        # ANIMATION
        self.animation = QPropertyAnimation(self.frm_left_menu, b"minimumWidth")
        self.animation.setDuration(400)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    
    def btnPageClicked(self, page, button):

        for i in self.btn_pages:
            if i == button:
                i.setStyleSheet(self.css_btn_2h)
            else:
                i.setStyleSheet(self.css_btn_2)
        self.stackedWidget.setCurrentWidget(page)